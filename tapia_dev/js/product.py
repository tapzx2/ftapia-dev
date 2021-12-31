import re

data = '''<!-- stack box -->
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="0" id="u718920" role="tabpanel" aria-labelledby="u718942" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="0" data-src="images/11%20product%20photographer%20san%20francisco%20_cyan955x636.jpg?crc=3895502856" src="images/11%20product%20photographer%20san%20francisco%20_cyan955x636.jpg?crc=3895502856" alt="San Francisco Product Photographer&nbsp; " title="Product Photographer San Francisco Bay Area " data-heightwidthratio="0.6666666666666666" data-image-width="954" data-image-height="636" id="u718920_img" data-widget-id="slideshowu46659" style="height: 621.333px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="1" id="u46916" role="tabpanel" aria-labelledby="u46922" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="1" data-src="images/12%20product_photography%20san%20francisco%20bay%20area_parker%20hannifin%20%e2%80%93%20veriflo%20division954x636.jpg?crc=350117006" src="images/12%20product_photography%20san%20francisco%20bay%20area_parker%20hannifin%20%e2%80%93%20veriflo%20division954x636.jpg?crc=350117006" alt="Industrial product photographer San Francisco Bay Area " title="Industrial product photographer San Francisco Bay Area " data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u46916_img" data-widget-id="slideshowu46659" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="2" id="u46956" role="tabpanel" aria-labelledby="u46962" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="2" data-src="images/14%20product_photography-arco-associates-inc-crop-u469563.jpg?crc=405967392" src="images/14%20product_photography-arco-associates-inc-crop-u469563.jpg?crc=405967392" alt="San Francisco Industrial product photography " title="&nbsp;Industrial product photography San Francisco" data-heightwidthratio="0.6457023060796646" data-image-width="954" data-image-height="616" id="u46956_img" data-widget-id="slideshowu46659" style="height: 601.795px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel wp-panel-active" data-col-pos="3" id="u46976" role="tabpanel" aria-labelledby="u46982" style="height: 621px;"><!-- image -->
  <img class="block" data-col-pos="3" data-src="images/15%20product_photography-arco-associates-inc954x636.jpg?crc=62776777" src="images/15%20product_photography-arco-associates-inc954x636.jpg?crc=62776777" alt="San Francisco Industrial product photography images _ ARCO-Associates-Inc" title="San Francisco Industrial product photography images _ ARCO-Associates-Inc" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u46976_img" data-widget-id="slideshowu46659" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="4" id="u46996" role="tabpanel" aria-labelledby="u47002" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="4" data-src="images/16%20product_photography-xei%20scientific%2c%20inc954x636.jpg?crc=4237637934" src="images/16%20product_photography-xei%20scientific%2c%20inc954x636.jpg?crc=4237637934" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u46996_img" data-widget-id="slideshowu46659" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="5" id="u47016" role="tabpanel" aria-labelledby="u47022" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="5" data-src="images/17%20product_photography-xei%20scientific%2c%20inc954x636.jpg?crc=4088038020" src="images/17%20product_photography-xei%20scientific%2c%20inc954x636.jpg?crc=4088038020" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u47016_img" data-widget-id="slideshowu46659" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="6" id="u47036" role="tabpanel" aria-labelledby="u47042" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="6" data-src="images/18%20product_photography_mchale%20-%20koepke%20communications954x636.jpg?crc=3794637167" src="images/18%20product_photography_mchale%20-%20koepke%20communications954x636.jpg?crc=3794637167" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u47036_img" data-widget-id="slideshowu46659" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="7" id="u47056" role="tabpanel" aria-labelledby="u47062" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="7" data-src="images/19%20product_photography-santur%20corporation%20954x636.jpg?crc=457753394" src="images/19%20product_photography-santur%20corporation%20954x636.jpg?crc=457753394" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u47056_img" data-widget-id="slideshowu46659" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="8" id="u47076" role="tabpanel" aria-labelledby="u47082" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="8" data-src="images/21%20product_image_bio-rad_laboratories954x636.jpg?crc=4185188112" src="images/21%20product_image_bio-rad_laboratories954x636.jpg?crc=4185188112" alt="Clinical diagnostics product image in San Francisco Bay Area _ Bio-Rad_Laboratories" title="Clinical diagnostics product image in San Francisco Bay Area _ Bio-Rad_Laboratories" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u47076_img" data-widget-id="slideshowu46659" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="9" id="u47096" role="tabpanel" aria-labelledby="u47102" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="9" data-src="images/22%20product_image_bio-rad_laboratories954x636.jpg?crc=31769202" src="images/22%20product_image_bio-rad_laboratories954x636.jpg?crc=31769202" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u47096_img" data-widget-id="slideshowu46659" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="10" id="u47116" role="tabpanel" aria-labelledby="u47122" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="10" data-src="images/31%20product_jewel-anna%20beck-design954x636.jpg?crc=225342681" src="images/31%20product_jewel-anna%20beck-design954x636.jpg?crc=225342681" alt="&nbsp;Jewel product photographer San Francisco" title="&nbsp;Jewel product photographer San Francisco" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u47116_img" data-widget-id="slideshowu46659" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="11" id="u47136" role="tabpanel" aria-labelledby="u47142" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="11" data-src="images/32%20product_jewel-anna%20beck-designjpg954x636.jpg?crc=3810596057" src="images/32%20product_jewel-anna%20beck-designjpg954x636.jpg?crc=3810596057" alt="&nbsp;Jewel product photographer San Francisco" title="Jewel product photographer San Francisco" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u47136_img" data-widget-id="slideshowu46659" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="12" id="u47156" role="tabpanel" aria-labelledby="u47162" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="12" data-src="images/33%20product_jewelry_chris_nikolas_fine_jewelry954x636.jpg?crc=3909832643" src="images/33%20product_jewelry_chris_nikolas_fine_jewelry954x636.jpg?crc=3909832643" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u47156_img" data-widget-id="slideshowu46659" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="13" id="u47176" role="tabpanel" aria-labelledby="u47182" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="13" data-src="images/41%20product_image_go-smile954x636.jpg?crc=34710616" src="images/41%20product_image_go-smile954x636.jpg?crc=34710616" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u47176_img" data-widget-id="slideshowu46659" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="14" id="u47196" role="tabpanel" aria-labelledby="u47202" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="14" data-src="images/42%20product_image_go-smile954x636.jpg?crc=488764378" src="images/42%20product_image_go-smile954x636.jpg?crc=488764378" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u47196_img" data-widget-id="slideshowu46659" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="15" id="u47216" role="tabpanel" aria-labelledby="u47222" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="15" data-src="images/43%20product_ac_label954x636.jpg?crc=435745676" src="images/43%20product_ac_label954x636.jpg?crc=435745676" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u47216_img" data-widget-id="slideshowu46659" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="16" id="u47236" role="tabpanel" aria-labelledby="u47242" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="16" data-src="images/44%20product-glass_hensley%20organic954x636.jpg?crc=3988442962" src="images/44%20product-glass_hensley%20organic954x636.jpg?crc=3988442962" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u47236_img" data-widget-id="slideshowu46659" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="17" id="u47256" role="tabpanel" aria-labelledby="u47262" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="17" data-src="images/51%20product_columbus_distributing954x636.jpg?crc=237431922" src="images/51%20product_columbus_distributing954x636.jpg?crc=237431922" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u47256_img" data-widget-id="slideshowu46659" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="18" id="u47276" role="tabpanel" aria-labelledby="u47282" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="18" data-src="images/52%20product_columbus_distributing954x636.jpg?crc=27922949" src="images/52%20product_columbus_distributing954x636.jpg?crc=27922949" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u47276_img" data-widget-id="slideshowu46659" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="19" id="u719064" role="tabpanel" aria-labelledby="u719086" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="19" data-src="images/53product_car_ferrari%20maserati%20of%20silicon%20valley954x636.jpg?crc=22499744" src="images/53product_car_ferrari%20maserati%20of%20silicon%20valley954x636.jpg?crc=22499744" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u719064_img" data-widget-id="slideshowu46659" style="height: 621.318px;">
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

<img    src="images/11%20product%20photographer%20san%20francisco%20_cyan955x636.jpg" alt="San Francisco Product Photographer&nbsp; " title="Product Photographer San Francisco Bay Area "    id="u718920_img"  >
<img    src="images/12%20product_photography%20san%20francisco%20bay%20area_parker%20hannifin%20%e2%80%93%20veriflo%20division954x636.jpg" alt="Industrial product photographer San Francisco Bay Area " title="Industrial product photographer San Francisco Bay Area "    id="u46916_img"  >
<img    src="images/14%20product_photography-arco-associates-inc-crop-u469563.jpg" alt="San Francisco Industrial product photography " title="&nbsp;Industrial product photography San Francisco"    id="u46956_img"  >
<img    src="images/15%20product_photography-arco-associates-inc954x636.jpg" alt="San Francisco Industrial product photography images _ ARCO-Associates-Inc" title="San Francisco Industrial product photography images _ ARCO-Associates-Inc"    id="u46976_img"  >
<img    src="images/16%20product_photography-xei%20scientific%2c%20inc954x636.jpg" alt=""    id="u46996_img"  >
<img    src="images/17%20product_photography-xei%20scientific%2c%20inc954x636.jpg" alt=""    id="u47016_img"  >
<img    src="images/18%20product_photography_mchale%20-%20koepke%20communications954x636.jpg" alt=""    id="u47036_img"  >
<img    src="images/19%20product_photography-santur%20corporation%20954x636.jpg" alt=""    id="u47056_img"  >
<img    src="images/21%20product_image_bio-rad_laboratories954x636.jpg" alt="Clinical diagnostics product image in San Francisco Bay Area _ Bio-Rad_Laboratories" title="Clinical diagnostics product image in San Francisco Bay Area _ Bio-Rad_Laboratories"    id="u47076_img"  >
<img    src="images/22%20product_image_bio-rad_laboratories954x636.jpg" alt=""    id="u47096_img"  >
<img    src="images/31%20product_jewel-anna%20beck-design954x636.jpg" alt="&nbsp;Jewel product photographer San Francisco" title="&nbsp;Jewel product photographer San Francisco"    id="u47116_img"  >
<img    src="images/32%20product_jewel-anna%20beck-designjpg954x636.jpg" alt="&nbsp;Jewel product photographer San Francisco" title="Jewel product photographer San Francisco"    id="u47136_img"  >
<img    src="images/33%20product_jewelry_chris_nikolas_fine_jewelry954x636.jpg" alt=""    id="u47156_img"  >
<img    src="images/41%20product_image_go-smile954x636.jpg" alt=""    id="u47176_img"  >
<img    src="images/42%20product_image_go-smile954x636.jpg" alt=""    id="u47196_img"  >
<img    src="images/43%20product_ac_label954x636.jpg" alt=""    id="u47216_img"  >
<img    src="images/44%20product-glass_hensley%20organic954x636.jpg" alt=""    id="u47236_img"  >
<img    src="images/51%20product_columbus_distributing954x636.jpg" alt=""    id="u47256_img"  >
<img    src="images/52%20product_columbus_distributing954x636.jpg" alt=""    id="u47276_img"  >
<img    src="images/53product_car_ferrari%20maserati%20of%20silicon%20valley954x636.jpg" alt=""    id="u719064_img"  >


## ROUND 2

import re

data = '''<!-- column -->
<div class="SSSlideLink clip_frame colelem" data-col-pos="0" id="u718942" role="tab" tabindex="-1" aria-selected="false" aria-controls="u718920" style="height: 22px;"><!-- image -->
<img class="block" data-col-pos="0" alt="" data-heightwidthratio="0.8620689655172413" data-image-width="29" data-image-height="25" src="images/11%20product%20photographer%20san%20francisco%20_cyan-crop-u7189423.jpg?crc=4581566" id="u718942_img" data-widget-id="slideshowu46659" style="height: 22.4138px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="2" id="u46962" role="tab" tabindex="-1" aria-selected="false" aria-controls="u46956" style="height: 22px;"><!-- image -->
<img class="block" data-col-pos="2" alt="" data-heightwidthratio="0.8620689655172413" data-image-width="29" data-image-height="25" src="images/14%20product_photography-arco-associates-inc-crop-u469623.jpg?crc=139423987" id="u46962_img" data-widget-id="slideshowu46659" style="height: 22.4138px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="4" id="u47002" role="tab" tabindex="-1" aria-selected="false" aria-controls="u46996" style="height: 22px;"><!-- image -->
<img class="block" data-col-pos="4" alt="" data-heightwidthratio="0.8620689655172413" data-image-width="29" data-image-height="25" src="images/16%20product_photography-xei%20scientific%2c%20inc-crop-u470023.jpg?crc=272942190" id="u47002_img" data-widget-id="slideshowu46659" style="height: 22.4138px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="6" id="u47042" role="tab" tabindex="-1" aria-selected="false" aria-controls="u47036" style="height: 22px;"><!-- image -->
<img class="block" data-col-pos="6" alt="" data-heightwidthratio="0.8620689655172413" data-image-width="29" data-image-height="25" src="images/18%20product_photography_mchale%20-%20koepke%20communications-crop-u470423.jpg?crc=158034231" id="u47042_img" data-widget-id="slideshowu46659" style="height: 22.4138px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="8" id="u47082" role="tab" tabindex="-1" aria-selected="false" aria-controls="u47076" style="height: 22px;"><!-- image -->
<img class="block" data-col-pos="8" alt="" data-heightwidthratio="0.8620689655172413" data-image-width="29" data-image-height="25" src="images/21%20product_image_bio-rad_laboratories-crop-u470823.jpg?crc=4056554093" id="u47082_img" data-widget-id="slideshowu46659" style="height: 22.4138px;">
</div>
<div class="SSSlideLink clip_frame colelem wp-tab-active SSSlideLinkSelected" data-col-pos="10" id="u47122" role="tab" tabindex="0" aria-selected="true" aria-controls="u47116" style="height: 22px;"><!-- image -->
<img class="block" data-col-pos="10" alt="" data-heightwidthratio="0.8620689655172413" data-image-width="29" data-image-height="25" src="images/31%20product_jewel-anna%20beck-design-crop-u471223.jpg?crc=4041217942" id="u47122_img" data-widget-id="slideshowu46659" style="height: 22.4138px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="12" id="u47162" role="tab" tabindex="-1" aria-selected="false" aria-controls="u47156" style="height: 22px;"><!-- image -->
<img class="block" data-col-pos="12" alt="" data-heightwidthratio="0.8620689655172413" data-image-width="29" data-image-height="25" src="images/33%20product_jewelry_chris_nikolas_fine_jewelry-crop-u471623.jpg?crc=407846424" id="u47162_img" data-widget-id="slideshowu46659" style="height: 22.4138px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="14" id="u47202" role="tab" tabindex="-1" aria-selected="false" aria-controls="u47196" style="height: 22px;"><!-- image -->
<img class="block" data-col-pos="14" alt="" data-heightwidthratio="0.8620689655172413" data-image-width="29" data-image-height="25" src="images/42%20product_image_go-smile-crop-u472023.jpg?crc=365004886" id="u47202_img" data-widget-id="slideshowu46659" style="height: 22.4138px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="16" id="u47242" role="tab" tabindex="-1" aria-selected="false" aria-controls="u47236" style="height: 22px;"><!-- image -->
<img class="block" data-col-pos="16" alt="" data-heightwidthratio="0.8620689655172413" data-image-width="29" data-image-height="25" src="images/44%20product-glass_hensley%20organic-crop-u472423.jpg?crc=3828077653" id="u47242_img" data-widget-id="slideshowu46659" style="height: 22.4138px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="18" id="u47282" role="tab" tabindex="-1" aria-selected="false" aria-controls="u47276" style="height: 22px;"><!-- image -->
<img class="block" data-col-pos="18" alt="" data-heightwidthratio="0.8620689655172413" data-image-width="29" data-image-height="25" src="images/52%20product_columbus_distributing-crop-u472823.jpg?crc=4130070025" id="u47282_img" data-widget-id="slideshowu46659" style="height: 22.4138px;">
</div><!-- column -->
<div class="SSSlideLink clip_frame colelem" data-col-pos="1" id="u46922" role="tab" tabindex="-1" aria-selected="false" aria-controls="u46916" style="height: 22px;"><!-- image -->
<img class="block" data-col-pos="1" alt="" data-heightwidthratio="0.8620689655172413" data-image-width="29" data-image-height="25" src="images/12%20product_photography%20san%20francisco%20bay%20area_parker%20hannifin%20%e2%80%93%20veriflo%20division-crop-u469223.jpg?crc=3819326544" id="u46922_img" data-widget-id="slideshowu46659" style="height: 22.4138px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="3" id="u46982" role="tab" tabindex="-1" aria-selected="false" aria-controls="u46976" style="height: 22px;"><!-- image -->
<img class="block" data-col-pos="3" alt="" data-heightwidthratio="0.8620689655172413" data-image-width="29" data-image-height="25" src="images/15%20product_photography-arco-associates-inc-crop-u469823.jpg?crc=411304626" id="u46982_img" data-widget-id="slideshowu46659" style="height: 22.4138px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="5" id="u47022" role="tab" tabindex="-1" aria-selected="false" aria-controls="u47016" style="height: 22px;"><!-- image -->
<img class="block" data-col-pos="5" alt="" data-heightwidthratio="0.8620689655172413" data-image-width="29" data-image-height="25" src="images/17%20product_photography-xei%20scientific%2c%20inc-crop-u470223.jpg?crc=365695019" id="u47022_img" data-widget-id="slideshowu46659" style="height: 22.4138px;">
</div>
<div class="SSSlideLink clip_frame colelem wp-tab-active SSSlideLinkSelected" data-col-pos="7" id="u47062" role="tab" tabindex="0" aria-selected="true" aria-controls="u47056" style="height: 22px;"><!-- image -->
<img class="block" data-col-pos="7" alt="" data-heightwidthratio="0.8620689655172413" data-image-width="29" data-image-height="25" src="images/19%20product_photography-santur%20corporation%20-crop-u470623.jpg?crc=4002850665" id="u47062_img" data-widget-id="slideshowu46659" style="height: 22.4138px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="9" id="u47102" role="tab" tabindex="-1" aria-selected="false" aria-controls="u47096" style="height: 22px;"><!-- image -->
<img class="block" data-col-pos="9" alt="" data-heightwidthratio="0.8620689655172413" data-image-width="29" data-image-height="25" src="images/22%20product_image_bio-rad_laboratories-crop-u471023.jpg?crc=201369102" id="u47102_img" data-widget-id="slideshowu46659" style="height: 22.4138px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="11" id="u47142" role="tab" tabindex="-1" aria-selected="false" aria-controls="u47136" style="height: 22px;"><!-- image -->
<img class="block" data-col-pos="11" alt="" data-heightwidthratio="0.8620689655172413" data-image-width="29" data-image-height="25" src="images/32%20product_jewel-anna%20beck-designjpg-crop-u471423.jpg?crc=4015224569" id="u47142_img" data-widget-id="slideshowu46659" style="height: 22.4138px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="13" id="u47182" role="tab" tabindex="-1" aria-selected="false" aria-controls="u47176" style="height: 22px;"><!-- image -->
<img class="block" data-col-pos="13" alt="" data-heightwidthratio="0.8620689655172413" data-image-width="29" data-image-height="25" src="images/41%20product_image_go-smile-crop-u471823.jpg?crc=3964339345" id="u47182_img" data-widget-id="slideshowu46659" style="height: 22.4138px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="15" id="u47222" role="tab" tabindex="-1" aria-selected="false" aria-controls="u47216" style="height: 22px;"><!-- image -->
<img class="block" data-col-pos="15" alt="" data-heightwidthratio="0.8620689655172413" data-image-width="29" data-image-height="25" src="images/43%20product_ac_label-crop-u472223.jpg?crc=401143211" id="u47222_img" data-widget-id="slideshowu46659" style="height: 22.4138px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="17" id="u47262" role="tab" tabindex="-1" aria-selected="false" aria-controls="u47256" style="height: 22px;"><!-- image -->
<img class="block" data-col-pos="17" alt="" data-heightwidthratio="0.8620689655172413" data-image-width="29" data-image-height="25" src="images/51%20product_columbus_distributing-crop-u472623.jpg?crc=3963922733" id="u47262_img" data-widget-id="slideshowu46659" style="height: 22.4138px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="19" id="u719086" role="tab" tabindex="-1" aria-selected="false" aria-controls="u719064" style="height: 22px;"><!-- image -->
<img class="block" data-col-pos="19" alt="" data-heightwidthratio="0.8620689655172413" data-image-width="29" data-image-height="25" src="images/53product_car_ferrari%20maserati%20of%20silicon%20valley-crop-u7190863.jpg?crc=75097052" id="u719086_img" data-widget-id="slideshowu46659" style="height: 22.4138px;">
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
cleaned_string = '\n'.join(cleaned)
cleaned_list = cleaned_string.split('\n')
list_strip = []
for item in cleaned_list:
  list_strip.append(item.strip())
super_clean_string = '\n'.join(list_strip)
#print(super_clean_string)
two_cols = super_clean_string.split('<!-- column -->\n')
empty = ''
while empty in two_cols: two_cols.remove(empty)    
first_col = two_cols[0].split('\n')
second_col = two_cols[1].split('\n')
zipped = zip(first_col, second_col)
almost_final = []
for item in zipped:
  for photo in item:
    add_class = re.sub('  ', ' class="mini-image"', photo, 1)
    almost_final.append(add_class)
almost_final_string = '\n'.join(almost_final)
print(almost_final_string)