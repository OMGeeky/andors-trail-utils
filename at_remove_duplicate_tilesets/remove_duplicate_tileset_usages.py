import shutil
import base64
import sys
import xml.etree.ElementTree
import zlib
import gzip
import struct
from re import RegexFlag
from typing import Any
import re


def get_min_gid_after(after: int, tilesets: list[tuple[Any, int]]):
    return min(
        (tileset[1] for tileset in tilesets if tileset[1] > after), default=9999999999
    )


def remove_tilesets(
    filepath: str, duplicates: list[tuple[int, int, int, str, int, int]]
):
    print(f"writing file: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    for duplicate in duplicates:
        content = remove_tileset_with_regex(content, duplicate[3], duplicate[0])

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    pass


def remove_tileset_with_regex(content, tileset_name, tileset_first_gid):
    first_gid = tileset_first_gid
    name = tileset_name
    modified = re.sub(
        f' <[^<]*firstgid="{first_gid}"[^<]*({name})[\\S\\s]*?</tileset>\\r?\\n',
        "",
        content,
        1,
        RegexFlag.MULTILINE,
    )
    return modified


def remove_duplicate_usages(xml_file_path: str):
    print(f"checking {xml_file_path}")
    tree = xml.etree.ElementTree.parse(xml_file_path)
    root = tree.getroot()
    tileset_elements_list: list[Any] = root.findall("tileset")
    tilesets_list: list[tuple[str, int]] = [
        (tileset.get("name"), int(tileset.get("firstgid")))
        for tileset in tileset_elements_list
    ]
    duplicates = find_duplicates(tilesets_list)
    found_duplicate = len(duplicates) > 0

    if not found_duplicate:
        print("no duplicates found")
        return

    # basically a map where the first two numbers are the range, that needs to be
    # subtracted by the third number to go from the duplicate to the first tileset
    duplicate_usages_maps: list[tuple[int, int, int, str, int, int]] = []
    for name, duplicate_list in duplicates.items():
        for i, duplicate in enumerate(duplicate_list):
            gid_dup = max(duplicate[0], duplicate[1])
            gid_not_dup = min(duplicate[0], duplicate[1])
            duplicate_usages_maps.append(
                (
                    gid_dup,
                    get_min_gid_after(gid_dup, tilesets_list),
                    gid_dup - gid_not_dup,
                    name,
                    i,
                    gid_not_dup,
                )
            )

    # go through each layer and remove all usages of these duplicates
    target_elements = root.findall("layer")
    for target_element in target_elements:
        data_element = target_element.find("data")
        encoding = data_element.get("encoding")
        compression = data_element.get("compression")

        data = data_element.text
        if data is None or data == "":
            continue

        gid_data = read_data_from_str(data, encoding, compression)
        found_change_in_layer = False

        # check and apply all mappings
        for duplicate_usages_map in duplicate_usages_maps:
            for i, gid in enumerate(gid_data):
                if duplicate_usages_map[0] <= gid < duplicate_usages_map[1]:
                    # reduce the duplicate usage by the offset to use the first tile-set
                    gid_data[i] -= duplicate_usages_map[2]
                    found_change_in_layer = True

        if found_change_in_layer:
            modified_data_str = write_data_to_str(compression, encoding, gid_data)
            print(f"writing file: {xml_file_path}")
            with open(xml_file_path, "r", encoding="utf-8") as f:
                original = f.read()
            with open(xml_file_path, "w", encoding="utf-8") as f:
                modified = original.replace(data, modified_data_str)
                f.write(modified)

    remove_tilesets(xml_file_path, duplicate_usages_maps)

    print(
        "XML file had duplicate tilesets. They were removed automatically"
        f", so please check if this worked: '{xml_file_path}' "
    )


def find_duplicates(
    tilesets_list: list[tuple[str, int]]
) -> dict[str, list[tuple[int, int]]]:
    duplicates: dict[str, list[tuple[int, int]]] = {}
    tilesets: dict[str, int] = {}
    for tileset in tilesets_list:
        current_name = tileset[0]
        first_gid = tileset[1]
        if first_gid is None:
            raise Exception("This tileset had no first_gid")

        first_gid = int(first_gid)
        if tilesets.get(current_name) is None:
            tilesets[current_name] = first_gid
        else:
            print(f"  - '{current_name}'")
            duplicate_list = duplicates.get(current_name)
            duplicate_value = (
                tilesets.get(current_name),
                first_gid,
            )
            if duplicate_list is None:
                duplicates[current_name] = [duplicate_value]
            else:
                duplicate_list.append(duplicate_value)
    return duplicates


def read_data_from_str(data: str, encoding: str, compression: str) -> list[int]:
    gid_data_str = decode_decompress(data, encoding, compression)

    data_len = len(gid_data_str)
    amount_of_ints = data_len // 4
    struct_format = get_struct_format(amount_of_ints)
    gid_data = list(struct.unpack(struct_format, gid_data_str))
    return gid_data


def write_data_to_str(compression: str, encoding: str, gid_data: list[int]) -> str:
    modified_data = struct.pack(get_struct_format(len(gid_data)), *gid_data)
    encoded_data = encode_compress(modified_data, encoding, compression)
    modified_data_str = encoded_data.decode("utf-8")
    return modified_data_str


def get_struct_format(amount_of_ints: int) -> str:
    """The format required to use struct.pack(...) and struct.unpack(...)"""
    struct_format = "<" + "I" * amount_of_ints
    return struct_format


def encode_compress(content: bytes, encoding: str, compression: str):
    fn_base64 = base64.b64encode
    fn_zlib = zlib.compress
    fn_gzip = gzip.compress

    data = do_zlib_gzip_fn(compression, content, fn_gzip, fn_zlib)
    data = do_base64_csv_fn(encoding, data, fn_base64)
    return data


def decode_decompress(content: str, encoding: str, compression: str) -> bytes:
    fn_base64 = base64.b64decode
    fn_zlib = zlib.decompress
    fn_gzip = gzip.decompress

    data = do_base64_csv_fn(encoding, content, fn_base64)
    data = do_zlib_gzip_fn(compression, data, fn_gzip, fn_zlib)
    return data


def do_base64_csv_fn(encoding: str, data: Any, fn: callable):
    if encoding == "base64":
        data = fn(data)
    elif encoding == "csv":
        raise Exception("csv not supported")
    else:
        data = str(data)
    return data


def do_zlib_gzip_fn(compression: str, data: Any, fn_gzip: callable, fn_zlib: callable):
    if compression == "zlib":
        data = fn_zlib(data)
    elif compression == "gzip":
        data = fn_gzip(data)
    return data


def main():
    args = sys.argv[1:]
    print(f"checking {len(args)} files")
    for arg in args:
        if not arg.endswith(".tmx"):
            print(f"file is not a tmx: {arg}")
            continue

        file = arg

        # for testing uncomment these 2 lines
        # file = f"{arg}.altered.tmx"
        # shutil.copy(arg, file)
        remove_duplicate_usages(file)


if __name__ == "__main__":
    main()
