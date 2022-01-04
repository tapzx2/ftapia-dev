import re

data = '''<!-- stack box -->
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="0" id="u32817" role="tabpanel" aria-labelledby="u32813" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="0" data-src="images/11%20advertising_photographer_%20san%20francisco954x636.jpg?crc=3991756518" src="images/11%20advertising_photographer_%20san%20francisco954x636.jpg?crc=3991756518" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u32817_img" data-widget-id="slideshowu32805" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="1" id="u33069" role="tabpanel" aria-labelledby="u33075" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="1" data-src="images/12%20advertising_photography954x636.jpg?crc=374851356" src="images/12%20advertising_photography954x636.jpg?crc=374851356" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u33069_img" data-widget-id="slideshowu32805" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="2" id="u33089" role="tabpanel" aria-labelledby="u33095" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="2" data-src="images/13%20advertising_image_danko%20law%20firm954x636.jpg?crc=3934215682" src="images/13%20advertising_image_danko%20law%20firm954x636.jpg?crc=3934215682" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u33089_img" data-widget-id="slideshowu32805" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="3" id="u33109" role="tabpanel" aria-labelledby="u33115" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="3" data-src="images/14%20advertising_image_fuse%20arct954x636.jpg?crc=3974186830" src="images/14%20advertising_image_fuse%20arct954x636.jpg?crc=3974186830" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u33109_img" data-widget-id="slideshowu32805" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="4" id="u33129" role="tabpanel" aria-labelledby="u33135" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="4" data-src="images/21%20advertising_image%20_abramson-smith-waldsmith%20%2c%20llp%2c954x636.jpg?crc=447073864" src="images/21%20advertising_image%20_abramson-smith-waldsmith%20%2c%20llp%2c954x636.jpg?crc=447073864" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u33129_img" data-widget-id="slideshowu32805" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="5" id="u33149" role="tabpanel" aria-labelledby="u33155" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="5" data-src="images/22advertising_image%20_abramson-smith-waldsmith%20%2c-llp%2c954x591.jpg?crc=3903289305" src="images/22advertising_image%20_abramson-smith-waldsmith%20%2c-llp%2c954x591.jpg?crc=3903289305" alt="" data-heightwidthratio="0.6190975865687304" data-image-width="953" data-image-height="590" id="u33149_img" data-widget-id="slideshowu32805" style="height: 576.38px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="6" id="u33169" role="tabpanel" aria-labelledby="u33175" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="6" data-src="images/23advertising_image%20_abramson-smith-waldsmith%20%2c-llp%2c605x636.jpg?crc=3916122507" src="images/23advertising_image%20_abramson-smith-waldsmith%20%2c-llp%2c605x636.jpg?crc=3916122507" alt="" data-heightwidthratio="1.0529801324503312" data-image-width="604" data-image-height="636" id="u33169_img" data-widget-id="slideshowu32805" style="height: 621.592px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="7" id="u33189" role="tabpanel" aria-labelledby="u33195" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="7" data-src="images/24advertising_image%20_abramson-smith-waldsmith%2c-llp%2c954x636.jpg?crc=4174317064" src="images/24advertising_image%20_abramson-smith-waldsmith%2c-llp%2c954x636.jpg?crc=4174317064" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u33189_img" data-widget-id="slideshowu32805" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="8" id="u33209" role="tabpanel" aria-labelledby="u33215" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="8" data-src="images/241advertising_image_abramson-smith-waldsmith%2c%20llp%2c954x605.jpg?crc=4156677768" src="images/241advertising_image_abramson-smith-waldsmith%2c%20llp%2c954x605.jpg?crc=4156677768" alt="" data-heightwidthratio="0.633788037775446" data-image-width="953" data-image-height="604" id="u33209_img" data-widget-id="slideshowu32805" style="height: 590.057px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="9" id="u714524" role="tabpanel" aria-labelledby="u714550" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="9" data-src="images/251fm%20industrial%2c%20inc954x566.jpg?crc=3971013515" src="images/251fm%20industrial%2c%20inc954x566.jpg?crc=3971013515" alt="" data-heightwidthratio="0.5939139559286464" data-image-width="953" data-image-height="566" id="u714524_img" data-widget-id="slideshowu32805" style="height: 552.934px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="10" id="u714604" role="tabpanel" aria-labelledby="u714625" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="10" data-src="images/252industrial_photographer_fm%20industrial%2c%20inc954x584.jpg?crc=506548205" src="images/252industrial_photographer_fm%20industrial%2c%20inc954x584.jpg?crc=506548205" alt="" data-heightwidthratio="0.6128016789087093" data-image-width="953" data-image-height="584" id="u714604_img" data-widget-id="slideshowu32805" style="height: 570.518px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="11" id="u714859" role="tabpanel" aria-labelledby="u714885" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="11" data-src="images/261%20advertising_image_499x636.jpg?crc=198549231" src="images/261%20advertising_image_499x636.jpg?crc=198549231" alt="" data-heightwidthratio="1.2745490981963927" data-image-width="499" data-image-height="636" id="u714859_img" data-widget-id="slideshowu32805" style="height: 621.767px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="12" id="u714987" role="tabpanel" aria-labelledby="u715013" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="12" data-src="images/262_advertising%20photographer_fight%20night801x636.jpg?crc=50249192" src="images/262_advertising%20photographer_fight%20night801x636.jpg?crc=50249192" alt="" data-heightwidthratio="0.795" data-image-width="800" data-image-height="636" id="u714987_img" data-widget-id="slideshowu32805" style="height: 621.412px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="13" id="u33249" role="tabpanel" aria-labelledby="u33255" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="13" data-src="images/33%20advertising%20_photographer_teraoka954x636.jpg?crc=3817075012" src="images/33%20advertising%20_photographer_teraoka954x636.jpg?crc=3817075012" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u33249_img" data-widget-id="slideshowu32805" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="14" id="u33269" role="tabpanel" aria-labelledby="u33275" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="14" data-src="images/32%20advertising%20_image_teraoka954x618.jpg?crc=3874696698" src="images/32%20advertising%20_image_teraoka954x618.jpg?crc=3874696698" alt="" data-heightwidthratio="0.6474291710388248" data-image-width="953" data-image-height="617" id="u33269_img" data-widget-id="slideshowu32805" style="height: 602.757px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="15" id="u33289" role="tabpanel" aria-labelledby="u33295" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="15" data-src="images/33%20advertising%20_photographer_teraoka954x636.jpg?crc=3817075012" src="images/33%20advertising%20_photographer_teraoka954x636.jpg?crc=3817075012" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u33289_img" data-widget-id="slideshowu32805" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="16" id="u33309" role="tabpanel" aria-labelledby="u33315" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="16" data-src="images/34%20advertising_image_cyan_lab954x6362.jpg?crc=335567405" src="images/34%20advertising_image_cyan_lab954x6362.jpg?crc=335567405" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u33309_img" data-widget-id="slideshowu32805" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel wp-panel-active" data-col-pos="17" id="u33329" role="tabpanel" aria-labelledby="u33335" style="height: 622px;"><!-- image -->
  <img class="block" data-col-pos="17" data-src="images/35%20advertising_image_cyan_z-series954x636.jpg?crc=3864020488" src="images/35%20advertising_image_cyan_z-series954x636.jpg?crc=3864020488" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u33329_img" data-widget-id="slideshowu32805" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="18" id="u33349" role="tabpanel" aria-labelledby="u33355" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="18" data-src="images/41%20advertising_image_mary%20alexander898x630.jpg?crc=3855989884" src="images/41%20advertising_image_mary%20alexander898x630.jpg?crc=3855989884" alt="" data-heightwidthratio="0.700445434298441" data-image-width="898" data-image-height="629" id="u33349_img" data-widget-id="slideshowu32805" style="height: 614.524px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="19" id="u33369" role="tabpanel" aria-labelledby="u33375" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="19" data-src="images/42%20advertising_image_mary%20alexander919x636.jpg?crc=225523828" src="images/42%20advertising_image_mary%20alexander919x636.jpg?crc=225523828" alt="" data-heightwidthratio="0.6928104575163399" data-image-width="918" data-image-height="636" id="u33369_img" data-widget-id="slideshowu32805" style="height: 621.347px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="20" id="u33389" role="tabpanel" aria-labelledby="u33395" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="20" data-src="images/43%20advertising_image_pinta%20acoustic954x636.jpg?crc=4171500941" src="images/43%20advertising_image_pinta%20acoustic954x636.jpg?crc=4171500941" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u33389_img" data-widget-id="slideshowu32805" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="21" id="u33409" role="tabpanel" aria-labelledby="u33415" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="21" data-src="images/51%20advertising_image_gwilliam-ivary-chiosso-cavalli---brewer954x636.jpg?crc=61967978" src="images/51%20advertising_image_gwilliam-ivary-chiosso-cavalli---brewer954x636.jpg?crc=61967978" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u33409_img" data-widget-id="slideshowu32805" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="22" id="u33429" role="tabpanel" aria-labelledby="u33435" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="22" data-src="images/52%20advertising_image_hartog-baer-hand954x636.jpg?crc=302352781" src="images/52%20advertising_image_hartog-baer-hand954x636.jpg?crc=302352781" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u33429_img" data-widget-id="slideshowu32805" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="23" id="u33449" role="tabpanel" aria-labelledby="u33455" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="23" data-src="images/53%20advertising_image_954x636.jpg?crc=495822927" src="images/53%20advertising_image_954x636.jpg?crc=495822927" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u33449_img" data-widget-id="slideshowu32805" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="24" id="u691251" role="tabpanel" aria-labelledby="u691273" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="24" data-src="images/61%20advertising%20corporate%20photographer954x636.jpg?crc=3823196423" src="images/61%20advertising%20corporate%20photographer954x636.jpg?crc=3823196423" alt="" data-heightwidthratio="0.6666666666666666" data-image-width="954" data-image-height="636" id="u691251_img" data-widget-id="slideshowu32805" style="height: 621.333px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="25" id="u691451" role="tabpanel" aria-labelledby="u691473" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="25" data-src="images/62alto%20litigation%2c%20pc954x636.jpg?crc=441720243" src="images/62alto%20litigation%2c%20pc954x636.jpg?crc=441720243" alt="" data-heightwidthratio="0.6666666666666666" data-image-width="954" data-image-height="636" id="u691451_img" data-widget-id="slideshowu32805" style="height: 621.333px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="26" id="u691711" role="tabpanel" aria-labelledby="u691729" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="26" data-src="images/65%20minami%20tamaki%20llp954x636.jpg?crc=135178473" src="images/65%20minami%20tamaki%20llp954x636.jpg?crc=135178473" alt="" data-heightwidthratio="0.6666666666666666" data-image-width="954" data-image-height="636" id="u691711_img" data-widget-id="slideshowu32805" style="height: 621.333px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="27" id="u691775" role="tabpanel" aria-labelledby="u691793" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="27" data-src="images/67advertising_image_abramson-smith-waldsmith%2c%20llp%2c-crop-u6917753.jpg?crc=119210254" src="images/67advertising_image_abramson-smith-waldsmith%2c%20llp%2c-crop-u6917753.jpg?crc=119210254" alt="" data-heightwidthratio="0.6666666666666666" data-image-width="954" data-image-height="636" id="u691775_img" data-widget-id="slideshowu32805" style="height: 621.333px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="28" id="u706674" role="tabpanel" aria-labelledby="u706700" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="28" data-src="images/68%20advertising%20photograhy_winer%2c%20burritt%20-%20tillis%20llp954x602.jpg?crc=168890339" src="images/68%20advertising%20photograhy_winer%2c%20burritt%20-%20tillis%20llp954x602.jpg?crc=168890339" alt="" data-heightwidthratio="0.6306400839454355" data-image-width="953" data-image-height="601" id="u706674_img" data-widget-id="slideshowu32805" style="height: 587.126px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="29" id="u691903" role="tabpanel" aria-labelledby="u691921" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="29" data-src="images/71%20advertising%20product%20photographer_teresonic954x636.jpg?crc=470383898" src="images/71%20advertising%20product%20photographer_teresonic954x636.jpg?crc=470383898" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u691903_img" data-widget-id="slideshowu32805" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="30" id="u691967" role="tabpanel" aria-labelledby="u691985" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="30" data-src="images/7advertising%20product%20photographer_seta%20di%20gioia-crop-u691967.jpg?crc=116577151" src="images/7advertising%20product%20photographer_seta%20di%20gioia-crop-u691967.jpg?crc=116577151" alt="" data-heightwidthratio="0.6666666666666666" data-image-width="954" data-image-height="636" id="u691967_img" data-widget-id="slideshowu32805" style="height: 621.333px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="31" id="u715075" role="tabpanel" aria-labelledby="u715101" style="height: 622px; display: none;"><!-- image -->
  <img class="block" data-col-pos="31" data-src="images/8937x636.jpg?crc=4192634881" src="images/8937x636.jpg?crc=4192634881" alt="" data-heightwidthratio="0.6787620064034151" data-image-width="937" data-image-height="636" id="u715075_img" data-widget-id="slideshowu32805" style="height: 621.35px;">
</div>
         '''

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

