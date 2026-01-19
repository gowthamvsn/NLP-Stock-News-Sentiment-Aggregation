# ============================================================
# FETCH STOCK NEWS FROM MULTIPLE SOURCES
# ============================================================

import requests
from datetime import date, timedelta, datetime
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd
import yfinance as yf

# ==============================
# CONFIG
# ==============================
TICKER_SYMBOL = "BE"
DAYS_LOOKBACK = 5

NEWSAPI_KEY = "YOUR_API_KEY"
NEWSAPI_URL = "https://newsapi.org/v2/everything"

# ==============================
# NEWSAPI
# ==============================
def fetch_newsapi(ticker):
    params = {
        "q": f"{ticker} stock",
        "sortBy": "publishedAt",
        "pageSize": 10,
        "apiKey": NEWSAPI_KEY
    }
    r = requests.get(NEWSAPI_URL, params=params, timeout=10)
    data = r.json()

    rows = []
    for article in data.get("articles", []):
        rows.append([
            ticker,
            article.get("publishedAt"),
            article.get("source", {}).get("name"),
            f"{article.get('title')} {article.get('description')} {article.get('content')}"
        ])

    df = pd.DataFrame(rows, columns=["Ticker", "Date", "Source", "Title"])
    df["Date"] = pd.to_datetime(df["Date"]).dt.date
    return df[df["Date"] > date.today() - timedelta(days=DAYS_LOOKBACK)]

# ==============================
# FINVIZ
# ==============================
def fetch_finviz(ticker):
    url = f"https://finviz.com/quote.ashx?t={ticker}"
    req = Request(url=url, headers={"user-agent": "news-app"})
    html = BeautifulSoup(urlopen(req), "html.parser")

    table = html.find(id="news-table")
    rows = []

    for row in table.findAll("tr"):
        try:
            title = row.a.text
            date_text = row.td.text
            rows.append([ticker, date_text, title])
        except:
            continue

    df = pd.DataFrame(rows, columns=["Ticker", "Date", "Title"])
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce").dt.date
    return df[df["Date"] > date.today() - timedelta(days=DAYS_LOOKBACK)]

# ==============================
# YAHOO FINANCE
# ==============================
def fetch_yahoo(ticker, max_items=10):
    news = yf.Ticker(ticker).news
    rows = []

    for item in news[:max_items]:
        rows.append([
            ticker,
            item["content"]["pubDate"],
            item["content"]["title"] + ". " + item["content"]["summary"]
        ])

    df = pd.DataFrame(rows, columns=["Ticker", "Date", "Title"])
    df["Date"] = pd.to_datetime(df["Date"]).dt.date
    return df[df["Date"] > date.today() - timedelta(days=DAYS_LOOKBACK)]
