import re

data = '''<!-- stack box -->
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="0" id="u43498" role="tabpanel" aria-labelledby="u43494" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="0" data-src="images/11%20industrial_image_gea%20westfalia%20separator954x636.jpg?crc=3994756780" src="images/11%20industrial_image_gea%20westfalia%20separator954x636.jpg?crc=3994756780" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u43498_img" data-widget-id="slideshowu43486" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="1" id="u43797" role="tabpanel" aria-labelledby="u43803" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="1" data-src="images/12%20industrial_image_gea%20westfalia%20separator954x636.jpg?crc=123454590" src="images/12%20industrial_image_gea%20westfalia%20separator954x636.jpg?crc=123454590" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u43797_img" data-widget-id="slideshowu43486" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="2" id="u43817" role="tabpanel" aria-labelledby="u43823" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="2" data-src="images/13%20industrial_image_gea%20westfalia%20separator954x636.jpg?crc=3923990939" src="images/13%20industrial_image_gea%20westfalia%20separator954x636.jpg?crc=3923990939" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u43817_img" data-widget-id="slideshowu43486" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="3" id="u43837" role="tabpanel" aria-labelledby="u43843" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="3" data-src="images/14%20industrial_image_gea%20westfalia%20separator954x636.jpg?crc=3829948049" src="images/14%20industrial_image_gea%20westfalia%20separator954x636.jpg?crc=3829948049" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u43837_img" data-widget-id="slideshowu43486" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel wp-panel-active" data-col-pos="4" id="u43857" role="tabpanel" aria-labelledby="u43863" style="height: 621px;"><!-- image -->
  <img class="block" data-col-pos="4" data-src="images/15%20industrial_image_gea%20westfalia%20separator954x6362.jpg?crc=4016276622" src="images/15%20industrial_image_gea%20westfalia%20separator954x6362.jpg?crc=4016276622" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u43857_img" data-widget-id="slideshowu43486" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="5" id="u43877" role="tabpanel" aria-labelledby="u43883" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="5" data-src="images/21%20industrial_image-air%20liquide954x636.jpg?crc=390920565" src="images/21%20industrial_image-air%20liquide954x636.jpg?crc=390920565" alt="" data-heightwidthratio="0.6663168940188877" data-image-width="953" data-image-height="635" id="u43877_img" data-widget-id="slideshowu43486" style="height: 620.341px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="6" id="u43897" role="tabpanel" aria-labelledby="u43903" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="6" data-src="images/22%20industrial_image-air%20liquide954x636.jpg?crc=148614907" src="images/22%20industrial_image-air%20liquide954x636.jpg?crc=148614907" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u43897_img" data-widget-id="slideshowu43486" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="7" id="u43917" role="tabpanel" aria-labelledby="u43923" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="7" data-src="images/23%20industrial_image-air%20liquide954x636.jpg?crc=3782397585" src="images/23%20industrial_image-air%20liquide954x636.jpg?crc=3782397585" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u43917_img" data-widget-id="slideshowu43486" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="8" id="u43937" role="tabpanel" aria-labelledby="u43943" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="8" data-src="images/24%20industrial_image-air%20liquide954x636.jpg?crc=4013957927" src="images/24%20industrial_image-air%20liquide954x636.jpg?crc=4013957927" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u43937_img" data-widget-id="slideshowu43486" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="9" id="u43957" role="tabpanel" aria-labelledby="u43963" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="9" data-src="images/31%20industrial_ac_transit_hydrogen_station954x636.jpg?crc=499682400" src="images/31%20industrial_ac_transit_hydrogen_station954x636.jpg?crc=499682400" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u43957_img" data-widget-id="slideshowu43486" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="10" id="u43977" role="tabpanel" aria-labelledby="u43983" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="10" data-src="images/32%20industrial_ac_transit_hydrogen_station954x634.jpg?crc=447575356" src="images/32%20industrial_ac_transit_hydrogen_station954x634.jpg?crc=447575356" alt="" data-heightwidthratio="0.6652675760755509" data-image-width="953" data-image-height="634" id="u43977_img" data-widget-id="slideshowu43486" style="height: 619.364px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="11" id="u43997" role="tabpanel" aria-labelledby="u44003" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="11" data-src="images/33%20industrial_ac_transit_hydrogen_station954x636.jpg?crc=4129124871" src="images/33%20industrial_ac_transit_hydrogen_station954x636.jpg?crc=4129124871" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u43997_img" data-widget-id="slideshowu43486" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="12" id="u44017" role="tabpanel" aria-labelledby="u44023" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="12" data-src="images/34%20industrial_ac_transit_hydrogen_station954x636.jpg?crc=248846346" src="images/34%20industrial_ac_transit_hydrogen_station954x636.jpg?crc=248846346" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u44017_img" data-widget-id="slideshowu43486" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="13" id="u44037" role="tabpanel" aria-labelledby="u44043" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="13" data-src="images/35%20industrial_ac_transit_hydrogen_station954x636.jpg?crc=97665149" src="images/35%20industrial_ac_transit_hydrogen_station954x636.jpg?crc=97665149" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u44037_img" data-widget-id="slideshowu43486" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="14" id="u44057" role="tabpanel" aria-labelledby="u44063" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="14" data-src="images/36%20industrial_ac_transit_hydrogen_station954x636.jpg?crc=406850465" src="images/36%20industrial_ac_transit_hydrogen_station954x636.jpg?crc=406850465" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u44057_img" data-widget-id="slideshowu43486" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="15" id="u44077" role="tabpanel" aria-labelledby="u44083" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="15" data-src="images/37%20industrial_ac_transit_hydrogen_station954x636.jpg?crc=3860094510" src="images/37%20industrial_ac_transit_hydrogen_station954x636.jpg?crc=3860094510" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u44077_img" data-widget-id="slideshowu43486" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="16" id="u44097" role="tabpanel" aria-labelledby="u44103" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="16" data-src="images/41%20industrial_bayer_pharmaceutical_sterile_filling%20facility954x636.jpg?crc=3990765060" src="images/41%20industrial_bayer_pharmaceutical_sterile_filling%20facility954x636.jpg?crc=3990765060" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u44097_img" data-widget-id="slideshowu43486" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="17" id="u44117" role="tabpanel" aria-labelledby="u44123" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="17" data-src="images/42%20industrial_bayer_pharmaceutical_sterile_filling%20facility954x636.jpg?crc=3863130086" src="images/42%20industrial_bayer_pharmaceutical_sterile_filling%20facility954x636.jpg?crc=3863130086" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u44117_img" data-widget-id="slideshowu43486" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="18" id="u44137" role="tabpanel" aria-labelledby="u44143" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="18" data-src="images/51%20ctp_aviation955x636.jpg?crc=261958158" src="images/51%20ctp_aviation955x636.jpg?crc=261958158" alt="" data-heightwidthratio="0.6666666666666666" data-image-width="954" data-image-height="636" id="u44137_img" data-widget-id="slideshowu43486" style="height: 621.333px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="19" id="u44157" role="tabpanel" aria-labelledby="u44163" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="19" data-src="images/52%20ctp_aviation954x636.jpg?crc=201727631" src="images/52%20ctp_aviation954x636.jpg?crc=201727631" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u44157_img" data-widget-id="slideshowu43486" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="20" id="u44177" role="tabpanel" aria-labelledby="u44183" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="20" data-src="images/53%20ctp_aviation954x622.jpg?crc=4178679460" src="images/53%20ctp_aviation954x622.jpg?crc=4178679460" alt="" data-heightwidthratio="0.6516264428121721" data-image-width="953" data-image-height="621" id="u44177_img" data-widget-id="slideshowu43486" style="height: 606.664px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="21" id="u44197" role="tabpanel" aria-labelledby="u44203" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="21" data-src="images/62%20industrial_nanogram_corporation954x636.jpg?crc=444068194" src="images/62%20industrial_nanogram_corporation954x636.jpg?crc=444068194" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u44197_img" data-widget-id="slideshowu43486" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="22" id="u44217" role="tabpanel" aria-labelledby="u44223" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="22" data-src="images/63%20industrial_nanogram_corporation954x636.jpg?crc=3836633125" src="images/63%20industrial_nanogram_corporation954x636.jpg?crc=3836633125" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u44217_img" data-widget-id="slideshowu43486" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="23" id="u44237" role="tabpanel" aria-labelledby="u44243" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="23" data-src="images/64%20industrial_nanogram_corporation954x636.jpg?crc=257618390" src="images/64%20industrial_nanogram_corporation954x636.jpg?crc=257618390" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u44237_img" data-widget-id="slideshowu43486" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="24" id="u44257" role="tabpanel" aria-labelledby="u44263" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="24" data-src="images/65%20industrial_nanogram_corporation954x636.jpg?crc=4231038145" src="images/65%20industrial_nanogram_corporation954x636.jpg?crc=4231038145" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u44257_img" data-widget-id="slideshowu43486" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="25" id="u90678" role="tabpanel" aria-labelledby="u90684" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="25" data-src="images/71%20industrial%20photography%20_%20tencate%20advanced%20composites954x636.jpg?crc=343161744" src="images/71%20industrial%20photography%20_%20tencate%20advanced%20composites954x636.jpg?crc=343161744" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u90678_img" data-widget-id="slideshowu43486" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="26" id="u90713" role="tabpanel" aria-labelledby="u90719" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="26" data-src="images/72%20industrial%20photography%20_%20tencate%20advanced%20composites954x636.jpg?crc=3968730117" src="images/72%20industrial%20photography%20_%20tencate%20advanced%20composites954x636.jpg?crc=3968730117" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u90713_img" data-widget-id="slideshowu43486" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="27" id="u90733" role="tabpanel" aria-labelledby="u90739" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="27" data-src="images/73%20industrial%20photography%20_%20tencate%20advanced%20composites954x636.jpg?crc=3785489769" src="images/73%20industrial%20photography%20_%20tencate%20advanced%20composites954x636.jpg?crc=3785489769" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u90733_img" data-widget-id="slideshowu43486" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="28" id="u90790" role="tabpanel" aria-labelledby="u90796" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="28" data-src="images/74%20industrial%20photography%20_%20tencate%20advanced%20composites954x636.jpg?crc=4054165947" src="images/74%20industrial%20photography%20_%20tencate%20advanced%20composites954x636.jpg?crc=4054165947" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u90790_img" data-widget-id="slideshowu43486" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="29" id="u90810" role="tabpanel" aria-labelledby="u90816" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="29" data-src="images/75%20industrial%20photography%20_%20tencate%20advanced%20composites954x636.jpg?crc=3975209807" src="images/75%20industrial%20photography%20_%20tencate%20advanced%20composites954x636.jpg?crc=3975209807" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u90810_img" data-widget-id="slideshowu43486" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="30" id="u90850" role="tabpanel" aria-labelledby="u90856" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="30" data-src="images/77%20industrial%20photography%20_%20tencate%20advanced%20composites954x636.jpg?crc=6558039" src="images/77%20industrial%20photography%20_%20tencate%20advanced%20composites954x636.jpg?crc=6558039" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u90850_img" data-widget-id="slideshowu43486" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="31" id="u90870" role="tabpanel" aria-labelledby="u90876" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="31" data-src="images/78%20industrial%20photography%20_%20tencate%20advanced%20composites954x636.jpg?crc=486288624" src="images/78%20industrial%20photography%20_%20tencate%20advanced%20composites954x636.jpg?crc=486288624" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u90870_img" data-widget-id="slideshowu43486" style="height: 621.318px;">
</div>'''

