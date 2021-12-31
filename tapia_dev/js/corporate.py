import re

data = '''<!-- stack box -->
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="0" id="u4462" role="tabpanel" aria-labelledby="u4455" style="height: 621px; display: none;"><!-- image -->
<img class="block" data-col-pos="0" data-src="images/11%20corporate_group_grube-brown---geidt-llp954x636.jpg?crc=3921921988" src="images/11%20corporate_group_grube-brown---geidt-llp954x636.jpg?crc=3921921988" alt="Corporate Group Image" title="Corporate Group Image" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u4462_img" data-widget-id="slideshowu4449" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="1" id="u4711" role="tabpanel" aria-labelledby="u4717" style="height: 621px; display: none;"><!-- image -->
<img class="block" data-col-pos="1" data-src="images/12-corporate_portrait_delacey-riebel-family-law954x636.jpg?crc=6128218" src="images/12-corporate_portrait_delacey-riebel-family-law954x636.jpg?crc=6128218" alt="Corporate portrait for Magdalena Law-Group" title="Corporate portrait for Magdalena Law-Group" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u4711_img" data-widget-id="slideshowu4449" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="2" id="u4731" role="tabpanel" aria-labelledby="u4737" style="height: 621px; display: none;"><!-- image -->
<img class="block" data-col-pos="2" data-src="images/13%20corporate_portrait_scott-a-freedman-of-zacks---freedman%2c-pc954x636.jpg?crc=62356682" src="images/13%20corporate_portrait_scott-a-freedman-of-zacks---freedman%2c-pc954x636.jpg?crc=62356682" alt="Corporate portrait_Scott A. Freedman of Zacks &amp; Freedman, PC" title="Corporate portrait_Scott A. Freedman of Zacks &amp; Freedman, PC" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u4731_img" data-widget-id="slideshowu4449" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="3" id="u4751" role="tabpanel" aria-labelledby="u4757" style="height: 621px; display: none;"><!-- image -->
<img class="block" data-col-pos="3" data-src="images/14%20corporate_portrait_lorber-greenfield---polito-llp954x636.jpg?crc=328374142" src="images/14%20corporate_portrait_lorber-greenfield---polito-llp954x636.jpg?crc=328374142" alt="Corporate portrait _ L orber Greenfield &amp; Polito- LP" title="Corporate portrait _ L orber Greenfield &amp; Polito- LP" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u4751_img" data-widget-id="slideshowu4449" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="4" id="u496271" role="tabpanel" aria-labelledby="u496293" style="height: 621px; display: none;"><!-- image -->
<img class="block" data-col-pos="4" data-src="images/141%20corporate_group_bogaards%20law-crop-u4962713.jpg?crc=511919192" src="images/141%20corporate_group_bogaards%20law-crop-u4962713.jpg?crc=511919192" alt="Corporate portrait _ L orber Greenfield &amp; Polito- LP" title="Corporate portrait _ L orber Greenfield &amp; Polito- LP" data-heightwidthratio="0.6666666666666666" data-image-width="954" data-image-height="636" id="u496271_img" data-widget-id="slideshowu4449" style="height: 621.333px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="5" id="u496347" role="tabpanel" aria-labelledby="u496369" style="height: 621px; display: none;"><!-- image -->
<img class="block" data-col-pos="5" data-src="images/151corporate_group_alto%20litigation954x636.jpg?crc=3943335210" src="images/151corporate_group_alto%20litigation954x636.jpg?crc=3943335210" alt="Corporate portrait _ L orber Greenfield &amp; Polito- LP" title="Corporate portrait _ L orber Greenfield &amp; Polito- LP" data-heightwidthratio="0.6666666666666666" data-image-width="954" data-image-height="636" id="u496347_img" data-widget-id="slideshowu4449" style="height: 621.333px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="6" id="u4771" role="tabpanel" aria-labelledby="u4777" style="height: 621px; display: none;"><!-- image -->
<img class="block" data-col-pos="6" data-src="images/15_corporate_group_image_teraoka%20-%20partners954x636.jpg?crc=3803976806" src="images/15_corporate_group_image_teraoka%20-%20partners954x636.jpg?crc=3803976806" alt="Corporate group&nbsp; image _ Teraoka &amp; Partners" title="Corporate group&nbsp; image _ Teraoka &amp; Partners" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u4771_img" data-widget-id="slideshowu4449" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel wp-panel-active" data-col-pos="7" id="u496423" role="tabpanel" aria-labelledby="u496445" style="height: 621px;"><!-- image -->
<img class="block" data-col-pos="7" data-src="images/16%20corporate_group_hartog%20i%20baer%20i%20hand954x636.jpg?crc=4078468072" src="images/16%20corporate_group_hartog%20i%20baer%20i%20hand954x636.jpg?crc=4078468072" alt="Corporate group&nbsp; image _ Teraoka &amp; Partners" title="Corporate group&nbsp; image _ Teraoka &amp; Partners" data-heightwidthratio="0.6666666666666666" data-image-width="954" data-image-height="636" id="u496423_img" data-widget-id="slideshowu4449" style="height: 621.333px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="8" id="u4811" role="tabpanel" aria-labelledby="u4817" style="height: 621px; display: none;"><!-- image -->
<img class="block" data-col-pos="8" data-src="images/17%20corporate_portrait_mary-alexander954x636.jpg?crc=4220554184" src="images/17%20corporate_portrait_mary-alexander954x636.jpg?crc=4220554184" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u4811_img" data-widget-id="slideshowu4449" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="9" id="u4831" role="tabpanel" aria-labelledby="u4837" style="height: 621px; display: none;"><!-- image -->
<img class="block" data-col-pos="9" data-src="images/18%20corporate_working_image954x636.jpg?crc=314521601" src="images/18%20corporate_working_image954x636.jpg?crc=314521601" alt="&nbsp;Corporate working group image" title="&nbsp;Corporate working group image" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u4831_img" data-widget-id="slideshowu4449" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="10" id="u4851" role="tabpanel" aria-labelledby="u4857" style="height: 621px; display: none;"><!-- image -->
<img class="block" data-col-pos="10" data-src="images/19%20corporate_group954x636.jpg?crc=291075105" src="images/19%20corporate_group954x636.jpg?crc=291075105" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u4851_img" data-widget-id="slideshowu4449" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="11" id="u4871" role="tabpanel" aria-labelledby="u4877" style="height: 621px; display: none;"><!-- image -->
<img class="block" data-col-pos="11" data-src="images/21%20corporate%20_portrait-richard%20sideman954x6362.jpg?crc=3770834640" src="images/21%20corporate%20_portrait-richard%20sideman954x6362.jpg?crc=3770834640" alt="Corporate headshot _ Richard Sideman" title="Corporate headshot _ Richard Sideman" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u4871_img" data-widget-id="slideshowu4449" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="12" id="u4891" role="tabpanel" aria-labelledby="u4897" style="height: 621px; display: none;"><!-- image -->
<img class="block" data-col-pos="12" data-src="images/22%20corporate_group_simon%20-%20bancroft%20-%20wired%20magazine%20954x636.jpg?crc=4057574288" src="images/22%20corporate_group_simon%20-%20bancroft%20-%20wired%20magazine%20954x636.jpg?crc=4057574288" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u4891_img" data-widget-id="slideshowu4449" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="13" id="u4911" role="tabpanel" aria-labelledby="u4917" style="height: 621px; display: none;"><!-- image -->
<img class="block" data-col-pos="13" data-src="images/23%20corporate_group_%20image_gwilliam%2c%20ivary%2c%20chiosso954x636.jpg?crc=3811881605" src="images/23%20corporate_group_%20image_gwilliam%2c%20ivary%2c%20chiosso954x636.jpg?crc=3811881605" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u4911_img" data-widget-id="slideshowu4449" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="14" id="u4931" role="tabpanel" aria-labelledby="u4937" style="height: 621px; display: none;"><!-- image -->
<img class="block" data-col-pos="14" data-src="images/24%20corporate%20_portrait-954x636.jpg?crc=4086300449" src="images/24%20corporate%20_portrait-954x636.jpg?crc=4086300449" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u4931_img" data-widget-id="slideshowu4449" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="15" id="u4951" role="tabpanel" aria-labelledby="u4957" style="height: 621px; display: none;"><!-- image -->
<img class="block" data-col-pos="15" data-src="images/25%20corporate_image954x636.jpg?crc=372766508" src="images/25%20corporate_image954x636.jpg?crc=372766508" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u4951_img" data-widget-id="slideshowu4449" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="16" id="u4971" role="tabpanel" aria-labelledby="u4977" style="height: 621px; display: none;"><!-- image -->
<img class="block" data-col-pos="16" data-src="images/26%20corporate-group-image_kerr---wagstaffe954x636.jpg?crc=4016923593" src="images/26%20corporate-group-image_kerr---wagstaffe954x636.jpg?crc=4016923593" alt="Corporate Group image _ Kerr &amp; Wagstaffe" title="Corporate Group Image" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u4971_img" data-widget-id="slideshowu4449" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="17" id="u4991" role="tabpanel" aria-labelledby="u4997" style="height: 621px; display: none;"><!-- image -->
<img class="block" data-col-pos="17" data-src="images/27%20corporate_safeway%20general_counsel-robert%20gordon954x636.jpg?crc=3783305172" src="images/27%20corporate_safeway%20general_counsel-robert%20gordon954x636.jpg?crc=3783305172" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u4991_img" data-widget-id="slideshowu4449" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="18" id="u5011" role="tabpanel" aria-labelledby="u5017" style="height: 621px; display: none;"><!-- image -->
<img class="block" data-col-pos="18" data-src="images/27%20corporate_working_group954x636.jpg?crc=238653474" src="images/27%20corporate_working_group954x636.jpg?crc=238653474" alt="Corporate working group image" title="Corporate working group image" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u5011_img" data-widget-id="slideshowu4449" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="19" id="u5031" role="tabpanel" aria-labelledby="u5037" style="height: 621px; display: none;"><!-- image -->
<img class="block" data-col-pos="19" data-src="images/28%20corporate_ceo%20of%20kaiser%20permanente%20_health%20plan%20of%20san%20francisco_blue%20shield%20of%20ca954x636.jpg?crc=271763014" src="images/28%20corporate_ceo%20of%20kaiser%20permanente%20_health%20plan%20of%20san%20francisco_blue%20shield%20of%20ca954x636.jpg?crc=271763014" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u5031_img" data-widget-id="slideshowu4449" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="20" id="u496513" role="tabpanel" aria-labelledby="u496535" style="height: 621px; display: none;"><!-- image -->
<img class="block" data-col-pos="20" data-src="images/37%20corporate_group-robert%20w%20wood%20pc954x636.jpg?crc=112651019" src="images/37%20corporate_group-robert%20w%20wood%20pc954x636.jpg?crc=112651019" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u496513_img" data-widget-id="slideshowu4449" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="21" id="u496581" role="tabpanel" aria-labelledby="u496599" style="height: 621px; display: none;"><!-- image -->
<img class="block" data-col-pos="21" data-src="images/38%20corporate-group_venardi%20zurada%20llp954x636.jpg?crc=3872475850" src="images/38%20corporate-group_venardi%20zurada%20llp954x636.jpg?crc=3872475850" alt="" data-heightwidthratio="0.6666666666666666" data-image-width="954" data-image-height="636" id="u496581_img" data-widget-id="slideshowu4449" style="height: 621.333px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="22" id="u496645" role="tabpanel" aria-labelledby="u496663" style="height: 621px; display: none;"><!-- image -->
<img class="block" data-col-pos="22" data-src="images/39%20corporate_working_william%20blair954x636.jpg?crc=10095165" src="images/39%20corporate_working_william%20blair954x636.jpg?crc=10095165" alt="" data-heightwidthratio="0.6666666666666666" data-image-width="954" data-image-height="636" id="u496645_img" data-widget-id="slideshowu4449" style="height: 621.333px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="23" id="u5051" role="tabpanel" aria-labelledby="u5057" style="height: 621px; display: none;"><!-- image -->
<img class="block" data-col-pos="23" data-src="images/31%20corporate_working_image954x636.jpg?crc=3988086871" src="images/31%20corporate_working_image954x636.jpg?crc=3988086871" alt="Corporate working group image" title="Corporate working group image" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u5051_img" data-widget-id="slideshowu4449" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="24" id="u5071" role="tabpanel" aria-labelledby="u5077" style="height: 621px; display: none;"><!-- image -->
<img class="block" data-col-pos="24" data-src="images/32%20corporate%20working%20image954x636.jpg?crc=4129960336" src="images/32%20corporate%20working%20image954x636.jpg?crc=4129960336" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u5071_img" data-widget-id="slideshowu4449" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="25" id="u5091" role="tabpanel" aria-labelledby="u5097" style="height: 621px; display: none;"><!-- image -->
<img class="block" data-col-pos="25" data-src="images/33%20corporate%20working_william%20blair954x636.jpg?crc=4255888367" src="images/33%20corporate%20working_william%20blair954x636.jpg?crc=4255888367" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u5091_img" data-widget-id="slideshowu4449" style="height: 621.318px;">
</div>
<div class="SSSlide clip_frame grpelem wp-panel" data-col-pos="26" id="u5111" role="tabpanel" aria-labelledby="u5117" style="height: 621px; display: none;"><!-- image -->
<img class="block" data-col-pos="26" data-src="images/34%20corporate-image_federal-deposit-insurance-corp-954x636.jpg?crc=4116195291" src="images/34%20corporate-image_federal-deposit-insurance-corp-954x636.jpg?crc=4116195291" alt="" data-heightwidthratio="0.6673662119622246" data-image-width="953" data-image-height="636" id="u5111_img" data-widget-id="slideshowu4449" style="height: 621.318px;">
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

<img    src="images/11%20corporate_group_grube-brown---geidt-llp954x636.jpg" alt="Corporate Group Image" title="Corporate Group Image"    id="u4462_img"  >
<img    src="images/12-corporate_portrait_delacey-riebel-family-law954x636.jpg" alt="Corporate portrait for Magdalena Law-Group" title="Corporate portrait for Magdalena Law-Group"    id="u4711_img"  >
<img    src="images/13%20corporate_portrait_scott-a-freedman-of-zacks---freedman%2c-pc954x636.jpg" alt="Corporate portrait_Scott A. Freedman of Zacks &amp; Freedman, PC" title="Corporate portrait_Scott A. Freedman of Zacks &amp; Freedman, PC"    id="u4731_img"  >
<img    src="images/14%20corporate_portrait_lorber-greenfield---polito-llp954x636.jpg" alt="Corporate portrait _ L orber Greenfield &amp; Polito- LP" title="Corporate portrait _ L orber Greenfield &amp; Polito- LP"    id="u4751_img"  >
<img    src="images/141%20corporate_group_bogaards%20law-crop-u4962713.jpg" alt="Corporate portrait _ L orber Greenfield &amp; Polito- LP" title="Corporate portrait _ L orber Greenfield &amp; Polito- LP"    id="u496271_img"  >
<img    src="images/151corporate_group_alto%20litigation954x636.jpg" alt="Corporate portrait _ L orber Greenfield &amp; Polito- LP" title="Corporate portrait _ L orber Greenfield &amp; Polito- LP"    id="u496347_img"  >
<img    src="images/15_corporate_group_image_teraoka%20-%20partners954x636.jpg" alt="Corporate group&nbsp; image _ Teraoka &amp; Partners" title="Corporate group&nbsp; image _ Teraoka &amp; Partners"    id="u4771_img"  >
<img    src="images/16%20corporate_group_hartog%20i%20baer%20i%20hand954x636.jpg" alt="Corporate group&nbsp; image _ Teraoka &amp; Partners" title="Corporate group&nbsp; image _ Teraoka &amp; Partners"    id="u496423_img"  >
<img    src="images/17%20corporate_portrait_mary-alexander954x636.jpg" alt=""    id="u4811_img"  >
<img    src="images/18%20corporate_working_image954x636.jpg" alt="&nbsp;Corporate working group image" title="&nbsp;Corporate working group image"    id="u4831_img"  >
<img    src="images/19%20corporate_group954x636.jpg" alt=""    id="u4851_img"  >
<img    src="images/21%20corporate%20_portrait-richard%20sideman954x6362.jpg" alt="Corporate headshot _ Richard Sideman" title="Corporate headshot _ Richard Sideman"    id="u4871_img"  >
<img    src="images/22%20corporate_group_simon%20-%20bancroft%20-%20wired%20magazine%20954x636.jpg" alt=""    id="u4891_img"  >
<img    src="images/23%20corporate_group_%20image_gwilliam%2c%20ivary%2c%20chiosso954x636.jpg" alt=""    id="u4911_img"  >
<img    src="images/24%20corporate%20_portrait-954x636.jpg" alt=""    id="u4931_img"  >
<img    src="images/25%20corporate_image954x636.jpg" alt=""    id="u4951_img"  >
<img    src="images/26%20corporate-group-image_kerr---wagstaffe954x636.jpg" alt="Corporate Group image _ Kerr &amp; Wagstaffe" title="Corporate Group Image"    id="u4971_img"  >
<img    src="images/27%20corporate_safeway%20general_counsel-robert%20gordon954x636.jpg" alt=""    id="u4991_img"  >
<img    src="images/27%20corporate_working_group954x636.jpg" alt="Corporate working group image" title="Corporate working group image"    id="u5011_img"  >
<img    src="images/28%20corporate_ceo%20of%20kaiser%20permanente%20_health%20plan%20of%20san%20francisco_blue%20shield%20of%20ca954x636.jpg" alt=""    id="u5031_img"  >
<img    src="images/37%20corporate_group-robert%20w%20wood%20pc954x636.jpg" alt=""    id="u496513_img"  >
<img    src="images/38%20corporate-group_venardi%20zurada%20llp954x636.jpg" alt=""    id="u496581_img"  >
<img    src="images/39%20corporate_working_william%20blair954x636.jpg" alt=""    id="u496645_img"  >
<img    src="images/31%20corporate_working_image954x636.jpg" alt="Corporate working group image" title="Corporate working group image"    id="u5051_img"  >
<img    src="images/32%20corporate%20working%20image954x636.jpg" alt=""    id="u5071_img"  >
<img    src="images/33%20corporate%20working_william%20blair954x636.jpg" alt=""    id="u5091_img"  >
<img    src="images/34%20corporate-image_federal-deposit-insurance-corp-954x636.jpg" alt=""    id="u5111_img"  >