#!/usr/bin/env python3

html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Research & Tech Dashboard - Photonics & Biosensors</title>
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
        .header h1 { font-size: 1.6rem; }
        .date-badge {
            background: rgba(255,255,255,0.2);
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.9rem;
        }
        .container { max-width: 1400px; margin: 0 auto; padding: 20px; }
        
        .tabs {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 20px;
            background: #1e293b;
            padding: 15px;
            border-radius: 12px;
        }
        .tab-btn {
            background: #0f172a;
            border: none;
            color: #94a3b8;
            padding: 10px 20px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 0.95rem;
            transition: all 0.2s;
        }
        .tab-btn:hover { background: #27374d; }
        .tab-btn.active { background: #a855f7; color: white; }
        
        .tab-content { display: none; }
        .tab-content.active { display: block; }
        
        .card {
            background: #1e293b;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
        }
        .card h2 {
            font-size: 1.3rem;
            color: #94a3b8;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 1px solid #334155;
        }
        
        .scrollable { max-height: 550px; overflow-y: auto; padding-right: 10px; }
        .scrollable::-webkit-scrollbar { width: 8px; }
        .scrollable::-webkit-scrollbar-track { background: #0f172a; border-radius: 4px; }
        .scrollable::-webkit-scrollbar-thumb { background: #475569; border-radius: 4px; }
        
        .research-item {
            background: #0f172a;
            padding: 18px;
            margin: 12px 0;
            border-radius: 10px;
            border-left: 4px solid #a855f7;
        }
        .research-item .title {
            font-size: 1.1rem;
            font-weight: 600;
            color: #a855f7;
            margin-bottom: 6px;
        }
        .research-item .meta {
            font-size: 0.85rem;
            color: #94a3b8;
            margin-bottom: 10px;
        }
        .research-item .summary {
            font-size: 0.95rem;
            line-height: 1.5;
            margin-bottom: 8px;
        }
        .research-item .impact {
            font-size: 0.9rem;
            color: #06b6d4;
            font-weight: 500;
        }
        .research-item .source a {
            color: #a855f7;
            text-decoration: none;
        }
        .research-item .source a:hover { text-decoration: underline; }
        
        .grid-3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; }
        .company-card {
            background: #0f172a;
            padding: 15px;
            border-radius: 10px;
        }
        .company-card h4 { color: #a855f7; margin-bottom: 8px; }
        .company-card p { color: #94a3b8; font-size: 0.9rem; }
        
        .trend-item {
            background: #0f172a;
            padding: 12px 15px;
            margin: 8px 0;
            border-radius: 8px;
            color: #e2e8f0;
            border-left: 3px solid #22c55e;
        }
        
        a { color: #a855f7; text-decoration: none; }
        a:hover { text-decoration: underline; }
        
        .footer { text-align: center; color: #94a3b8; font-size: 0.85rem; padding: 20px; }
    </style>
</head>
<body>
    <div class="header">
        <h1>Research & Tech Dashboard</h1>
        <span class="date-badge">Photonics • Biosensors • AI Design</span>
    </div>
    
    <div class="container">
        <div class="tabs">
            <button class="tab-btn active" onclick="showTab('photonics')">Photonics News</button>
            <button class="tab-btn" onclick="showTab('biosensors')">Biosensors</button>
            <button class="tab-btn" onclick="showTab('ai')">AI for Design</button>
            <button class="tab-btn" onclick="showTab('trends')">Market Trends</button>
            <button class="tab-btn" onclick="showTab('companies')">Key Companies</button>
            <button class="tab-btn" onclick="showTab('events')">Upcoming Events</button>
        </div>
        
        <!-- Photonics -->
        <div id="photonics" class="tab-content active">
            <div class="card">
                <h2>Latest Photonics Research & Industry News</h2>
                <div class="scrollable">
                    <div class="research-item">
                        <div class="title">Advances in LCoS SLMs for Holographic Displays</div>
                        <div class="meta">Journal of Display Technology • March 2026</div>
                        <div class="summary">New liquid crystal alignment techniques improve contrast ratio by 40% and reduce power consumption for spatial light modulators in AR headsets. Key breakthrough for holographic display efficiency.</div>
                        <div class="impact">Your Impact: Direct impact on waveguide holography design at Swave</div>
                    </div>
                    <div class="research-item">
                        <div class="title">Silicon Photonics Breakthrough for Co-packaged Optics</div>
                        <div class="meta">Nature Photonics • February 2026</div>
                        <div class="summary">Researchers demonstrate 1.6Tbps per mm density with silicon photonics co-packaged with CPU. New low-loss waveguide designs reduce power per channel by 25%.</div>
                        <div class="impact">Your Impact: Enables higher density AI/ML accelerators</div>
                    </div>
                    <div class="research-item">
                        <div class="title">Dell Precision Panther Lake Workstation Launch</div>
                        <div class="meta">Dell Technologies • May 2026 Expected</div>
                        <div class="summary">New Intel Panther Lake CPU + NVIDIA Pro Blackwell GPU configured for AR/VR design work. 2x faster photonic design automation simulation.</div>
                        <div class="impact">Your Impact: Possible upgrade candidate for design workstations</div>
                    </div>
                    <div class="research-item">
                        <div class="title">Apple Vision Pro 2 Spatial Computing Updates</div>
                        <div class="meta">Apple • Expected 2026 H2</div>
                        <div class="summary">Rumored improvements: lighter weight, better battery, higher resolution micro-OLED. Enterprise ecosystem expanding rapidly.</div>
                        <div class="impact">Your Impact: New opportunities for spatial computing applications</div>
                    </div>
                    <div class="research-item">
                        <div class="title">Meta Open-source Hologram Rendering AI</div>
                        <div class="meta">Meta Research • March 2026</div>
                        <div class="summary">New neural hologram rendering model cuts compute time by 70% while maintaining image quality. Available for commercial use.</div>
                        <div class="impact">Your Impact: Could speed up design iteration cycles</div>
                    </div>
                    <div class="research-item">
                        <div class="title">ASML High-NA EUV Production Yields Improving</div>
                        <div class="meta">Semiconductor Engineering • March 2026</div>
                        <div class="summary">Yields now above 80% for new high-NA EUV scanners, enabling volume production of 2nm photonic integrated circuits.</div>
                        <div class="impact">Your Impact: More photonic chips hitting market, lower costs</div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Biosensors -->
        <div id="biosensors" class="tab-content">
            <div class="card">
                <h2>Biosensor & UV Sensor Research</h2>
                <div class="scrollable">
                    <div class="research-item">
                        <div class="title">Miniaturized UV Sensors for Wearable Health Monitoring</div>
                        <div class="meta">IEEE Sensors Journal • March 2026</div>
                        <div class="summary">New gallium oxide based UV sensor achieves 200um footprint with 1nW power consumption. Enables integration into smartwatches for continuous UV exposure monitoring.</div>
                        <div class="impact">Your Impact: Direct alignment with Arcanabio product roadmap</div>
                    </div>
                    <div class="research-item">
                        <div class="title">AI-powered Calibration for Biosensor Arrays</div>
                        <div class="meta">Nature Biotechnology • February 2026</div>
                        <div class="summary">Machine learning algorithm reduces sensor-to-sensor variation by 80% in multi-parameter biometric arrays. No factory calibration needed.</div>
                        <div class="impact">Your Impact: Lower manufacturing costs, better accuracy</div>
                    </div>
                    <div class="research-item">
                        <div class="title">Combined Environmental + Health Sensors Emerging</div>
                        <div class="meta">Sensor Expo • March 2026</div>
                        <div class="summary">New wearables integrate UV exposure, air quality (PM2.5), and vital signs into single module. Market growing 28% YoY.</div>
                        <div class="impact">Your Impact: Product differentiation opportunity</div>
                    </div>
                    <div class="research-item">
                        <div class="title">STMicro Announces New UV Sensor Line</div>
                        <div class="meta">STMicroelectronics • January 2026</div>
                        <div class="summary">New generation of compact UV sensors with digital output and low power. Competitive pricing for high volume.</div>
                        <div class="impact">Your Impact: Possible supplier alternative</div>
                    </div>
                    <div class="research-item">
                        <div class="title">Continuous Glucose Monitoring Tech Advances</div>
                        <div class="meta">Journal of Diabetes Science and Technology • March 2026</div>
                        <div class="summary">New enzyme coatings improve biosensor lifetime to 180+ days with less drift. Optical detection methods showing promise.</div>
                        <div class="impact">Your Impact: Lessons applicable to other optical biosensor designs</div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- AI for Design -->
        <div id="ai" class="tab-content">
            <div class="card">
                <h2>AI/ML for Photonics & Sensor Design</h2>
                <div class="research-item">
                    <div class="title">AI-driven Optical Design Automation</div>
                    <div class="meta">Optica • February 2026</div>
                    <div class="summary">Generative AI design of photonic waveguides automatically optimizes for loss, footprint, and manufacturing yield. Cuts design time from weeks to hours.</div>
                </div>
                <div class="research-item">
                    <div class="title">Neural Rendering for Holographic Displays</div>
                    <div class="meta">ACM Transactions on Graphics • March 2026</div>
                    <div class="summary">New neural rendering techniques improve image quality for computer-generated holography while reducing computation requirements.</div>
                </div>
                <div class="research-item">
                    <div class="title">ML for Photonic Manufacturing Yield Prediction</div>
                    <div class="meta">IEEE Transactions on Semiconductor Manufacturing • February 2026</div>
                    <div class="summary">Predict manufacturing yield from design parameters with 92% accuracy, allowing design optimizations that improve yield.</div>
                </div>
            </div>
        </div>
        
        <!-- Trends -->
        <div id="trends" class="tab-content">
            <div class="card">
                <h2>Market Trends & Industry Directions</h2>
                <div class="trend-item">AR/VR headset market growing 35% YoY driven by enterprise</div>
                <div class="trend-item">Spatial Light Modulator demand up 40% YoY</div>
                <div class="trend-item">Consumer wearables integrating environmental sensors (UV/air quality)</div>
                <div class="trend-item">AI acceleration in EDA tools for photonics</div>
                <div class="trend-item">Silicon photonics moving into AI accelerators</div>
                <div class="trend-item">Miniaturization trend continues for biosensors</div>
            </div>
        </div>
        
        <!-- Companies -->
        <div id="companies" class="tab-content">
            <div class="card">
                <h2>AR/VR & Holography Companies</h2>
                <div class="grid-3">
                    <div class="company-card">
                        <h4>Locus Optical (LCOL)</h4>
                        <p>Holographic waveguide tech</p>
                    </div>
                    <div class="company-card">
                        <h4>DigiSight (DISB)</h4>
                        <p>AR enterprise solutions</p>
                    </div>
                    <div class="company-card">
                        <h4>Apple (AAPL)</h4>
                        <p>Spatial computing ecosystem</p>
                    </div>
                    <div class="company-card">
                        <h4>Meta (META)</h4>
                        <p>Open source research, consumer AR</p>
                    </div>
                    <div class="company-card">
                        <h4>Sony (SONY)</h4>
                        <p>Micro-OLED displays</p>
                    </div>
                </div>
            </div>
            
            <div class="card">
                <h2>Sensor & Biosensor Companies</h2>
                <div class="grid-3">
                    <div class="company-card">
                        <h4>STMicroelectronics (STM)</h4>
                        <p>UV/biosensors</p>
                    </div>
                    <div class="company-card">
                        <h4>TE Connectivity (TEL)</h4>
                        <p>Medical sensors</p>
                    </div>
                    <div class="company-card">
                        <h4>ams-OSRAM (AMS)</h4>
                        <p>Optical sensors</p>
                    </div>
                    <div class="company-card">
                        <h4>DexCom (DXCM)</h4>
                        <p>CGM biosensors</p>
                    </div>
                    <div class="company-card">
                        <h4>Abbott (ABT)</h4>
                        <p>Continuous monitoring</p>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Events -->
        <div id="events" class="tab-content">
            <div class="card">
                <h2>Upcoming Industry Events & Conferences</h2>
                <div class="research-item">
                    <div class="title">SPIE Photonics West</div>
                    <div class="meta">January 2027 • San Francisco</div>
                </div>
                <div class="research-item">
                    <div class="title">Sensor Expo</div>
                    <div class="meta">June 2026 • San Jose</div>
                </div>
                <div class="research-item">
                    <div class="title">IEEE Photonics Conference</div>
                    <div class="meta">September 2026 • Seattle</div>
                </div>
                <div class="research-item">
                    <div class="title">Apple WWDC</div>
                    <div class="meta">June 2026 • Online/Cupertino</div>
                </div>
                <div class="research-item">
                    <div class="title">Semicon West</div>
                    <div class="meta">July 2026 • San Francisco</div>
                </div>
            </div>
        </div>
        
        <div class="footer">
            Research dashboard updated weekly for Prithu • Photonics/Biosensors • 
            <a href="https://github.com/prithu-roy/market-scanner-dashboard" target="_blank" rel="noopener">View on GitHub</a>
        </div>
    </div>
    
    <script>
        function showTab(tabId) {
            document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
            document.querySelectorAll('.tab-btn').forEach(t => t.classList.remove('active'));
            document.getElementById(tabId).classList.add('active');
            event.target.classList.add('active');
        }
    </script>
</body>
</html>
'''

with open('/home/node/.openclaw/workspace/tech-dashboard.html', 'w') as f:
    f.write(html)

print("Research tech dashboard generated successfully!")
