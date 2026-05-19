# Binance Futures Testnet Trading Bot

## Overview

This project is a simplified trading bot developed for the Binance Futures Testnet (USDT-M).  
The bot allows users to place both MARKET and LIMIT orders directly from the command line using Python.

The application is built with a clean and reusable structure and includes:

- Binance Futures Testnet integration
- CLI-based order execution
- Input validation
- Logging support
- Error handling
- Separate API and order management layers

---

# Features

✅ Place MARKET orders  
✅ Place LIMIT orders  
✅ BUY and SELL support  
✅ Command-line interface (CLI)  
✅ Input validation  
✅ Logging of requests and responses  
✅ Exception handling  
✅ Structured project architecture  

---

# Tech Stack

- Python 3.x
- Requests
- python-dotenv

---

# Binance Futures Testnet

Base URL used for API requests:

```text
https://testnet.binancefuture.com
```

---

# Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── bot.log
│
├── cli.py
├── requirements.txt
├── .env
└── README.md
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <your_repository_url>
cd trading_bot
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in the project root directory.

Example:

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
BASE_URL=https://testnet.binancefuture.com
```

---

# Running the Application

## MARKET Order Example

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

## LIMIT Order Example

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 75000
```

---

# Command Line Arguments

| Argument | Description | Required |
|---|---|---|
| `--symbol` | Trading pair symbol (e.g. BTCUSDT) | Yes |
| `--side` | BUY or SELL | Yes |
| `--type` | MARKET or LIMIT | Yes |
| `--quantity` | Order quantity | Yes |
| `--price` | Required for LIMIT orders | Only for LIMIT |

---

# Validation Rules

The application validates:

- Valid order side (`BUY` or `SELL`)
- Valid order type (`MARKET` or `LIMIT`)
- LIMIT orders must include `--price`

Example validation error:

```text
❌ Error: LIMIT orders require --price
```

---

# Example Output

## MARKET Order

```text
=== ORDER REQUEST ===
{'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 0.001}

=== ORDER RESPONSE ===
{
  'orderId': 13161639263,
  'status': 'NEW',
  'executedQty': '0.0000',
  'avgPrice': '0.00'
}

✅ Order placed successfully!
```

---

## LIMIT Order

```text
=== ORDER REQUEST ===
{'symbol': 'BTCUSDT', 'side': 'SELL', 'type': 'LIMIT', 'quantity': 0.001, 'price': 75000}

=== ORDER RESPONSE ===
{
  'orderId': 13161642740,
  'status': 'NEW',
  'executedQty': '0.0000',
  'avgPrice': '0.00'
}

✅ Order placed successfully!
```

---

# Logging

All API requests, responses, and errors are logged in:

```text
logs/bot.log
```

Example log entries:

```text
2026-05-19 15:19:57,913 - INFO - bot.orders - Placing MARKET order: BTCUSDT BUY 0.001

2026-05-19 15:20:34,469 - INFO - bot.orders - Response: {'orderId': 13161642740, 'status': 'NEW'}
```

---

# Error Handling

The bot handles:

- Invalid order side
- Invalid order type
- Missing LIMIT price
- API response errors
- Network/request exceptions

---

# Assumptions

- Binance Futures Testnet account is active
- Valid API credentials are configured
- Internet connection is available
- BTCUSDT pair is available on Binance Futures Testnet

---

# Requirements

```text
python-binance==1.0.36
python-dotenv==1.2.2
requests==2.32.3
```

---

# Notes

- This project uses Binance Futures Testnet for safe testing purposes.
- No real funds are used.
- LIMIT orders may remain in `NEW` status until the target price is reached.

```
