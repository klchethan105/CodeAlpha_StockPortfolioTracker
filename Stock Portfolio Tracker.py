# Hardcoded stock prices (USD)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "MSFT": 310,
    "AMZN": 140
}

portfolio = {}  # To store stock name and quantity

print("Stock Portfolio Tracker")
print("Available stocks and prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

# Take user inputs
while True:
    stock_name = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
    if stock_name == "DONE":
        break
    if stock_name not in stock_prices:
        print("⚠ Stock not found! Please enter a valid symbol.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
        if quantity <= 0:
            print(" Quantity must be positive.")
            continue
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
    except ValueError:
        print("⚠ Please enter a valid number.")

# Calculate total investment
total_value = 0
print("\n Your Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_value += investment
    print(f"{stock}: {qty} shares × ${price} = ${investment}")

print(f"\n Total Investment Value: ${total_value}")

# Save to file
save_choice = input("\nDo you want to save this portfolio to a file? (yes/no): ").lower()
if save_choice == "yes":
    filename = "portfolio_summary.txt"
    with open(filename, "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("----------------------\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            investment = price * qty
            file.write(f"{stock}: {qty} shares × ${price} = ${investment}\n")
        file.write(f"\n Total Investment Value: ${total_value}\n")
    print(f" Portfolio saved to {filename}")
