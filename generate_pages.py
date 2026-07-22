# -*- coding: utf-8 -*-
import os

categories = [
    {"id": "drones", "title": "Drones 無人機終極挑戰賽", "icon": "🚁", "link": "https://www.he-ro.gr/"},
    {"id": "football", "title": "Football 機械人足球賽", "icon": "⚽", "link": "https://www.he-ro.gr/"},
    {"id": "wrestling", "title": "1kg Wrestling 1kg擂台賽", "icon": "🤼", "link": "https://www.he-ro.gr/"},
    {"id": "rally", "title": "Rally 拉力賽", "icon": "🏎️", "link": "https://www.he-ro.gr/"},
    {"id": "marathon", "title": "Marathon 馬拉松賽跑", "icon": "🏃", "link": "https://www.he-ro.gr/"},
    {"id": "exhibition", "title": "Exhibition 機械人展覽賽", "icon": "💡", "link": "https://www.he-ro.gr/"},
    {"id": "relay-race", "title": "Relay Race 接力賽", "icon": "🤝", "link": "https://www.he-ro.gr/"},
    {"id": "obstacle-race", "title": "Obstacle Race 障礙賽", "icon": "🚧", "link": "https://www.he-ro.gr/"}
]

template = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - MRC Taiwan</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../style.css">
</head>
<body>
    <nav id="navbar">
        <div class="nav-container">
            <a href="../index.html" class="brand-logo">
                <div class="logo-box">
                    <div class="logo-icon">🤖</div>
                    <div class="logo-text-main">MRC TAIWAN</div>
                    <div class="logo-text-sub">Minoan Robotsports Competition</div>
                </div>
            </a>
            <ul class="nav-links">
                <li><a href="../index.html">返回首頁</a></li>
                <li><a href="{link}" target="_blank" class="global-link" title="Visit Original Rules">🔗 希臘官網原始規則</a></li>
            </ul>
        </div>
    </nav>

    <header class="hero" style="height: 40vh; min-height: 300px;">
        <div class="hero-overlay"></div>
        <div class="hero-content">
            <div style="font-size: 4rem; margin-bottom: 20px;">{icon}</div>
            <h1 class="fade-in">{title}</h1>
        </div>
    </header>

    <section class="section">
        <div class="container glass" style="padding: 40px; margin-top: -50px; position: relative; z-index: 10;">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 20px; margin-bottom: 30px;">
                <h2>賽事規則中文說明</h2>
                <a href="{link}" target="_blank" class="btn-primary btn-small">🌐 查看希臘官方英文規則</a>
            </div>
            
            <div class="rules-content" style="min-height: 300px; color: var(--text-muted); line-height: 1.8;">
                <p>【系統提示】此處尚未填寫中文翻譯規則。請管理員後續將希臘官方網站之對應賽事規則翻譯後，張貼於此處。</p>
                <br>
                <h3>競賽概要 (Placeholder)</h3>
                <p>本項目考驗參賽隊伍在特定環境下的機器人設計、程式編寫與團隊合作能力...</p>
                <br>
                <h3>計分方式 (Placeholder)</h3>
                <p>請參閱希臘官方原始網頁之最新計分標準為主。</p>
            </div>
        </div>
    </section>

    <footer>
        <div class="footer-bottom">
            <p>&copy; 2026 MRC Taiwan. All rights reserved.</p>
        </div>
    </footer>
    <script src="../script.js"></script>
</body>
</html>
"""

try:
    os.makedirs('rules')
except OSError:
    pass

for cat in categories:
    content = template.format(
        title=cat["title"],
        icon=cat["icon"],
        link=cat["link"]
    )
    filename = 'rules/' + cat["id"] + '.html'
    import io
    with io.open(filename, 'w', encoding='utf-8') as f:
        f.write(content.decode('utf-8'))

print("Generated HTML files for categories.")