<img    src="images/11%20advertising_photographer_%20san%20francisco954x636.jpg" alt=""    id="u32817_img"  >
<img    src="images/12%20advertising_photography954x636.jpg" alt=""    id="u33069_img"  >
<img    src="images/13%20advertising_image_danko%20law%20firm954x636.jpg" alt=""    id="u33089_img"  >
<img    src="images/14%20advertising_image_fuse%20arct954x636.jpg" alt=""    id="u33109_img"  >
<img    src="images/21%20advertising_image%20_abramson-smith-waldsmith%20%2c%20llp%2c954x636.jpg" alt=""    id="u33129_img"  >
<img    src="images/22advertising_image%20_abramson-smith-waldsmith%20%2c-llp%2c954x591.jpg" alt=""    id="u33149_img"  >
<img    src="images/23advertising_image%20_abramson-smith-waldsmith%20%2c-llp%2c605x636.jpg" alt=""    id="u33169_img"  >
<img    src="images/24advertising_image%20_abramson-smith-waldsmith%2c-llp%2c954x636.jpg" alt=""    id="u33189_img"  >
<img    src="images/241advertising_image_abramson-smith-waldsmith%2c%20llp%2c954x605.jpg" alt=""    id="u33209_img"  >
<img    src="images/251fm%20industrial%2c%20inc954x566.jpg" alt=""    id="u714524_img"  >
<img    src="images/252industrial_photographer_fm%20industrial%2c%20inc954x584.jpg" alt=""    id="u714604_img"  >
<img    src="images/261%20advertising_image_499x636.jpg" alt=""    id="u714859_img"  >
<img    src="images/262_advertising%20photographer_fight%20night801x636.jpg" alt=""    id="u714987_img"  >
<img    src="images/33%20advertising%20_photographer_teraoka954x636.jpg" alt=""    id="u33249_img"  >
<img    src="images/32%20advertising%20_image_teraoka954x618.jpg" alt=""    id="u33269_img"  >
<img    src="images/33%20advertising%20_photographer_teraoka954x636.jpg" alt=""    id="u33289_img"  >
<img    src="images/34%20advertising_image_cyan_lab954x6362.jpg" alt=""    id="u33309_img"  >
<img    src="images/35%20advertising_image_cyan_z-series954x636.jpg" alt=""    id="u33329_img"  >
<img    src="images/41%20advertising_image_mary%20alexander898x630.jpg" alt=""    id="u33349_img"  >
<img    src="images/42%20advertising_image_mary%20alexander919x636.jpg" alt=""    id="u33369_img"  >
<img    src="images/43%20advertising_image_pinta%20acoustic954x636.jpg" alt=""    id="u33389_img"  >
<img    src="images/51%20advertising_image_gwilliam-ivary-chiosso-cavalli---brewer954x636.jpg" alt=""    id="u33409_img"  >
<img    src="images/52%20advertising_image_hartog-baer-hand954x636.jpg" alt=""    id="u33429_img"  >
<img    src="images/53%20advertising_image_954x636.jpg" alt=""    id="u33449_img"  >
<img    src="images/61%20advertising%20corporate%20photographer954x636.jpg" alt=""    id="u691251_img"  >
<img    src="images/62alto%20litigation%2c%20pc954x636.jpg" alt=""    id="u691451_img"  >
<img    src="images/65%20minami%20tamaki%20llp954x636.jpg" alt=""    id="u691711_img"  >
<img    src="images/67advertising_image_abramson-smith-waldsmith%2c%20llp%2c-crop-u6917753.jpg" alt=""    id="u691775_img"  >
<img    src="images/68%20advertising%20photograhy_winer%2c%20burritt%20-%20tillis%20llp954x602.jpg" alt=""    id="u706674_img"  >
<img    src="images/71%20advertising%20product%20photographer_teresonic954x636.jpg" alt=""    id="u691903_img"  >
<img    src="images/7advertising%20product%20photographer_seta%20di%20gioia-crop-u691967.jpg" alt=""    id="u691967_img"  >
<img    src="images/8937x636.jpg" alt=""    id="u715075_img"  >

