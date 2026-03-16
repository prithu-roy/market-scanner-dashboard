#!/usr/bin/env python3

html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>✅ Personal Tasks & Agenda</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #0f172a;
            color: #e2e8f0;
            min-height: 100vh;
        }
        .header {
            background: linear-gradient(135deg, #059669 0%, #10b981 100%);
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
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        
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
        
        .tasks-scroll {
            max-height: 450px;
            overflow-y: auto;
        }
        .tasks-scroll::-webkit-scrollbar { width: 8px; }
        .tasks-scroll::-webkit-scrollbar-track { background: #0f172a; border-radius: 4px; }
        .tasks-scroll::-webkit-scrollbar-thumb { background: #475569; border-radius: 4px; }
        
        .task-list { list-style: none; }
        .task {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 12px 15px;
            background: #0f172a;
            border-radius: 8px;
            margin: 8px 0;
            border-left: 3px solid;
        }
        .task.high { border-left-color: #ef4444; }
        .task.medium { border-left-color: #f59e0b; }
        .task.low { border-left-color: #10b981; }
        
        .checkbox {
            width: 20px;
            height: 20px;
            border: 2px solid #10b981;
            border-radius: 4px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .checkbox.checked { background: #10b981; }
        .checkbox.checked::after { content: "✓"; color: #0f172a; font-size: 14px; }
        
        .task-content { flex: 1; }
        .task-title { font-weight: 500; }
        .task-meta { font-size: 0.8rem; color: #94a3b8; margin-top: 3px; }
        
        .tag {
            padding: 3px 10px;
            border-radius: 12px;
            font-size: 0.7rem;
            font-weight: 600;
        }
        .tag.high { background: #ef444420; color: #ef4444; }
        .tag.medium { background: #f59e0b20; color: #f59e0b; }
        .tag.low { background: #22c55e20; color: #22c55e; }
        
        .agenda {
            background: #0f172a;
            border-radius: 8px;
            overflow: hidden;
        }
        .agenda-item {
            display: flex;
            padding: 12px 15px;
            border-bottom: 1px solid #334155;
        }
        .agenda-item:last-child { border-bottom: none; }
        .agenda-time {
            min-width: 90px;
            color: #10b981;
            font-weight: 600;
            font-size: 0.9rem;
        }
        .agenda-content { color: #e2e8f0; }
        
        .routine-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
        }
        .routine-card {
            background: #0f172a;
            padding: 15px;
            border-radius: 10px;
        }
        .routine-card h4 { color: #10b981; margin-bottom: 10px; }
        .routine-card ul { padding-left: 18px; color: #94a3b8; }
        .routine-card li { margin: 5px 0; font-size: 0.9rem; }
        
        .notes-container {
            background: #0f172a;
            padding: 15px;
            border-radius: 8px;
        }
        .note-item {
            padding: 8px 0;
            color: #94a3b8;
            border-bottom: 1px solid #334155;
        }
        .note-item:last-child { border-bottom: none; }
        
        .footer-note {
            text-align: center;
            color: #64748b;
            font-size: 0.8rem;
            padding: 10px;
        }
        .footer-note a { color: #10b981; text-decoration: none; }
    </style>
</head>
<body>
    <div class="header">
        <h1>✅ Personal Tasks</h1>
        <span class="date-badge">Wednesday, March 17, 2026</span>
    </div>
    
    <div class="container">
        <div class="card">
            <h2>🎯 Today's Priorities</h2>
            <div class="tasks-scroll">
                <ul class="task-list">
'''

priorities = [
    {"title": "Complete Q1 Financial Report Draft", "meta": "Crucial deadline approaching for internal review", "priority": "high"},
    {"title": "Follow up on insurance claim status", "meta": "Need to clarify submitted documents", "priority": "high"},
    {"title": "Review 'Python for Data Science' Module 3", "meta": "Stay on track with personal learning goals", "priority": "medium"},
    {"title": "Meal prep for Wednesday/Thursday", "meta": "Prepare healthy lunch/dinner to avoid eating out", "priority": "medium"},
    {"title": "Check dashboard auto-update status", "meta": "Verify GitHub Pages deployment is working", "priority": "medium"},
    {"title": "Water indoor plants", "meta": "They are looking a bit dry", "priority": "low"},
    {"title": "Research new running shoes", "meta": "Old pair is worn out; explore options online", "priority": "low"}
]

for p in priorities:
    html += f'''                    <li class="task {p['priority']}">
                        <div class="checkbox"></div>
                        <div class="task-content">
                            <div class="task-title">{p['title']}</div>
                            <div class="task-meta">{p['meta']}</div>
                        </div>
                        <span class="tag {p['priority']}">{p['priority'].upper()}</span>
                    </li>
'''

html += '''                </ul>
            </div>
        </div>
        
        <div class="card">
            <h2>📅 Today's Agenda</h2>
            <div class="agenda">
'''

agenda = [
    {"time": "Morning", "task": "Wake up, morning routine, healthy breakfast"},
    {"time": "Morning", "task": "Deep work: Complete Q1 Financial Report draft"},
    {"time": "Morning", "task": "Address critical work emails & communications"},
    {"time": "Mid-day", "task": "Lunch break and 15-minute walk outside"},
    {"time": "Mid-day", "task": "Call insurance company regarding claim update"},
    {"time": "Mid-day", "task": "Learning time: Review Python Data Science Module 3"},
    {"time": "Mid-day", "task": "Wrap remaining work, plan tomorrow"},
    {"time": "Evening", "task": "End workday, transition to personal time"},
    {"time": "Evening", "task": "Meal prep + water plants"},
    {"time": "Evening", "task": "Research running shoes online"},
    {"time": "Evening", "task": "Relax, read, prepare for bed"}
]

for a in agenda:
    html += f'''                <div class="agenda-item">
                    <div class="agenda-time">{a['time']}</div>
                    <div class="agenda-content">{a['task']}</div>
                </div>
'''

html += '''            </div>
        </div>
        
        <div class="card">
            <h2>🔄 Daily Routine</h2>
            <div class="routine-grid">
                <div class="routine-card">
                    <h4>🌅 Morning (8-9 AM)</h4>
                    <ul>
                        <li>Check market open</li>
                        <li>Review pre-market movers</li>
                        <li>Scan earnings calendar</li>
                    </ul>
                </div>
                <div class="routine-card">
                    <h4>📊 Mid-day (12-1 PM)</h4>
                    <ul>
                        <li>Check news catalysts</li>
                        <li>Review sector rotation</li>
                        <li>Update watchlist</li>
                    </ul>
                </div>
                <div class="routine-card">
                    <h4>🌙 Evening (6-7 PM)</h4>
                    <ul>
                        <li>Run daily scan</li>
                        <li>Update all dashboards</li>
                        <li>Commit & push to GitHub</li>
                        <li>Plan next day</li>
                    </ul>
                </div>
                <div class="routine-card">
                    <h4>📅 Weekly</h4>
                    <ul>
                        <li>Portfolio review</li>
                        <li>Sector analysis</li>
                        <li>Rebalance check</li>
                    </ul>
                </div>
            </div>
        </div>
        
        <div class="card">
            <h2>📝 Notes & Reminders</h2>
            <div class="notes-container">
'''

notes = [
    "Today is St. Patrick's Day - remember to wear something green if going out!",
    "Fed meeting March 18-19 - watch for rate decision announcements",
    "MU earnings March 27 - AI memory play, on watchlist",
    "Configure Brave Search API for better market data collection",
    "Stay hydrated throughout the day during deep work sessions",
    "Prioritize Q1 report: aim for solid draft before end of day"
]

for n in notes:
    html += f'''                <div class="note-item">{n}</div>
'''

html += '''            </div>
        </div>
        
        <div class="footer-note">
            Dashboard auto-updates daily from cloud cron job • <a href="https://github.com/prithu-roy/market-scanner-dashboard" target="_blank" rel="noopener">View Source on GitHub</a>
        </div>
    </div>
    
    <script>
        // Simple checkbox toggle
        document.querySelectorAll('.checkbox').forEach(cb => {
            cb.addEventListener('click', () => cb.classList.toggle('checked'));
        });
    </script>
</body>
</html>
'''

with open('/home/node/.openclaw/workspace/personal-dashboard.html', 'w') as f:
    f.write(html)

print("✅ Personal dashboard updated successfully!")
