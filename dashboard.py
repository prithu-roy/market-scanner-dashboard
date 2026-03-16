"""
Stock Market Dashboard - Streamlit App
Run with: streamlit run dashboard.py
"""

import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Page config
st.set_page_config(
    page_title="Market Scanner Dashboard",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #0e1117
    }
    .stApp {
        background-color: #0e1117
    }
    .metric-card {
        background-color: #1e293b;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .bull { color: #22c55e; }
    .bear { color: #ef4444; }
    .caution { color: #f59e0b; }
</style>
""", unsafe_allow_html=True)

# Sample data (will be replaced by parsed markdown)
REPORTS = {
    "2026-03-16": {
        "title": "Stock Market Scan & Field Update",
        "major_news": [
            {"title": "UBS Downgrades US Equities to 'Benchmark'", "sentiment": "bearish"},
            {"title": "Fed Uncertainty Escalating - Kevin Warsh Nominated", "sentiment": "bearish"},
            {"title": "Geopolitical Risk - War with Iran", "sentiment": "bearish"},
        ],
        "movers": [
            {"ticker": "NKE", "move": "+1.50%", "type": "bull"},
            {"ticker": "BLK", "move": "+2.07%", "type": "bull"},
            {"ticker": "STLA", "move": "+1.08%", "type": "bull"},
            {"ticker": "GM", "move": "+0.77%", "type": "bull"},
            {"ticker": "CL=F", "move": "-4.94%", "type": "bear"},
        ],
        "earnings": [
            {"date": "Mar 19", "ticker": "FDX", "call": "Bearish", "reason": "shipping slowdown"},
            {"date": "Mar 20", "ticker": "BBY", "call": "Bullish", "reason": "consumer electronics"},
            {"date": "Mar 24", "ticker": "LMT", "call": "Bullish", "reason": "government spend"},
            {"date": "Mar 25", "ticker": "NKE", "call": "Bearish", "reason": "China demand weak"},
            {"date": "Mar 27", "ticker": "MU", "call": "Bullish", "reason": "AI memory demand"},
            {"date": "Apr 2", "ticker": "AAPL", "call": "Bullish", "reason": "services growth"},
        ],
        "recommendations": [
            {"ticker": "MU", "direction": "BULLISH", "reason": "AI memory demand strong"},
            {"ticker": "LMT", "direction": "BULLISH", "reason": "Defense spending tailwind"},
            {"ticker": "AAPL", "direction": "BULLISH", "reason": "Services growth"},
            {"ticker": "NKE", "direction": "BEARISH", "reason": "China demand weak"},
            {"ticker": "TSLA", "direction": "BEARISH", "reason": "Thiel exit signal"},
        ],
        "indices": [
            {"index": "S&P 500", "level": "~5,800", "support": "5,650", "resistance": "5,900"},
            {"index": "NASDAQ", "level": "~18,500", "support": "18,000", "resistance": "19,000"},
            {"index": "DOW", "level": "~42,000", "support": "41,500", "resistance": "43,000"},
            {"index": "VIX", "level": "~18", "support": "15", "resistance": "22"},
        ]
    },
    "2026-03-17": {
        "title": "Market Scan - March 17, 2026",
        "earnings_tomorrow": [
            {"ticker": "DLTR", "company": "Dollar Tree", "cap": "$23.33B", "eps": "$2.53"},
            {"ticker": "SMTC", "company": "Semtech", "cap": "$8.24B", "eps": "$0.43"},
            {"ticker": "VFS", "company": "VinFast Auto", "cap": "$7.07B", "eps": "-$0.36"},
            {"ticker": "SAIC", "company": "Science Applications", "cap": "$4.28B", "eps": "Pending"},
        ],
        "setups": [
            {"ticker": "SMTC", "direction": "BEARISH", "zone": "$22.50-$24.00", "confidence": "LOW"},
            {"ticker": "SAIC", "direction": "BULLISH", "zone": "$95-$98", "confidence": "MEDIUM"},
        ]
    }
}

def main():
    st.title("📊 Market Scanner Dashboard")
    
    # Sidebar
    st.sidebar.header("Navigation")
    report_date = st.sidebar.selectbox(
        "Select Report Date",
        options=list(REPORTS.keys()),
        index=len(REPORTS.keys()) - 1
    )
    
    report = REPORTS[report_date]
    
    # Header
    st.header(f"📅 {report['title']}")
    st.markdown(f"**Generated:** {report_date}")
    
    # Layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Major News
        if "major_news" in report:
            st.subheader("🚨 Major Market News")
            for news in report["major_news"]:
                emoji = "🔴" if news.get("sentiment") == "bearish" else "🟢"
                st.markdown(f"- {emoji} **{news['title']}**")
        
        # Earnings Calls
        if "earnings" in report:
            st.subheader("📅 Upcoming Earnings")
            df = pd.DataFrame(report["earnings"])
            st.dataframe(df, use_container_width=True, hide_index=True)
        
        # Earnings Tomorrow
        if "earnings_tomorrow" in report:
            st.subheader("📅 Earnings Tomorrow")
            df = pd.DataFrame(report["earnings_tomorrow"])
            st.dataframe(df, use_container_width=True, hide_index=True)
    
    with col2:
        # Movers
        if "movers" in report:
            st.subheader("📈 Today's Movers")
            for m in report["movers"]:
                color = "green" if m["type"] == "bull" else "red"
                st.markdown(f":{color}[**{m['ticker']}**] {m['move']}")
        
        # Indices
        if "indices" in report:
            st.subheader("📊 Key Levels")
            for idx in report["indices"]:
                st.markdown(f"""
                <div class="metric-card">
                    <strong>{idx['index']}</strong><br>
                    Level: {idx['level']}<br>
                    <span style="color: #22c55e">Support: {idx['support']}</span> | 
                    <span style="color: #ef4444">Resistance: {idx['resistance']}</span>
                </div>
                """, unsafe_allow_html=True)
    
    # Recommendations (full width)
    if "recommendations" in report:
        st.subheader("🎯 High-Conviction Plays")
        cols = st.columns(len(report["recommendations"]))
        for i, rec in enumerate(report["recommendations"]):
            with cols[i]:
                color = "green" if rec["direction"] == "BULLISH" else "red"
                st.markdown(f"""
                <div style="background-color: #1e293b; padding: 15px; border-radius: 10px; text-align: center;">
                    <h3 style="color: {color}; margin: 0;">{rec['ticker']}</h3>
                    <strong>{rec['direction']}</strong><br>
                    <small>{rec['reason']}</small>
                </div>
                """, unsafe_allow_html=True)
    
    # Data Status
    st.markdown("---")
    st.caption("📡 Data sources: Yahoo Finance, Reuters, UBS Global Strategy")

if __name__ == "__main__":
    main()