# round 2 MINI IMAGES!

import re

data = '''<!-- column -->
<div class="SSSlideLink clip_frame colelem" data-col-pos="0" id="u32813" role="tab" tabindex="-1" aria-selected="false" aria-controls="u32817" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="0" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/11%20advertising_photographer_%20san%20francisco-crop-u328132.jpg?crc=3912390214" id="u32813_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="2" id="u33095" role="tab" tabindex="-1" aria-selected="false" aria-controls="u33089" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="2" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/13%20advertising_image_danko%20law%20firm-crop-u330953.jpg?crc=3915966557" id="u33095_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="4" id="u33135" role="tab" tabindex="-1" aria-selected="false" aria-controls="u33129" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="4" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/21%20advertising_image%20_abramson-smith-waldsmith%20%2c%20llp%2c-crop-u331353.jpg?crc=452372878" id="u33135_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="6" id="u33175" role="tab" tabindex="-1" aria-selected="false" aria-controls="u33169" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="6" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/23advertising_image%20_abramson-smith-waldsmith%20%2c-llp%2c-crop-u331753.jpg?crc=4143346537" id="u33175_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="8" id="u33215" role="tab" tabindex="-1" aria-selected="false" aria-controls="u33209" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="8" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/241advertising_image_abramson-smith-waldsmith%2c%20llp%2c-crop-u332153.jpg?crc=4182766561" id="u33215_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="10" id="u714625" role="tab" tabindex="-1" aria-selected="false" aria-controls="u714604" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="10" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/252industrial_photographer_fm%20industrial%2c%20inc-crop-u7146253.jpg?crc=3963539476" id="u714625_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="12" id="u715013" role="tab" tabindex="-1" aria-selected="false" aria-controls="u714987" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="12" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/262_advertising%20photographer_fight%20night-crop-u7150133.jpg?crc=270916956" id="u715013_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="14" id="u33275" role="tab" tabindex="-1" aria-selected="false" aria-controls="u33269" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="14" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/32%20advertising%20_image_teraoka-crop-u332753.jpg?crc=173040802" id="u33275_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="16" id="u33315" role="tab" tabindex="-1" aria-selected="false" aria-controls="u33309" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="16" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/34%20advertising_image_cyan_lab-crop-u333153.jpg?crc=4018581664" id="u33315_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="18" id="u33355" role="tab" tabindex="-1" aria-selected="false" aria-controls="u33349" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="18" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/41%20advertising_image_mary%20alexander-crop-u333553.jpg?crc=3808643071" id="u33355_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="20" id="u33395" role="tab" tabindex="-1" aria-selected="false" aria-controls="u33389" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="20" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/43%20advertising_image_pinta%20acoustic-crop-u333953.jpg?crc=3858378048" id="u33395_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="22" id="u33435" role="tab" tabindex="-1" aria-selected="false" aria-controls="u33429" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="22" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/52%20advertising_image_hartog-baer-hand-crop-u334353.jpg?crc=3880718182" id="u33435_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="24" id="u691273" role="tab" tabindex="-1" aria-selected="false" aria-controls="u691251" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="24" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/61%20advertising%20corporate%20photographer-crop-u6912733.jpg?crc=437572631" id="u691273_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="26" id="u691729" role="tab" tabindex="-1" aria-selected="false" aria-controls="u691711" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="26" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/65%20minami%20tamaki%20llp-crop-u6917293.jpg?crc=264483456" id="u691729_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="28" id="u706700" role="tab" tabindex="-1" aria-selected="false" aria-controls="u706674" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="28" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/68%20advertising%20photograhy_winer%2c%20burritt%20-%20tillis%20llp-crop-u7067003.jpg?crc=4191553049" id="u706700_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="30" id="u691985" role="tab" tabindex="-1" aria-selected="false" aria-controls="u691967" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="30" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/7advertising%20product%20photographer_seta%20di%20gioia-crop-u6919853.jpg?crc=4191380321" id="u691985_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<!-- column -->
<div class="SSSlideLink clip_frame colelem" data-col-pos="1" id="u33075" role="tab" tabindex="-1" aria-selected="false" aria-controls="u33069" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="1" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/12%20advertising_photography-crop-u330752.jpg?crc=4225119165" id="u33075_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="3" id="u33115" role="tab" tabindex="-1" aria-selected="false" aria-controls="u33109" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="3" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/14%20advertising_image_fuse%20arct-crop-u331153.jpg?crc=286551650" id="u33115_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="5" id="u33155" role="tab" tabindex="-1" aria-selected="false" aria-controls="u33149" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="5" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/22advertising_image%20_abramson-smith-waldsmith%20%2c-llp%2c-crop-u331553.jpg?crc=3888077829" id="u33155_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="7" id="u33195" role="tab" tabindex="-1" aria-selected="false" aria-controls="u33189" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="7" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/24advertising_image%20_abramson-smith-waldsmith%2c-llp%2c-crop-u331953.jpg?crc=228470910" id="u33195_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="9" id="u714550" role="tab" tabindex="-1" aria-selected="false" aria-controls="u714524" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="9" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/251fm%20industrial%2c%20inc-crop-u7145503.jpg?crc=4289737986" id="u714550_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="11" id="u714885" role="tab" tabindex="-1" aria-selected="false" aria-controls="u714859" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="11" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/261%20advertising_image_-crop-u7148853.jpg?crc=4267440180" id="u714885_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="13" id="u33255" role="tab" tabindex="-1" aria-selected="false" aria-controls="u33249" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="13" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/33%20advertising%20_photographer_teraoka-crop-u332553.jpg?crc=3969057297" id="u33255_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="15" id="u33295" role="tab" tabindex="-1" aria-selected="false" aria-controls="u33289" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="15" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/33%20advertising%20_photographer_teraoka-crop-u332953.jpg?crc=3969057297" id="u33295_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="17" id="u33335" role="tab" tabindex="-1" aria-selected="false" aria-controls="u33329" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="17" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/35%20advertising_image_cyan_z-series-crop-u333353.jpg?crc=4182261463" id="u33335_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="19" id="u33375" role="tab" tabindex="-1" aria-selected="false" aria-controls="u33369" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="19" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/42%20advertising_image_mary%20alexander-crop-u333753.jpg?crc=3763218323" id="u33375_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="21" id="u33415" role="tab" tabindex="-1" aria-selected="false" aria-controls="u33409" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="21" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/51%20advertising_image_gwilliam-ivary-chiosso-cavalli---brewer-crop-u334153.jpg?crc=145888234" id="u33415_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="23" id="u33455" role="tab" tabindex="-1" aria-selected="false" aria-controls="u33449" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="23" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/53%20advertising_image_-crop-u334553.jpg?crc=3944583675" id="u33455_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="25" id="u691473" role="tab" tabindex="-1" aria-selected="false" aria-controls="u691451" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="25" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/62alto%20litigation%2c%20pc-crop-u6914733.jpg?crc=456493906" id="u691473_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="27" id="u691793" role="tab" tabindex="-1" aria-selected="false" aria-controls="u691775" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="27" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/67advertising_image_abramson-smith-waldsmith%2c%20llp%2c-crop-u6917933.jpg?crc=497230188" id="u691793_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="29" id="u691921" role="tab" tabindex="-1" aria-selected="false" aria-controls="u691903" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="29" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/71%20advertising%20product%20photographer_teresonic-crop-u6919213.jpg?crc=305746712" id="u691921_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
</div>
<div class="SSSlideLink clip_frame colelem" data-col-pos="31" id="u715101" role="tab" tabindex="-1" aria-selected="false" aria-controls="u715075" style="height: 21px;"><!-- image -->
  <img class="block" data-col-pos="31" alt="" data-heightwidthratio="0.8461538461538461" data-image-width="26" data-image-height="22" src="images/8-crop-u7151013.jpg?crc=177226809" id="u715101_img" data-widget-id="slideshowu32805" style="height: 21.1538px;">
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

# result

<img class="mini-image" alt=""    src="images/11%20advertising_photographer_%20san%20francisco-crop-u328132.jpg" id="u32813_img"  >
<img class="mini-image" alt=""    src="images/12%20advertising_photography-crop-u330752.jpg" id="u33075_img"  >
<img class="mini-image" alt=""    src="images/13%20advertising_image_danko%20law%20firm-crop-u330953.jpg" id="u33095_img"  >
<img class="mini-image" alt=""    src="images/14%20advertising_image_fuse%20arct-crop-u331153.jpg" id="u33115_img"  >
<img class="mini-image" alt=""    src="images/21%20advertising_image%20_abramson-smith-waldsmith%20%2c%20llp%2c-crop-u331353.jpg" id="u33135_img"  >
<img class="mini-image" alt=""    src="images/22advertising_image%20_abramson-smith-waldsmith%20%2c-llp%2c-crop-u331553.jpg" id="u33155_img"  >
<img class="mini-image" alt=""    src="images/23advertising_image%20_abramson-smith-waldsmith%20%2c-llp%2c-crop-u331753.jpg" id="u33175_img"  >
<img class="mini-image" alt=""    src="images/24advertising_image%20_abramson-smith-waldsmith%2c-llp%2c-crop-u331953.jpg" id="u33195_img"  >
<img class="mini-image" alt=""    src="images/241advertising_image_abramson-smith-waldsmith%2c%20llp%2c-crop-u332153.jpg" id="u33215_img"  >
<img class="mini-image" alt=""    src="images/251fm%20industrial%2c%20inc-crop-u7145503.jpg" id="u714550_img"  >
<img class="mini-image" alt=""    src="images/252industrial_photographer_fm%20industrial%2c%20inc-crop-u7146253.jpg" id="u714625_img"  >
<img class="mini-image" alt=""    src="images/261%20advertising_image_-crop-u7148853.jpg" id="u714885_img"  >
<img class="mini-image" alt=""    src="images/262_advertising%20photographer_fight%20night-crop-u7150133.jpg" id="u715013_img"  >
<img class="mini-image" alt=""    src="images/33%20advertising%20_photographer_teraoka-crop-u332553.jpg" id="u33255_img"  >
<img class="mini-image" alt=""    src="images/32%20advertising%20_image_teraoka-crop-u332753.jpg" id="u33275_img"  >
<img class="mini-image" alt=""    src="images/33%20advertising%20_photographer_teraoka-crop-u332953.jpg" id="u33295_img"  >
<img class="mini-image" alt=""    src="images/34%20advertising_image_cyan_lab-crop-u333153.jpg" id="u33315_img"  >
<img class="mini-image" alt=""    src="images/35%20advertising_image_cyan_z-series-crop-u333353.jpg" id="u33335_img"  >
<img class="mini-image" alt=""    src="images/41%20advertising_image_mary%20alexander-crop-u333553.jpg" id="u33355_img"  >
<img class="mini-image" alt=""    src="images/42%20advertising_image_mary%20alexander-crop-u333753.jpg" id="u33375_img"  >
<img class="mini-image" alt=""    src="images/43%20advertising_image_pinta%20acoustic-crop-u333953.jpg" id="u33395_img"  >
<img class="mini-image" alt=""    src="images/51%20advertising_image_gwilliam-ivary-chiosso-cavalli---brewer-crop-u334153.jpg" id="u33415_img"  >
<img class="mini-image" alt=""    src="images/52%20advertising_image_hartog-baer-hand-crop-u334353.jpg" id="u33435_img"  >
<img class="mini-image" alt=""    src="images/53%20advertising_image_-crop-u334553.jpg" id="u33455_img"  >
<img class="mini-image" alt=""    src="images/61%20advertising%20corporate%20photographer-crop-u6912733.jpg" id="u691273_img"  >
<img class="mini-image" alt=""    src="images/62alto%20litigation%2c%20pc-crop-u6914733.jpg" id="u691473_img"  >
<img class="mini-image" alt=""    src="images/65%20minami%20tamaki%20llp-crop-u6917293.jpg" id="u691729_img"  >
<img class="mini-image" alt=""    src="images/67advertising_image_abramson-smith-waldsmith%2c%20llp%2c-crop-u6917933.jpg" id="u691793_img"  >
<img class="mini-image" alt=""    src="images/68%20advertising%20photograhy_winer%2c%20burritt%20-%20tillis%20llp-crop-u7067003.jpg" id="u706700_img"  >
<img class="mini-image" alt=""    src="images/71%20advertising%20product%20photographer_teresonic-crop-u6919213.jpg" id="u691921_img"  >
<img class="mini-image" alt=""    src="images/7advertising%20product%20photographer_seta%20di%20gioia-crop-u6919853.jpg" id="u691985_img"  >
<img class="mini-image" alt=""    src="images/8-crop-u7151013.jpg" id="u715101_img"  >