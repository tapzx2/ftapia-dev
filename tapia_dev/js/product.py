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