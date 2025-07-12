# 🔀 rune-arbitrage-bot — Telegram Bot & Visualization Tool for RUNE Arbitrage

## 🇬🇧 Description

This project consists of 3 Python scripts working together to track the price difference of **RUNE** cryptocurrency between **Binance** and **THORChain (Midgard)**:

1. **`rune_logger.py`** — logs the price delta every 5 seconds into `price_info.txt`
2. **`rune_bot.py`** — a Telegram bot that shows real-time price difference and sends a chart
3. **`price_graph.py`** — standalone script for charting historical deltas from the log

Great for tracking arbitrage opportunities or analyzing market spread over time.

---

## 💡 Features
- Pulls real-time prices from Binance & Midgard APIs
- Logs price deltas into a text file as JSON lines
- Visualizes historical price spread
- Telegram bot interface with buttons:
  - `⏱ Time?` → Real-time arbitrage direction
  - `📈 Graph!` → Sends matplotlib graph
- Simple architecture, easy to customize

---

## 🛠 Technologies
- Python 3.10+
- `requests`, `json`, `decimal`
- `telebot (pyTelegramBotAPI)`
- `matplotlib`
- Telegram Bot API

---

## 🚀 How to use

### 1. Start logger (recommended first step):
```bash
python rune_logger.py
