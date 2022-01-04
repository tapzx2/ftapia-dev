import re

data = '''<!-- stack box -->
<div class="SSSlide clip_frame grpelem wp-panel wp-panel-active" data-col-pos="0" id="u3858" role="tabpanel" aria-labelledby="u3850" style="height: 621px;"><!-- image -->
  <img class="block" data-col-pos="0" data-src="images/11%20architecture_image954x636.jpg?crc=4105000400" src="images/11%20architecture_image954x636.jpg?crc=4105000400" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u3858_img" data-widget-id="slideshowu3846" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel SSSlideLoading" data-col-pos="1" id="u758523" role="tabpanel" aria-labelledby="u758549" style="height: 621px; display: none;"><!-- image -->
  <img class="block ImageInclude" data-col-pos="1" data-src="images/%201%20architectural%20photographer%20san%20francisco954x636.jpg?crc=336748221" src="images/blank.gif?crc=4208392903" alt="" data-heightwidthratio="0.6666666666666666" data-image-width="954" data-image-height="636" id="u758523_img" data-widget-id="slideshowu3846" style="visibility: hidden; height: 621.333px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel SSSlideLoading" data-col-pos="2" id="u758603" role="tabpanel" aria-labelledby="u758624" style="height: 621px; display: none;"><!-- image -->
  <img class="block ImageInclude" data-col-pos="2" data-src="images/%202%20architectural%20photographer%20san%20francisco954x636.jpg?crc=4005793202" src="images/blank.gif?crc=4208392903" alt="" data-heightwidthratio="0.6666666666666666" data-image-width="954" data-image-height="636" id="u758603_img" data-widget-id="slideshowu3846" style="visibility: hidden; height: 621.333px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel SSSlideLoading" data-col-pos="3" id="u758678" role="tabpanel" aria-labelledby="u758699" style="height: 621px; display: none;"><!-- image -->
  <img class="block ImageInclude" data-col-pos="3" data-src="images/%203%20architectural%20photographer%20san%20francisco954x636.jpg?crc=394938140" src="images/blank.gif?crc=4208392903" alt="" data-heightwidthratio="0.6666666666666666" data-image-width="954" data-image-height="636" id="u758678_img" data-widget-id="slideshowu3846" style="visibility: hidden; height: 621.333px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel SSSlideLoading" data-col-pos="4" id="u758753" role="tabpanel" aria-labelledby="u758774" style="height: 621px; display: none;"><!-- image -->
  <img class="block ImageInclude" data-col-pos="4" data-src="images/%204%20architectural%20photographer%20san%20francisco954x636.jpg?crc=3828433910" src="images/blank.gif?crc=4208392903" alt="" data-heightwidthratio="0.6666666666666666" data-image-width="954" data-image-height="636" id="u758753_img" data-widget-id="slideshowu3846" style="visibility: hidden; height: 621.333px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel SSSlideLoading" data-col-pos="5" id="u758828" role="tabpanel" aria-labelledby="u758849" style="height: 621px; display: none;"><!-- image -->
  <img class="block ImageInclude" data-col-pos="5" data-src="images/%205%20architectural%20photographer%20san%20francisco954x636.jpg?crc=226798766" src="images/blank.gif?crc=4208392903" alt="" data-heightwidthratio="0.6666666666666666" data-image-width="954" data-image-height="636" id="u758828_img" data-widget-id="slideshowu3846" style="visibility: hidden; height: 621.333px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="6" id="u4079" role="tabpanel" aria-labelledby="u4085" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="6" data-src="images/12%20architecture_intercontinental%20hotel%20bar%20lights%20san%20francisco954x634.jpg?crc=245166864" src="images/12%20architecture_intercontinental%20hotel%20bar%20lights%20san%20francisco954x634.jpg?crc=245166864" alt="" data-heightwidthratio="0.6652675760755509" data-image-width="953" data-image-height="634" id="u4079_img" data-widget-id="slideshowu3846" style="height: 619.364px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="7" id="u4099" role="tabpanel" aria-labelledby="u4105" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="7" data-src="images/13%20architecture_intercontinental%20hotel%20bar%20lights%20san%20francisco954x634.jpg?crc=300627674" src="images/13%20architecture_intercontinental%20hotel%20bar%20lights%20san%20francisco954x634.jpg?crc=300627674" alt="" data-heightwidthratio="0.6652675760755509" data-image-width="953" data-image-height="634" id="u4099_img" data-widget-id="slideshowu3846" style="height: 619.364px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="8" id="u4119" role="tabpanel" aria-labelledby="u4125" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="8" data-src="images/14%20architecture_intercontinental%20hotel%20bar%20lights%20san%20francisco954x6342.jpg?crc=4049416800" src="images/14%20architecture_intercontinental%20hotel%20bar%20lights%20san%20francisco954x6342.jpg?crc=4049416800" alt="" data-heightwidthratio="0.6652675760755509" data-image-width="953" data-image-height="634" id="u4119_img" data-widget-id="slideshowu3846" style="height: 619.364px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="9" id="u4139" role="tabpanel" aria-labelledby="u4145" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="9" data-src="images/21%20architecture_napa%20county%20transportation%20-%20planning%20agency954x636.jpg?crc=4157844532" src="images/21%20architecture_napa%20county%20transportation%20-%20planning%20agency954x636.jpg?crc=4157844532" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u4139_img" data-widget-id="slideshowu3846" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="10" id="u4159" role="tabpanel" aria-labelledby="u4165" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="10" data-src="images/22%20architecture_napa%20county%20transportation%20-%20planning%20agency954x636.jpg?crc=212730440" src="images/22%20architecture_napa%20county%20transportation%20-%20planning%20agency954x636.jpg?crc=212730440" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u4159_img" data-widget-id="slideshowu3846" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="11" id="u4179" role="tabpanel" aria-labelledby="u4185" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="11" data-src="images/23%20architecture_napa%20county%20transportation%20-%20planning%20agency954x636.jpg?crc=428579771" src="images/23%20architecture_napa%20county%20transportation%20-%20planning%20agency954x636.jpg?crc=428579771" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u4179_img" data-widget-id="slideshowu3846" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="12" id="u4199" role="tabpanel" aria-labelledby="u4205" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="12" data-src="images/31%20architecture_fremont%20fire%20dept%20training%20center954x636.jpg?crc=3992431695" src="images/31%20architecture_fremont%20fire%20dept%20training%20center954x636.jpg?crc=3992431695" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u4199_img" data-widget-id="slideshowu3846" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="13" id="u4219" role="tabpanel" aria-labelledby="u4225" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="13" data-src="images/32%20architecture_fremont%20fire%20dept%20training%20center954x636.jpg?crc=4254504185" src="images/32%20architecture_fremont%20fire%20dept%20training%20center954x636.jpg?crc=4254504185" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u4219_img" data-widget-id="slideshowu3846" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="14" id="u4239" role="tabpanel" aria-labelledby="u4245" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="14" data-src="images/33%20architecture_fremont%20fire%20dept%20training%20center954x636.jpg?crc=3860616855" src="images/33%20architecture_fremont%20fire%20dept%20training%20center954x636.jpg?crc=3860616855" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u4239_img" data-widget-id="slideshowu3846" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="15" id="u4259" role="tabpanel" aria-labelledby="u4265" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="15" data-src="images/41%20architecture_midtown%20library%20-%20senior%20center954x636.jpg?crc=201757881" src="images/41%20architecture_midtown%20library%20-%20senior%20center954x636.jpg?crc=201757881" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u4259_img" data-widget-id="slideshowu3846" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="16" id="u4279" role="tabpanel" aria-labelledby="u4285" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="16" data-src="images/43%20architecture_midtown%20library%20-%20senior%20center954x636.jpg?crc=3901359327" src="images/43%20architecture_midtown%20library%20-%20senior%20center954x636.jpg?crc=3901359327" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u4279_img" data-widget-id="slideshowu3846" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="17" id="u4299" role="tabpanel" aria-labelledby="u4305" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="17" data-src="images/51%20architecture_transit%20center%20vallejo%2c%20ca954x623.jpg?crc=4117533349" src="images/51%20architecture_transit%20center%20vallejo%2c%20ca954x623.jpg?crc=4117533349" alt="" data-heightwidthratio="0.6537250786988458" data-image-width="953" data-image-height="623" id="u4299_img" data-widget-id="slideshowu3846" style="height: 608.618px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="18" id="u4319" role="tabpanel" aria-labelledby="u4325" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="18" data-src="images/52%20architecture_transit%20center%20vallejo%2c%20ca954x614.jpg?crc=199018754" src="images/52%20architecture_transit%20center%20vallejo%2c%20ca954x614.jpg?crc=199018754" alt="" data-heightwidthratio="0.6432318992654774" data-image-width="953" data-image-height="613" id="u4319_img" data-widget-id="slideshowu3846" style="height: 598.849px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="19" id="u4339" role="tabpanel" aria-labelledby="u4345" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="19" data-src="images/53%20architecture_transit%20center%20vallejo%2c%20ca954x630.jpg?crc=160486995" src="images/53%20architecture_transit%20center%20vallejo%2c%20ca954x630.jpg?crc=160486995" alt="" data-heightwidthratio="0.6600209863588667" data-image-width="953" data-image-height="629" id="u4339_img" data-widget-id="slideshowu3846" style="height: 614.48px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="20" id="u4359" role="tabpanel" aria-labelledby="u4365" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="20" data-src="images/61%20architecture_residential%20interior954x636.jpg?crc=252137002" src="images/61%20architecture_residential%20interior954x636.jpg?crc=252137002" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u4359_img" data-widget-id="slideshowu3846" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="21" id="u4379" role="tabpanel" aria-labelledby="u4385" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="21" data-src="images/62%20architecture_residential%20interior954x636.jpg?crc=459966866" src="images/62%20architecture_residential%20interior954x636.jpg?crc=459966866" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u4379_img" data-widget-id="slideshowu3846" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="22" id="u4399" role="tabpanel" aria-labelledby="u4405" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="22" data-src="images/67%20architecture_residential%20interior954x636.jpg?crc=516586185" src="images/67%20architecture_residential%20interior954x636.jpg?crc=516586185" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u4399_img" data-widget-id="slideshowu3846" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="23" id="u4419" role="tabpanel" aria-labelledby="u4425" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="23" data-src="images/68%20architecture_residential%20interior954x636.jpg?crc=3895193582" src="images/68%20architecture_residential%20interior954x636.jpg?crc=3895193582" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u4419_img" data-widget-id="slideshowu3846" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="24" id="u758925" role="tabpanel" aria-labelledby="u758951" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="24" data-src="images/71%20architectural%20photographer%20oakland954x636.jpg?crc=4033285809" src="images/71%20architectural%20photographer%20oakland954x636.jpg?crc=4033285809" alt="" data-heightwidthratio="0.6666666666666666" data-image-width="954" data-image-height="636" id="u758925_img" data-widget-id="slideshowu3846" style="height: 621.333px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="25" id="u759005" role="tabpanel" aria-labelledby="u759026" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="25" data-src="images/72%20architectural%20photographer%20oakland954x636.jpg?crc=4002328986" src="images/72%20architectural%20photographer%20oakland954x636.jpg?crc=4002328986" alt="" data-heightwidthratio="0.6666666666666666" data-image-width="954" data-image-height="636" id="u759005_img" data-widget-id="slideshowu3846" style="height: 621.333px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="26" id="u759080" role="tabpanel" aria-labelledby="u759101" style="height: 621px; display: none;"><!-- image -->
  <img class="block" data-col-pos="26" data-src="images/73%20architectural%20photographer%20oakland954x636.jpg?crc=4073476531" src="images/73%20architectural%20photographer%20oakland954x636.jpg?crc=4073476531" alt="" data-heightwidthratio="0.6666666666666666" data-image-width="954" data-image-height="636" id="u759080_img" data-widget-id="slideshowu3846" style="height: 621.333px;">
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

<img    src="images/11%20architecture_image954x636.jpg" alt=""    id="u3858_img"  >
<img class="block ImageInclude"   src="images/blank.gif" alt=""    id="u758523_img"  >
<img class="block ImageInclude"   src="images/blank.gif" alt=""    id="u758603_img"  >
<img class="block ImageInclude"   src="images/blank.gif" alt=""    id="u758678_img"  >
<img class="block ImageInclude"   src="images/blank.gif" alt=""    id="u758753_img"  >
<img class="block ImageInclude"   src="images/blank.gif" alt=""    id="u758828_img"  >
<img    src="images/12%20architecture_intercontinental%20hotel%20bar%20lights%20san%20francisco954x634.jpg" alt=""    id="u4079_img"  >
<img    src="images/13%20architecture_intercontinental%20hotel%20bar%20lights%20san%20francisco954x634.jpg" alt=""    id="u4099_img"  >
<img    src="images/14%20architecture_intercontinental%20hotel%20bar%20lights%20san%20francisco954x6342.jpg" alt=""    id="u4119_img"  >
<img    src="images/21%20architecture_napa%20county%20transportation%20-%20planning%20agency954x636.jpg" alt=""    id="u4139_img"  >
<img    src="images/22%20architecture_napa%20county%20transportation%20-%20planning%20agency954x636.jpg" alt=""    id="u4159_img"  >
<img    src="images/23%20architecture_napa%20county%20transportation%20-%20planning%20agency954x636.jpg" alt=""    id="u4179_img"  >
<img    src="images/31%20architecture_fremont%20fire%20dept%20training%20center954x636.jpg" alt=""    id="u4199_img"  >
<img    src="images/32%20architecture_fremont%20fire%20dept%20training%20center954x636.jpg" alt=""    id="u4219_img"  >
<img    src="images/33%20architecture_fremont%20fire%20dept%20training%20center954x636.jpg" alt=""    id="u4239_img"  >
<img    src="images/41%20architecture_midtown%20library%20-%20senior%20center954x636.jpg" alt=""    id="u4259_img"  >
<img    src="images/43%20architecture_midtown%20library%20-%20senior%20center954x636.jpg" alt=""    id="u4279_img"  >
<img    src="images/51%20architecture_transit%20center%20vallejo%2c%20ca954x623.jpg" alt=""    id="u4299_img"  >
<img    src="images/52%20architecture_transit%20center%20vallejo%2c%20ca954x614.jpg" alt=""    id="u4319_img"  >
<img    src="images/53%20architecture_transit%20center%20vallejo%2c%20ca954x630.jpg" alt=""    id="u4339_img"  >
<img    src="images/61%20architecture_residential%20interior954x636.jpg" alt=""    id="u4359_img"  >
<img    src="images/62%20architecture_residential%20interior954x636.jpg" alt=""    id="u4379_img"  >
<img    src="images/67%20architecture_residential%20interior954x636.jpg" alt=""    id="u4399_img"  >
<img    src="images/68%20architecture_residential%20interior954x636.jpg" alt=""    id="u4419_img"  >
<img    src="images/71%20architectural%20photographer%20oakland954x636.jpg" alt=""    id="u758925_img"  >
<img    src="images/72%20architectural%20photographer%20oakland954x636.jpg" alt=""    id="u759005_img"  >
<img    src="images/73%20architectural%20photographer%20oakland954x636.jpg" alt=""    id="u759080_img"  > 

# SECOND ROUND MINI IMAGES

import re

data = '''<!-- column -->
<div class="SSSlideLink clip_frame colelem wp-tab-active SSSlideLinkSelected" data-col-pos="0" id="u3850" role="tab" tabindex="0" aria-selected="true" aria-controls="u3858" style="height: 37px;"><!-- image -->
<img class="block" data-col-pos="0" alt="" data-heightwidthratio="0.9047619047619048" data-image-width="42" data-image-height="38" src="images/11%20architecture_image-crop-u38502.jpg?crc=366125988" id="u3850_img" data-widget-id="slideshowu3846" style="height: 37.0952px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="2" id="u758624" role="tab" tabindex="-1" aria-selected="false" aria-controls="u758603" style="height: 37px;"><!-- image -->
<img class="block" data-col-pos="2" alt="" data-heightwidthratio="0.9047619047619048" data-image-width="42" data-image-height="38" src="images/%202%20architectural%20photographer%20san%20francisco-crop-u7586242.jpg?crc=386444673" id="u758624_img" data-widget-id="slideshowu3846" style="height: 37.0952px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="4" id="u758774" role="tab" tabindex="-1" aria-selected="false" aria-controls="u758753" style="height: 37px;"><!-- image -->
<img class="block" data-col-pos="4" alt="" data-heightwidthratio="0.9047619047619048" data-image-width="42" data-image-height="38" src="images/%204%20architectural%20photographer%20san%20francisco-crop-u7587742.jpg?crc=4129267776" id="u758774_img" data-widget-id="slideshowu3846" style="height: 37.0952px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="6" id="u4085" role="tab" tabindex="-1" aria-selected="false" aria-controls="u4079" style="height: 37px;"><!-- image -->
<img class="block" data-col-pos="6" alt="" data-heightwidthratio="0.9047619047619048" data-image-width="42" data-image-height="38" src="images/12%20architecture_intercontinental%20hotel%20bar%20lights%20san%20francisco-crop-u40852.jpg?crc=91501788" id="u4085_img" data-widget-id="slideshowu3846" style="height: 37.0952px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="8" id="u4125" role="tab" tabindex="-1" aria-selected="false" aria-controls="u4119" style="height: 37px;"><!-- image -->
<img class="block" data-col-pos="8" alt="" data-heightwidthratio="0.9047619047619048" data-image-width="42" data-image-height="38" src="images/14%20architecture_intercontinental%20hotel%20bar%20lights%20san%20francisco-crop-u41252.jpg?crc=517448447" id="u4125_img" data-widget-id="slideshowu3846" style="height: 37.0952px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="10" id="u4165" role="tab" tabindex="-1" aria-selected="false" aria-controls="u4159" style="height: 37px;"><!-- image -->
<img class="block" data-col-pos="10" alt="" data-heightwidthratio="0.9047619047619048" data-image-width="42" data-image-height="38" src="images/22%20architecture_napa%20county%20transportation%20-%20planning%20agency-crop-u41652.jpg?crc=61335673" id="u4165_img" data-widget-id="slideshowu3846" style="height: 37.0952px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="12" id="u4205" role="tab" tabindex="-1" aria-selected="false" aria-controls="u4199" style="height: 37px;"><!-- image -->
<img class="block" data-col-pos="12" alt="" data-heightwidthratio="0.9047619047619048" data-image-width="42" data-image-height="38" src="images/31%20architecture_fremont%20fire%20dept%20training%20center-crop-u42052.jpg?crc=4041888144" id="u4205_img" data-widget-id="slideshowu3846" style="height: 37.0952px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="14" id="u4245" role="tab" tabindex="-1" aria-selected="false" aria-controls="u4239" style="height: 37px;"><!-- image -->
<img class="block" data-col-pos="14" alt="" data-heightwidthratio="0.9047619047619048" data-image-width="42" data-image-height="38" src="images/33%20architecture_fremont%20fire%20dept%20training%20center-crop-u42452.jpg?crc=4053206608" id="u4245_img" data-widget-id="slideshowu3846" style="height: 37.0952px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="16" id="u4285" role="tab" tabindex="-1" aria-selected="false" aria-controls="u4279" style="height: 37px;"><!-- image -->
<img class="block" data-col-pos="16" alt="" data-heightwidthratio="0.9047619047619048" data-image-width="42" data-image-height="38" src="images/43%20architecture_midtown%20library%20-%20senior%20center-crop-u42852.jpg?crc=117581821" id="u4285_img" data-widget-id="slideshowu3846" style="height: 37.0952px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="18" id="u4325" role="tab" tabindex="-1" aria-selected="false" aria-controls="u4319" style="height: 37px;"><!-- image -->
<img class="block" data-col-pos="18" alt="" data-heightwidthratio="0.9047619047619048" data-image-width="42" data-image-height="38" src="images/52%20architecture_transit%20center%20vallejo%2c%20ca-crop-u43252.jpg?crc=148176876" id="u4325_img" data-widget-id="slideshowu3846" style="height: 37.0952px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="20" id="u4365" role="tab" tabindex="-1" aria-selected="false" aria-controls="u4359" style="height: 37px;"><!-- image -->
<img class="block" data-col-pos="20" alt="" data-heightwidthratio="0.9047619047619048" data-image-width="42" data-image-height="38" src="images/61%20architecture_residential%20interior-crop-u43652.jpg?crc=4007737096" id="u4365_img" data-widget-id="slideshowu3846" style="height: 37.0952px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="22" id="u4405" role="tab" tabindex="-1" aria-selected="false" aria-controls="u4399" style="height: 37px;"><!-- image -->
<img class="block" data-col-pos="22" alt="" data-heightwidthratio="0.9047619047619048" data-image-width="42" data-image-height="38" src="images/67%20architecture_residential%20interior-crop-u44052.jpg?crc=3803862551" id="u4405_img" data-widget-id="slideshowu3846" style="height: 37.0952px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="24" id="u758951" role="tab" tabindex="-1" aria-selected="false" aria-controls="u758925" style="height: 37px;"><!-- image -->
<img class="block" data-col-pos="24" alt="" data-heightwidthratio="0.9047619047619048" data-image-width="42" data-image-height="38" src="images/71%20architectural%20photographer%20oakland-crop-u7589512.jpg?crc=230310167" id="u758951_img" data-widget-id="slideshowu3846" style="height: 37.0952px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="26" id="u759101" role="tab" tabindex="-1" aria-selected="false" aria-controls="u759080" style="height: 37px;"><!-- image -->
<img class="block" data-col-pos="26" alt="" data-heightwidthratio="0.9047619047619048" data-image-width="42" data-image-height="38" src="images/73%20architectural%20photographer%20oakland-crop-u7591012.jpg?crc=4085869011" id="u759101_img" data-widget-id="slideshowu3846" style="height: 37.0952px;">
</div>
<!-- column -->
<div class="SSSlideLink clip_frame colelem" data-col-pos="1" id="u758549" role="tab" tabindex="-1" aria-selected="false" aria-controls="u758523" style="height: 37px;"><!-- image -->
<img class="block" data-col-pos="1" alt="" data-heightwidthratio="0.9047619047619048" data-image-width="42" data-image-height="38" src="images/%201%20architectural%20photographer%20san%20francisco-crop-u7585492.jpg?crc=3931510653" id="u758549_img" data-widget-id="slideshowu3846" style="height: 37.0952px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="3" id="u758699" role="tab" tabindex="-1" aria-selected="false" aria-controls="u758678" style="height: 37px;"><!-- image -->
<img class="block" data-col-pos="3" alt="" data-heightwidthratio="0.9047619047619048" data-image-width="42" data-image-height="38" src="images/%203%20architectural%20photographer%20san%20francisco-crop-u7586992.jpg?crc=280488159" id="u758699_img" data-widget-id="slideshowu3846" style="height: 37.0952px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="5" id="u758849" role="tab" tabindex="-1" aria-selected="false" aria-controls="u758828" style="height: 37px;"><!-- image -->
<img class="block" data-col-pos="5" alt="" data-heightwidthratio="0.9047619047619048" data-image-width="42" data-image-height="38" src="images/%205%20architectural%20photographer%20san%20francisco-crop-u7588492.jpg?crc=194861464" id="u758849_img" data-widget-id="slideshowu3846" style="height: 37.0952px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="7" id="u4105" role="tab" tabindex="-1" aria-selected="false" aria-controls="u4099" style="height: 37px;"><!-- image -->
<img class="block" data-col-pos="7" alt="" data-heightwidthratio="0.9047619047619048" data-image-width="42" data-image-height="38" src="images/13%20architecture_intercontinental%20hotel%20bar%20lights%20san%20francisco-crop-u41052.jpg?crc=3956319348" id="u4105_img" data-widget-id="slideshowu3846" style="height: 37.0952px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="9" id="u4145" role="tab" tabindex="-1" aria-selected="false" aria-controls="u4139" style="height: 37px;"><!-- image -->
<img class="block" data-col-pos="9" alt="" data-heightwidthratio="0.9047619047619048" data-image-width="42" data-image-height="38" src="images/21%20architecture_napa%20county%20transportation%20-%20planning%20agency-crop-u41452.jpg?crc=517263263" id="u4145_img" data-widget-id="slideshowu3846" style="height: 37.0952px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="11" id="u4185" role="tab" tabindex="-1" aria-selected="false" aria-controls="u4179" style="height: 37px;"><!-- image -->
<img class="block" data-col-pos="11" alt="" data-heightwidthratio="0.9047619047619048" data-image-width="42" data-image-height="38" src="images/23%20architecture_napa%20county%20transportation%20-%20planning%20agency-crop-u41852.jpg?crc=367702083" id="u4185_img" data-widget-id="slideshowu3846" style="height: 37.0952px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="13" id="u4225" role="tab" tabindex="-1" aria-selected="false" aria-controls="u4219" style="height: 37px;"><!-- image -->
<img class="block" data-col-pos="13" alt="" data-heightwidthratio="0.9047619047619048" data-image-width="42" data-image-height="38" src="images/32%20architecture_fremont%20fire%20dept%20training%20center-crop-u42252.jpg?crc=4143956455" id="u4225_img" data-widget-id="slideshowu3846" style="height: 37.0952px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="15" id="u4265" role="tab" tabindex="-1" aria-selected="false" aria-controls="u4259" style="height: 37px;"><!-- image -->
<img class="block" data-col-pos="15" alt="" data-heightwidthratio="0.9047619047619048" data-image-width="42" data-image-height="38" src="images/41%20architecture_midtown%20library%20-%20senior%20center-crop-u42652.jpg?crc=4086416353" id="u4265_img" data-widget-id="slideshowu3846" style="height: 37.0952px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="17" id="u4305" role="tab" tabindex="-1" aria-selected="false" aria-controls="u4299" style="height: 37px;"><!-- image -->
<img class="block" data-col-pos="17" alt="" data-heightwidthratio="0.9047619047619048" data-image-width="42" data-image-height="38" src="images/51%20architecture_transit%20center%20vallejo%2c%20ca-crop-u43052.jpg?crc=4173370272" id="u4305_img" data-widget-id="slideshowu3846" style="height: 37.0952px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="19" id="u4345" role="tab" tabindex="-1" aria-selected="false" aria-controls="u4339" style="height: 37px;"><!-- image -->
<img class="block" data-col-pos="19" alt="" data-heightwidthratio="0.9047619047619048" data-image-width="42" data-image-height="38" src="images/53%20architecture_transit%20center%20vallejo%2c%20ca-crop-u43452.jpg?crc=4261024282" id="u4345_img" data-widget-id="slideshowu3846" style="height: 37.0952px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="21" id="u4385" role="tab" tabindex="-1" aria-selected="false" aria-controls="u4379" style="height: 37px;"><!-- image -->
<img class="block" data-col-pos="21" alt="" data-heightwidthratio="0.9047619047619048" data-image-width="42" data-image-height="38" src="images/62%20architecture_residential%20interior-crop-u43852.jpg?crc=270866922" id="u4385_img" data-widget-id="slideshowu3846" style="height: 37.0952px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="23" id="u4425" role="tab" tabindex="-1" aria-selected="false" aria-controls="u4419" style="height: 37px;"><!-- image -->
<img class="block" data-col-pos="23" alt="" data-heightwidthratio="0.9047619047619048" data-image-width="42" data-image-height="38" src="images/68%20architecture_residential%20interior-crop-u44252.jpg?crc=4123980420" id="u4425_img" data-widget-id="slideshowu3846" style="height: 37.0952px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="25" id="u759026" role="tab" tabindex="-1" aria-selected="false" aria-controls="u759005" style="height: 37px;"><!-- image -->
<img class="block" data-col-pos="25" alt="" data-heightwidthratio="0.9047619047619048" data-image-width="42" data-image-height="38" src="images/72%20architectural%20photographer%20oakland-crop-u7590262.jpg?crc=4153490677" id="u759026_img" data-widget-id="slideshowu3846" style="height: 37.0952px;">
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