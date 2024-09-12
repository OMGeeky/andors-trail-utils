from unittest import TestCase

from remove_duplicate_tileset_usages import remove_tileset_with_regex

sample_input = """
<?xml version="1.0" encoding="UTF-8"?>
<map version="1.10" tiledversion="1.11.0" orientation="orthogonal" renderorder="right-down" width="30" height="14" tilewidth="32" tileheight="32" infinite="0" nextlayerid="9" nextobjectid="2">
 <tileset firstgid="1" name="map_bed_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_bed_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="129" name="map_border_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_border_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="257" name="map_bridge_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_bridge_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="385" name="map_bridge_2" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_bridge_2.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="513" name="map_broken_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_broken_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="641" name="map_cavewall_1" tilewidth="32" tileheight="32" tilecount="108" columns="18">
  <image source="../drawable/map_cavewall_1.png" width="576" height="192"/>
 </tileset>
 <tileset firstgid="749" name="map_cavewall_2" tilewidth="32" tileheight="32" tilecount="108" columns="18">
  <image source="../drawable/map_cavewall_2.png" width="576" height="192"/>
 </tileset>
 <tileset firstgid="857" name="map_cavewall_3" tilewidth="32" tileheight="32" tilecount="108" columns="18">
  <image source="../drawable/map_cavewall_3.png" width="576" height="192"/>
 </tileset>
 <tileset firstgid="965" name="map_cavewall_4" tilewidth="32" tileheight="32" tilecount="108" columns="18">
  <image source="../drawable/map_cavewall_4.png" width="576" height="192"/>
 </tileset>
 <tileset firstgid="1073" name="map_chair_table_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_chair_table_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="1201" name="map_chair_table_2" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_chair_table_2.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="1329" name="map_crate_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_crate_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="1457" name="map_cupboard_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_cupboard_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="1585" name="map_curtain_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_curtain_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="1713" name="map_entrance_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_entrance_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="1841" name="map_entrance_2" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_entrance_2.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="1969" name="map_fence_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_fence_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="2097" name="map_fence_2" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_fence_2.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="2225" name="map_fence_3" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_fence_3.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="2353" name="map_fence_4" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_fence_4.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="2481" name="map_ground_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_ground_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="2609" name="map_ground_2" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_ground_2.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="2737" name="map_ground_3" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_ground_3.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="2865" name="map_ground_4" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_ground_4.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="2993" name="map_ground_5" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_ground_5.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="3121" name="map_ground_6" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_ground_6.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="3249" name="map_ground_7" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_ground_7.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="3377" name="map_ground_8" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_ground_8.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="3505" name="map_house_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_house_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="3633" name="map_house_2" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_house_2.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="3761" name="map_indoor_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_indoor_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="3889" name="map_indoor_2" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_indoor_2.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="4017" name="map_kitchen_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_kitchen_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="4145" name="map_outdoor_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_outdoor_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="4273" name="map_pillar_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_pillar_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="4401" name="map_pillar_2" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_pillar_2.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="4529" name="map_plant_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_plant_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="4657" name="map_plant_2" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_plant_2.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="4785" name="map_rock_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_rock_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="4913" name="map_rock_2" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_rock_2.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="5041" name="map_roof_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_roof_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="5169" name="map_roof_2" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_roof_2.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="5297" name="map_roof_3" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_roof_3.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="5425" name="map_shop_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_shop_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="5553" name="map_sign_ladder_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_sign_ladder_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="5681" name="map_table_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_table_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="5809" name="map_trail_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_trail_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="5937" name="map_transition_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_transition_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="6065" name="map_transition_2" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_transition_2.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="6193" name="map_transition_3" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_transition_3.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="6321" name="map_transition_4" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_transition_4.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="6449" name="map_transition_5" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_transition_5.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="6577" name="map_tree_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_tree_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="6705" name="map_tree_2" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_tree_2.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="6833" name="map_wall_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_wall_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="6961" name="map_wall_2" tilewidth="32" tileheight="32" tilecount="120" columns="15">
  <image source="../drawable/map_wall_2.png" width="480" height="256"/>
 </tileset>
 <tileset firstgid="7081" name="map_wall_3" tilewidth="32" tileheight="32" tilecount="120" columns="15">
  <image source="../drawable/map_wall_3.png" width="480" height="256"/>
 </tileset>
 <tileset firstgid="7201" name="map_wall_4" tilewidth="32" tileheight="32" tilecount="120" columns="15">
  <image source="../drawable/map_wall_4.png" width="480" height="256"/>
 </tileset>
 <tileset firstgid="7321" name="map_window_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_window_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="7449" name="map_window_2" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_window_2.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="7577" name="map_trail_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_trail_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="7705" name="map_ground_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_ground_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="7833" name="map_cavewall_1" tilewidth="32" tileheight="32" tilecount="108" columns="18">
  <image source="../drawable/map_cavewall_1.png" width="576" height="192"/>
 </tileset>
 <tileset firstgid="7941" name="map_tree_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_tree_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="8069" name="map_brightport" tilewidth="32" tileheight="32" tilecount="112" columns="16">
  <image source="../drawable/map_brightport.png" width="512" height="224"/>
 </tileset>
 <tileset firstgid="8181" name="map_tree_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_tree_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="8309" name="map_tree_3" tilewidth="32" tileheight="32" tilecount="544" columns="32">
  <image source="../drawable/map_tree_3.png" width="1024" height="544"/>
 </tileset>
 <tileset firstgid="8853" name="map_pillar_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_pillar_1.png" width="512" height="256"/>
 </tileset>
 <layer id="1" name="Ground" width="30" height="14">
  <data encoding="base64" compression="zlib">
   eJzbyMnAsJFGeD8TA8MBIF6HhNdCaVrZCcIXgeZfQrILhPfTwV4QfsKE6u+LUHdQYuZPbgaGX0D8m5s0f+/HYu9PJHNwsWGYk4eBgQuIuXmI8/daJD+jy0sCzZDmwc9GViuFRZyYdEbr+MUV3vS0Fzm86W0vCI/aO2ovLTAoHwMAiyotWg==
  </data>
 </layer>
 <layer id="2" name="Objects" width="30" height="14">
  <data encoding="base64" compression="zlib">eJylVE1LA0EMDd4WVJpZWLAXpf1l6l78OPYn9KRe9acInhcKgvS4tuJNaD3U/+CE3bBv0pltxQfDTF6bSV4ym80J0Y9fG7MLLJfaBUeO6NiFfoglE9Xc2fvEqeAs/n3xYzEVFfB3w3jM84zowq/LLIyPPPo9nhE9+VW2vHBfB/H4Nr97n8NDm8c71GTFoc/M2ILDotknWViTudGOuaAexZh3n2OYtnoHuY8/IDrNu1jYX6zRf1FzWL+XIt5vyUN78mF0rFv71fD1Dr1lth0r9da0NraPCJuX5eQ9SJ8mWcctjH7s7XPRrGUR3jnyPs41/cxdaDPYI5PPtEcvvltBCTlW0Ju/7Aq8+9vn9MZhbJujAHunWlQrG+0MvwsW4Ls2NYjNF3lXqXmzr9YVhzNN8RmZbTaXOXxPfTNLYGeW5VIx+uapnSGp/+r5yvfyerh9943nbiO84hcEGsAg</data>
 </layer>
 <layer id="3" name="Above" width="30" height="14">
  <data encoding="base64" compression="zlib">eJy7I8nAcBeIQeAOlI1Ob0Zi41OHLIcNbEYSr5LCbhYyQLYfHcDkShUYGMoUCNuNrg8EqoFuqJHCr54Y8AbJ/fvw2I/PP7QC6GFEKUAPY1xhTi37yLGbWgBfuqMHwOVffOmW0rSFy2x6+hvdTmS7QemK2PIGH0Av0/DZiSy+Dyk/4dNPiv/w2Y1LzWYs8tjYkcC4jJLCNDsaKBaDRRwZ4NKLrQxFLmNgbFxlMz7zAPGWgcM=</data>
 </layer>
 <layer id="4" name="Walkable" width="30" height="14" visible="0">
  <data encoding="base64" compression="zlib">
   eJzbKMbAsHEUDwgmFmDTQw934RJDZxNjHjFsYvxLrP+pBYgNe+TwoJaduNxBjD/R3USIxmYPPrvR9VLqd1z+ISWcSfUrIbcQm55JAbjijp55mdS8RE8MAAqL1Dg=
  </data>
 </layer>
 <objectgroup id="5" name="Mapevents">
  <object id="1" name="west" type="mapchange" x="0" y="224" width="32" height="128">
   <properties>
    <property name="map" value="brightport4"/>
    <property name="place" value="east"/>
   </properties>
  </object>
 </objectgroup>
 <objectgroup id="6" name="Spawn"/>
 <objectgroup id="7" name="Keys"/>
 <objectgroup id="8" name="Replace"/>
</map>

"""
expected_output = """
<?xml version="1.0" encoding="UTF-8"?>
<map version="1.10" tiledversion="1.11.0" orientation="orthogonal" renderorder="right-down" width="30" height="14" tilewidth="32" tileheight="32" infinite="0" nextlayerid="9" nextobjectid="2">
 <tileset firstgid="1" name="map_bed_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_bed_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="129" name="map_border_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_border_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="257" name="map_bridge_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_bridge_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="385" name="map_bridge_2" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_bridge_2.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="513" name="map_broken_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_broken_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="641" name="map_cavewall_1" tilewidth="32" tileheight="32" tilecount="108" columns="18">
  <image source="../drawable/map_cavewall_1.png" width="576" height="192"/>
 </tileset>
 <tileset firstgid="749" name="map_cavewall_2" tilewidth="32" tileheight="32" tilecount="108" columns="18">
  <image source="../drawable/map_cavewall_2.png" width="576" height="192"/>
 </tileset>
 <tileset firstgid="857" name="map_cavewall_3" tilewidth="32" tileheight="32" tilecount="108" columns="18">
  <image source="../drawable/map_cavewall_3.png" width="576" height="192"/>
 </tileset>
 <tileset firstgid="965" name="map_cavewall_4" tilewidth="32" tileheight="32" tilecount="108" columns="18">
  <image source="../drawable/map_cavewall_4.png" width="576" height="192"/>
 </tileset>
 <tileset firstgid="1073" name="map_chair_table_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_chair_table_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="1201" name="map_chair_table_2" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_chair_table_2.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="1329" name="map_crate_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_crate_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="1457" name="map_cupboard_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_cupboard_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="1585" name="map_curtain_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_curtain_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="1713" name="map_entrance_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_entrance_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="1841" name="map_entrance_2" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_entrance_2.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="1969" name="map_fence_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_fence_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="2097" name="map_fence_2" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_fence_2.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="2225" name="map_fence_3" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_fence_3.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="2353" name="map_fence_4" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_fence_4.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="2481" name="map_ground_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_ground_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="2609" name="map_ground_2" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_ground_2.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="2737" name="map_ground_3" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_ground_3.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="2865" name="map_ground_4" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_ground_4.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="2993" name="map_ground_5" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_ground_5.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="3121" name="map_ground_6" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_ground_6.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="3249" name="map_ground_7" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_ground_7.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="3377" name="map_ground_8" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_ground_8.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="3505" name="map_house_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_house_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="3633" name="map_house_2" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_house_2.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="3761" name="map_indoor_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_indoor_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="3889" name="map_indoor_2" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_indoor_2.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="4017" name="map_kitchen_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_kitchen_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="4145" name="map_outdoor_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_outdoor_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="4273" name="map_pillar_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_pillar_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="4401" name="map_pillar_2" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_pillar_2.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="4529" name="map_plant_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_plant_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="4657" name="map_plant_2" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_plant_2.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="4785" name="map_rock_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_rock_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="4913" name="map_rock_2" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_rock_2.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="5041" name="map_roof_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_roof_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="5169" name="map_roof_2" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_roof_2.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="5297" name="map_roof_3" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_roof_3.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="5425" name="map_shop_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_shop_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="5553" name="map_sign_ladder_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_sign_ladder_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="5681" name="map_table_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_table_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="5809" name="map_trail_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_trail_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="5937" name="map_transition_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_transition_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="6065" name="map_transition_2" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_transition_2.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="6193" name="map_transition_3" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_transition_3.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="6321" name="map_transition_4" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_transition_4.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="6449" name="map_transition_5" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_transition_5.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="6577" name="map_tree_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_tree_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="6705" name="map_tree_2" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_tree_2.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="6833" name="map_wall_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_wall_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="6961" name="map_wall_2" tilewidth="32" tileheight="32" tilecount="120" columns="15">
  <image source="../drawable/map_wall_2.png" width="480" height="256"/>
 </tileset>
 <tileset firstgid="7081" name="map_wall_3" tilewidth="32" tileheight="32" tilecount="120" columns="15">
  <image source="../drawable/map_wall_3.png" width="480" height="256"/>
 </tileset>
 <tileset firstgid="7201" name="map_wall_4" tilewidth="32" tileheight="32" tilecount="120" columns="15">
  <image source="../drawable/map_wall_4.png" width="480" height="256"/>
 </tileset>
 <tileset firstgid="7321" name="map_window_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_window_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="7449" name="map_window_2" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_window_2.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="7577" name="map_trail_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_trail_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="7705" name="map_ground_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_ground_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="7833" name="map_cavewall_1" tilewidth="32" tileheight="32" tilecount="108" columns="18">
  <image source="../drawable/map_cavewall_1.png" width="576" height="192"/>
 </tileset>
 <tileset firstgid="7941" name="map_tree_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_tree_1.png" width="512" height="256"/>
 </tileset>
 <tileset firstgid="8069" name="map_brightport" tilewidth="32" tileheight="32" tilecount="112" columns="16">
  <image source="../drawable/map_brightport.png" width="512" height="224"/>
 </tileset>
  <tileset firstgid="8309" name="map_tree_3" tilewidth="32" tileheight="32" tilecount="544" columns="32">
  <image source="../drawable/map_tree_3.png" width="1024" height="544"/>
 </tileset>
 <tileset firstgid="8853" name="map_pillar_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
  <image source="../drawable/map_pillar_1.png" width="512" height="256"/>
 </tileset>
 <layer id="1" name="Ground" width="30" height="14">
  <data encoding="base64" compression="zlib">
   eJzbyMnAsJFGeD8TA8MBIF6HhNdCaVrZCcIXgeZfQrILhPfTwV4QfsKE6u+LUHdQYuZPbgaGX0D8m5s0f+/HYu9PJHNwsWGYk4eBgQuIuXmI8/daJD+jy0sCzZDmwc9GViuFRZyYdEbr+MUV3vS0Fzm86W0vCI/aO2ovLTAoHwMAiyotWg==
  </data>
 </layer>
 <layer id="2" name="Objects" width="30" height="14">
  <data encoding="base64" compression="zlib">eJylVE1LA0EMDd4WVJpZWLAXpf1l6l78OPYn9KRe9acInhcKgvS4tuJNaD3U/+CE3bBv0pltxQfDTF6bSV4ym80J0Y9fG7MLLJfaBUeO6NiFfoglE9Xc2fvEqeAs/n3xYzEVFfB3w3jM84zowq/LLIyPPPo9nhE9+VW2vHBfB/H4Nr97n8NDm8c71GTFoc/M2ILDotknWViTudGOuaAexZh3n2OYtnoHuY8/IDrNu1jYX6zRf1FzWL+XIt5vyUN78mF0rFv71fD1Dr1lth0r9da0NraPCJuX5eQ9SJ8mWcctjH7s7XPRrGUR3jnyPs41/cxdaDPYI5PPtEcvvltBCTlW0Ju/7Aq8+9vn9MZhbJujAHunWlQrG+0MvwsW4Ls2NYjNF3lXqXmzr9YVhzNN8RmZbTaXOXxPfTNLYGeW5VIx+uapnSGp/+r5yvfyerh9943nbiO84hcEGsAg</data>
 </layer>
 <layer id="3" name="Above" width="30" height="14">
  <data encoding="base64" compression="zlib">eJy7I8nAcBeIQeAOlI1Ob0Zi41OHLIcNbEYSr5LCbhYyQLYfHcDkShUYGMoUCNuNrg8EqoFuqJHCr54Y8AbJ/fvw2I/PP7QC6GFEKUAPY1xhTi37yLGbWgBfuqMHwOVffOmW0rSFy2x6+hvdTmS7QemK2PIGH0Av0/DZiSy+Dyk/4dNPiv/w2Y1LzWYs8tjYkcC4jJLCNDsaKBaDRRwZ4NKLrQxFLmNgbFxlMz7zAPGWgcM=</data>
 </layer>
 <layer id="4" name="Walkable" width="30" height="14" visible="0">
  <data encoding="base64" compression="zlib">
   eJzbKMbAsHEUDwgmFmDTQw934RJDZxNjHjFsYvxLrP+pBYgNe+TwoJaduNxBjD/R3USIxmYPPrvR9VLqd1z+ISWcSfUrIbcQm55JAbjijp55mdS8RE8MAAqL1Dg=
  </data>
 </layer>
 <objectgroup id="5" name="Mapevents">
  <object id="1" name="west" type="mapchange" x="0" y="224" width="32" height="128">
   <properties>
    <property name="map" value="brightport4"/>
    <property name="place" value="east"/>
   </properties>
  </object>
 </objectgroup>
 <objectgroup id="6" name="Spawn"/>
 <objectgroup id="7" name="Keys"/>
 <objectgroup id="8" name="Replace"/>
</map>

"""


class Test(TestCase):

    def test_remove_tileset_with_regex(self):
        """
        should remove this tileset:

        <tileset firstgid="8181" name="map_tree_1" tilewidth="32" tileheight="32" tilecount="128" columns="16">
         <image source="../drawable/map_tree_1.png" width="512" height="256"/>
        </tileset>"""
        response = remove_tileset_with_regex(sample_input, "map_tree_1", 8181)
        self.assertEqual(
            response, expected_output, "removed stuff was not what we expected"
        )
