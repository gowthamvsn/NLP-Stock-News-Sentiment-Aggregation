# Stock News Sentiment Aggregation

This project collects recent stock-related news from multiple public sources
and applies sentiment analysis to measure overall market tone for a given ticker.

The goal is to compare sentiment signals across sources and NLP methods,
not to predict prices or execute trades.

---

## Why This Project?

Market participants often react to news before fundamentals change.
However, news sentiment is noisy and source-dependent.

This project explores:
- How sentiment differs across news sources
- How different NLP models score the same text
- Whether sentiment signals align consistently

It is designed as a **research and signal exploration tool**.

---

## News Sources

- **Finviz** (scraped headlines)
- **NewsAPI** (curated articles)
- **Yahoo Finance** (ticker-specific news)

---

## Sentiment Models Used

- **VADER** (rule-based, finance-friendly)
- **TextBlob** (lexicon-based polarity scoring)

Using two models helps highlight model bias and disagreement.

---

## Pipeline Overview

### Stage 1: News Collection
- Fetch recent articles (last 5 days)
- Normalize titles and timestamps
- Filter out same-day noise

### Stage 2: Sentiment Analysis
- Compute sentiment using VADER
- Compute sentiment using TextBlob
- Aggregate sentiment scores per source

### Stage 3: Comparison
- Compare sentiment totals across:
  - Sources
  - Models

---

## File Structure

```
src/
├── fetch_news.py
├── sentiment_analysis.py
```

---

## Notes

- API keys are required for NewsAPI.
- Data is fetched live and not stored.
- This project focuses on sentiment signals only.

---

## Author
Gowtham Vuppaladhadiam
