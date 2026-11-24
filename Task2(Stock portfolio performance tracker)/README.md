
# Task 2: Stock Portfolio Performance Tracker

## Overview
The Stock Portfolio Performance Tracker is a Python-based project that calculates the performance of stock holdings using purchase prices, share quantities, and current stock prices stored in a CSV file.

It calculates the total investment, current market value, profit or loss, and percentage return for each stock and the overall portfolio.

## Features
- Loads stock ticker symbols and current prices from a CSV file.
- Accepts stock ticker, buying price, and share quantity from the user.
- Checks whether a stock ticker exists in the price dataset.
- Calculates investment for each stock.
- Calculates current market value.
- Determines profit or loss for individual holdings.
- Calculates percentage gain or loss.
- Generates an overall portfolio performance summary.
- Exports the results to a CSV report.

## Technologies Used
- Python 3
- `csv` module

## Project Structure
```text
Task2(Stock portfolio performance tracker)/
│
├── portfolio.py
├── stock_prices.csv
├── summary.csv
└── README.md
```

*Note: `summary.csv` is generated when the program runs.*

## Calculations

**1. Investment**

Investment = Buying Price × Quantity

**2. Market Value**

Market Value = Current Price × Quantity

**3. Profit or Loss**

Profit/Loss = Market Value − Investment

**4. Percentage Gain or Loss**

Gain/Loss (%) = (Profit/Loss ÷ Investment) × 100

**5. Overall Portfolio Return**

Overall Return (%) = (Total Profit/Loss ÷ Total Investment) × 100

## Input Dataset

The program reads stock prices from `stock_prices.csv`.

Example:

```csv
Ticker,CurrentPrice
AAPL,180
MSFT,400
GOOGL,170
NVDA,140
```

These are sample prices for demonstration, not live market prices.

## Output
The program displays:
- Stock ticker
- Buying price
- Share quantity
- Current price
- Total investment
- Current market value
- Profit or loss
- Percentage gain or loss

It also exports the calculated results to `summary.csv`.

## How to Run

1. Install Python 3.
2. Keep `portfolio.py` and `stock_prices.csv` in the same directory.
3. Open the project folder in VS Code or a terminal.
4. Run:

```bash
python portfolio.py
```

5. Enter the number of stocks.
6. Provide the ticker, buying price, and share quantity for each stock.
7. View the portfolio summary and generated CSV report.

## Python Concepts Used
- Dictionaries
- Lists
- Loops
- Conditional statements
- User input
- File handling
- CSV reading and writing
- Exception handling
- Arithmetic operations

## Learning Outcomes
- Practiced working with CSV datasets.
- Learned to store and process financial information using dictionaries.
- Applied mathematical formulas to calculate portfolio performance.
- Generated structured reports using Python's CSV module.
- Practiced basic error handling and input validation.

## Project Type
Python Programming Internship — Task 2
