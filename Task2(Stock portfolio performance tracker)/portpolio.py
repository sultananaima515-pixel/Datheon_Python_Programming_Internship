import csv


stock_prices = {}

try:
    with open("stock_prices.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            ticker = row["Ticker"].strip().upper()
        
            price = float(row["CurrentPrice"])

            stock_prices[ticker] = price
            
except FileNotFoundError:
    print("Error: stock_prices.csv not found!")
    exit()

except (KeyError, ValueError):
    print("Error: Invalid CSV structure or price!")
    exit()

print(stock_prices)


portfolio = {}

number_of_stocks = int(input("How many stocks do you want to add? "))

for i in range(number_of_stocks):

    ticker = input("Enter stock ticker: ").upper()

    buy_price = float(input("Enter buying price: "))

    quantity = int(input("Enter share quantity: "))

    portfolio[ticker] = {
        "buy_price": buy_price,
        "quantity": quantity
    }
    


results = []

total_investment = 0
total_market_value = 0

for ticker, details in portfolio.items():

    buy_price = details["buy_price"]
    quantity = details["quantity"]

    if ticker not in stock_prices:
        print("Stock not found:", ticker)
        continue

    current_price = stock_prices[ticker]

    investment = buy_price * quantity
    market_value = current_price * quantity

    profit_loss = market_value - investment
    gain_loss_percent = (profit_loss / investment) * 100

    total_investment += investment
    total_market_value += market_value

    print("\nTicker:", ticker)
    print("Investment:", investment)
    print("Market Value:", market_value)
    print("Profit/Loss:", profit_loss)
    print("Gain/Loss:", round(gain_loss_percent, 2), "%")

    results.append({
        "Ticker": ticker,
        "Buy Price": buy_price,
        "Quantity": quantity,
        "Current Price": current_price,
        "Investment": investment,
        "Market Value": market_value,
        "Profit/Loss": profit_loss,
        "Gain/Loss (%)": round(gain_loss_percent, 2)
    })


print("\n========== PORTFOLIO SUMMARY ==========")

overall_profit_loss = total_market_value - total_investment

if total_investment > 0:
    overall_percentage = (overall_profit_loss / total_investment) * 100
else:
    overall_percentage = 0

print("Total Investment:", total_investment)
print("Total Market Value:", total_market_value)
print("Total Profit/Loss:", overall_profit_loss)
print("Overall Return:", round(overall_percentage, 2), "%")


with open("summary.csv", "w", newline="") as file:

    fieldnames = [
        "Ticker",
        "Buy Price",
        "Quantity",
        "Current Price",
        "Investment",
        "Market Value",
        "Profit/Loss",
        "Gain/Loss (%)"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(results)

print("\nPortfolio summary saved successfully!")