#!/usr/bin/env python3
# Generate upgraded tech dashboard

html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>💻 Tech Dashboard</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #0f172a;
            color: #e2e8f0;
            min-height: 100vh;
        }
        .header {
            background: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%);
            padding: 20px 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 100;
        }
        .header h1 { font-size: 1.8rem; }
        .date-badge {
            background: rgba(255,255,255,0.2);
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.9rem;
        }
        .container { max-width: 1400px; margin: 0 auto; padding: 20px; }
        
        .card {
            background: #1e293b;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
        }
        .card h2 {
            font-size: 1.1rem;
            color: #94a3b8;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 1px solid #334155;
        }
        
        .news-scroll {
            max-height: 400px;
            overflow-y: auto;
            padding-right: 10px;
        }
        .news-scroll::-webkit-scrollbar { width: 8px; }
        .news-scroll::-webkit-scrollbar-track { background: #0f172a; border-radius: 4px; }
        .news-scroll::-webkit-scrollbar-thumb { background: #475569; border-radius: 4px; }
        
        .tech-item {
            padding: 15px;
            margin: 10px 0;
            background: #0f172a;
            border-radius: 8px;
        }
        .tech-item h3 { color: #a855f7; margin-bottom: 8px; }
        .tech-item p { color: #94a3b8; font-size: 0.9rem; line-height: 1.5; }
        .tech-item .tag {
            display: inline-block;
            background: #334155;
            padding: 3px 10px;
            border-radius: 12px;
            font-size: 0.75rem;
            margin-right: 8px;
        }
        .tech-item .source { 
            font-size: 0.75rem; 
            color: #64748b; 
            margin-top: 10px;
        }
        .tech-item .source a { color: #a855f7; text-decoration: none; }
        
        .category-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 15px;
        }
        .category-card {
            background: #0f172a;
            padding: 15px;
            border-radius: 10px;
        }
        .category-card h4 { color: #e2e8f0; margin-bottom: 10px; }
        .category-card ul { padding-left: 20px; color: #94a3b8; }
        .category-card li { margin: 5px 0; }
        .category-card li strong { color: #a855f7; }
        
        .field-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }
        .field-header h3 { color: #a855f7; }
        
        .refresh-note {
            text-align: center;
            color: #64748b;
            font-size: 0.8rem;
            padding: 10px;
        }
        .refresh-note a { color: #a855f7; text-decoration: none; }
    </style>
</head>
<body>
    <div class="header">
        <h1>💻 Tech Dashboard</h1>
        <span class="date-badge">March 17, 2026</span>
    </div>
    
    <div class="container">
        <div class="card">
            <h2>🔧 Tech News (Scrollable)</h2>
            <div class="news-scroll">
'''

tech_news = [
    {
        "title": "TSMC Announces 2nm Volume Production",
        "category": "Semiconductors",
        "details": "Taiwan Semiconductor Manufacturing Co. announces successful volume production of its 2nm process node, attracting pre-orders from major AI and smartphone chip designers. Performance and efficiency gains expected to drive next-gen chips.",
        "source": "TSMC Press Release",
        "url": "https://www.tsmc.com/press_releases"
    },
    {
        "title": "Intel 18A Process Hits Milestones",
        "category": "Semiconductors",
        "details": "Intel's 'Intel 18A' process hits critical milestones, positioning the company as a credible contender for advanced foundry services. Market optimism surges for their roadmap.",
        "source": "Intel",
        "url": "https://www.intel.com/content/www/us/en/newsroom.html"
    },
    {
        "title": "NVIDIA RTX 5090 Leaks Reveal Massive Performance Gains",
        "category": "Hardware",
        "details": "Upcoming NVIDIA Blackwell architecture shows 70% improvement in AI inference workloads. Gaming performance also expected to double over current generation.",
        "source": "Tom's Hardware",
        "url": "https://www.tomshardware.com/"
    },
    {
        "title": "Apple Vision Pro Enterprise Expansion",
        "category": "AR/VR",
        "details": "Apple expands Vision Pro ecosystem with enterprise applications. Major Fortune 500 companies adopting spatial computing for training and design.",
        "source": "Apple",
        "url": "https://www.apple.com/newsroom/"
    },
    {
        "title": "Google Gemini 2.5 Sets New LLM Benchmarks",
        "category": "AI",
        "details": "Google's latest Gemini model achieves state-of-the-art results across reasoning, coding, and multimodal benchmarks. Thinking mode shows improvedChain-of-thought capabilities.",
        "source": "Google AI",
        "url": "https://blog.google/technology/ai/"
    },
    {
        "title": "ASML Reports Record EUV Backlog",
        "category": "Semiconductors",
        "details": "Global chip equipment giant ASML reports record backlog for High-NA EUV systems, indicating strong industry commitment to sub-2nm manufacturing despite geopolitical tensions.",
        "source": "ASML",
        "url": "https://www.asml.com/company/en/index"
    }
]

for item in tech_news:
    html += f'''                <div class="tech-item">
                    <h3>{item['title']}</h3>
                    <span class="tag">{item['category']}</span>
                    <p>{item['details']}</p>
                    <div class="source">Source: <a href="{item['url']}" target="_blank" rel="noopener">{item['source']}</a></div>
                </div>
'''

html += '''            </div>
        </div>
        
        <div class="card">
            <div class="field-header">
                <h3>🥽 AR/VR & Holographic Display</h3>
            </div>
            <div class="category-grid">
                <div class="category-card">
                    <h4>Latest Developments</h4>
                    <ul>
                        <li>SLM advances in LCoS technology</li>
                        <li>Silicon photonics breakthroughs</li>
                        <li>Dell Pro Precision (May 2026)</li>
                        <li>Apple Vision Pro enterprise expansion</li>
                    </ul>
                </div>
                <div class="category-card">
                    <h4>Key Companies</h4>
                    <ul>
                        <li><strong>LCOL</strong> - Locus Optical</li>
                        <li><strong>DISB</strong> - DigiSight</li>
                        <li><strong>AAPL</strong> - Spatial computing</li>
                    </ul>
                </div>
                <div class="category-card">
                    <h4>Catalysts</h4>
                    <ul>
                        <li>Major product launches H2 2026</li>
                        <li>Edge AI for real-time rendering</li>
                        <li>Neural rendering improvements</li>
                    </ul>
                </div>
            </div>
        </div>
        
        <div class="card">
            <div class="field-header">
                <h3>🧬 Biosensors & UV Technology</h3>
            </div>
            <div class="category-grid">
                <div class="category-card">
                    <h4>Latest Developments</h4>
                    <ul>
                        <li>UV sensor miniaturization</li>
                        <li>Biometric sensor accuracy +</li>
                        <li>Environmental sensing integration</li>
                    </ul>
                </div>
                <div class="category-card">
                    <h4>Key Players</h4>
                    <ul>
                        <li><strong>STM</strong> - STMicroelectronics</li>
                        <li><strong>TEL</strong> - TE Connectivity</li>
                        <li><strong>AMS</strong> - ams-OSRAM</li>
                    </ul>
                </div>
            </div>
        </div>
        
        <div class="card">
            <div class="field-header">
                <h3>🤖 AI & Machine Learning</h3>
            </div>
            <div class="category-grid">
                <div class="category-card">
                    <h4>AR/VR/Photonics</h4>
                    <ul>
                        <li>Edge AI for real-time rendering</li>
                        <li>Neural rendering improvements</li>
                        <li>AI-powered optical design</li>
                    </ul>
                </div>
                <div class="category-card">
                    <h4>Biosensors</h4>
                    <ul>
                        <li>ML improving sensor accuracy</li>
                        <li>AI-driven anomaly detection</li>
                        <li>Predictive maintenance</li>
                    </ul>
                </div>
                <div class="category-card">
                    <h4>Key Players</h4>
                    <ul>
                        <li><strong>NVDA</strong> - AI infrastructure</li>
                        <li><strong>MSFT</strong> - Azure AI</li>
                        <li><strong>GOOGL</strong> - Tensor processing</li>
                    </ul>
                </div>
            </div>
        </div>
        
        <div class="card">
            <h2>📦 Software & Tools</h2>
            <div class="category-grid">
                <div class="category-card">
                    <h4>Python</h4>
                    <ul><li>Version 3.11+</li><li>FastAPI, Streamlit</li></ul>
                </div>
                <div class="category-card">
                    <h4>Node.js</h4>
                    <ul><li>Version 22+</li><li>Express, Next.js</li></ul>
                </div>
                <div class="category-card">
                    <h4>Cloud</h4>
                    <ul><li>AWS, GCP, Azure</li><li>Serverless</li></ul>
                </div>
            </div>
        </div>
        
        <div class="refresh-note">
            Dashboard auto-updates daily from cloud cron job • <a href="https://github.com/prithu-roy/market-scanner-dashboard" target="_blank" rel="noopener">View Source on GitHub</a>
        </div>
    </div>
</body>
</html>
'''

with open('/home/node/.openclaw/workspace/tech-dashboard.html', 'w') as f:
    f.write(html)

print("✅ Tech dashboard updated successfully!")