to_remove = [
  '\<div.*',
  '\<\/div>',
  'class="block"',
  'data-col-pos="0"',
  'data-src=".+?(?=")"',
  'data-image-height=".+?(?=")"',
  'data-heightwidthratio=".+?(?=")"',
  'data-image-width=".+?(?=")"',
  'style=".+?(?=")"',
  'data-widget-id=".+?(?=")"',
  '\?.+?(?=")',
  'data-col-pos=".+?(?=")"'
]

removed = data
for item in to_remove:
  removed = re.sub(item, '', removed)
cleaned = [line for line in removed.split('\n') if line.strip() != '']
print('\n'.join(cleaned))

# result:

<img    src="images/11%20industrial_image_gea%20westfalia%20separator954x636.jpg" alt=""    id="u43498_img"  >
<img    src="images/12%20industrial_image_gea%20westfalia%20separator954x636.jpg" alt=""    id="u43797_img"  >
<img    src="images/13%20industrial_image_gea%20westfalia%20separator954x636.jpg" alt=""    id="u43817_img"  >
<img    src="images/14%20industrial_image_gea%20westfalia%20separator954x636.jpg" alt=""    id="u43837_img"  >
<img    src="images/15%20industrial_image_gea%20westfalia%20separator954x6362.jpg" alt=""    id="u43857_img"  >
<img    src="images/21%20industrial_image-air%20liquide954x636.jpg" alt=""    id="u43877_img"  >
<img    src="images/22%20industrial_image-air%20liquide954x636.jpg" alt=""    id="u43897_img"  >
<img    src="images/23%20industrial_image-air%20liquide954x636.jpg" alt=""    id="u43917_img"  >
<img    src="images/24%20industrial_image-air%20liquide954x636.jpg" alt=""    id="u43937_img"  >
<img    src="images/31%20industrial_ac_transit_hydrogen_station954x636.jpg" alt=""    id="u43957_img"  >
<img    src="images/32%20industrial_ac_transit_hydrogen_station954x634.jpg" alt=""    id="u43977_img"  >
<img    src="images/33%20industrial_ac_transit_hydrogen_station954x636.jpg" alt=""    id="u43997_img"  >
<img    src="images/34%20industrial_ac_transit_hydrogen_station954x636.jpg" alt=""    id="u44017_img"  >
<img    src="images/35%20industrial_ac_transit_hydrogen_station954x636.jpg" alt=""    id="u44037_img"  >
<img    src="images/36%20industrial_ac_transit_hydrogen_station954x636.jpg" alt=""    id="u44057_img"  >
<img    src="images/37%20industrial_ac_transit_hydrogen_station954x636.jpg" alt=""    id="u44077_img"  >
<img    src="images/41%20industrial_bayer_pharmaceutical_sterile_filling%20facility954x636.jpg" alt=""    id="u44097_img"  >
<img    src="images/42%20industrial_bayer_pharmaceutical_sterile_filling%20facility954x636.jpg" alt=""    id="u44117_img"  >
<img    src="images/51%20ctp_aviation955x636.jpg" alt=""    id="u44137_img"  >
<img    src="images/52%20ctp_aviation954x636.jpg" alt=""    id="u44157_img"  >
<img    src="images/53%20ctp_aviation954x622.jpg" alt=""    id="u44177_img"  >
<img    src="images/62%20industrial_nanogram_corporation954x636.jpg" alt=""    id="u44197_img"  >
<img    src="images/63%20industrial_nanogram_corporation954x636.jpg" alt=""    id="u44217_img"  >
<img    src="images/64%20industrial_nanogram_corporation954x636.jpg" alt=""    id="u44237_img"  >
<img    src="images/65%20industrial_nanogram_corporation954x636.jpg" alt=""    id="u44257_img"  >
<img    src="images/71%20industrial%20photography%20_%20tencate%20advanced%20composites954x636.jpg" alt=""    id="u90678_img"  >
<img    src="images/72%20industrial%20photography%20_%20tencate%20advanced%20composites954x636.jpg" alt=""    id="u90713_img"  >
<img    src="images/73%20industrial%20photography%20_%20tencate%20advanced%20composites954x636.jpg" alt=""    id="u90733_img"  >
<img    src="images/74%20industrial%20photography%20_%20tencate%20advanced%20composites954x636.jpg" alt=""    id="u90790_img"  >
<img    src="images/75%20industrial%20photography%20_%20tencate%20advanced%20composites954x636.jpg" alt=""    id="u90810_img"  >
<img    src="images/77%20industrial%20photography%20_%20tencate%20advanced%20composites954x636.jpg" alt=""    id="u90850_img"  >
<img    src="images/78%20industrial%20photography%20_%20tencate%20advanced%20composites954x636.jpg" alt=""    id="u90870_img"  >