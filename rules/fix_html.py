# -*- coding: utf-8 -*-
import io

configs = {
    'mrc-soccer.html': {
        'title': u'MRC SOCCER (機器人足球賽)',
        'hero_title': u'MRC SOCCER (機器人足球賽)',
        'img_src': u'../assets/images/mrc-soccer/image_01.webp',
        'href': u'https://www.he-ro.gr/mrc-soccer'
    },
    'mrc-weightlifting-humanoid.html': {
        'title': u'MRC WEIGHTLIFTING HUMANOID (人形機器人舉重)',
        'hero_title': u'MRC WEIGHTLIFTING HUMANOID (人形機器人舉重)',
        'img_src': u'../assets/images/mrc-weightlifting-humanoid/image_01.webp',
        'href': u'https://www.he-ro.gr/mrc-weightlifting-humanoid'
    },
    'bowling.html': {
        'title': u'BOWLING (機器人保齡球)',
        'hero_title': u'BOWLING (機器人保齡球)',
        'img_src': u'../assets/images/bowling/image_01.webp',
        'href': u'https://www.he-ro.gr/bowling'
    }
}

for filename, info in configs.items():
    with io.open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # The content currently has mangled tags. Let's do a regex replacement for the `<head>` and the hero section.
    import re
    # Fix <title>
    content = re.sub(ur'<title>.*?</title>', u'<title>{} - MRC Taiwan 賽事規則</title>'.format(info['title']), content, flags=re.DOTALL)
    
    # Fix the global link in navbar
    content = re.sub(ur'<a class="global-link" href="[^"]+".*?</a>', u'<a class="global-link" href="{}" target="_blank">🌐 查看希臘大會原文</a>'.format(info['href']), content)
    
    # Fix the hero image
    content = re.sub(ur'<div style="margin: 30px 0; text-align: center;">\s*<img src="[^"]+".*?/>\s*</div>', u'<div style="margin: 30px 0; text-align: center;">\n<img src="{}" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); display: block; margin: 0 auto;"/>\n</div>'.format(info['img_src']), content)
    
    # Fix the H1 (hero title)
    content = re.sub(ur'<h1>.*?</h1>', u'<h1>{}</h1>'.format(info['hero_title']), content, count=1)
    
    # Fix the original link
    content = re.sub(ur'<a class="original-link" href="[^"]+".*?</a>', u'<a class="original-link" href="{}" target="_blank">🔗 前往希臘官方網頁查看最新原始英文規則 (Original Rules)</a>'.format(info['href']), content)

    # Remove the bad h2 that was added
    content = re.sub(ur'<h2[^>]*>.*?</h2>', u'', content, count=1)

    with io.open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed " + filename)
