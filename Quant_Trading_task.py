import yfinance as yf

# This gets the last 2 years of Apple stock prices
data = yf.download("NVDA", period="10y")

def get_trading_signals(prices):
    bank_balance = float(input("What is your bank balance"))
    shares_held = 0
    isholding = False
    price_list = [100,102]
    buying_price = 0
    for i in range(2, len(prices)):
        print(f"DAY { i + 1}")
        average_price = (prices[i]+prices[i-1]+prices[i-2])/3
        price_list.append(round(average_price, 2))
        if 1.03*average_price < (prices[i]) and isholding == False:
            print(f"BUY SIGNAL")
            shares_held += bank_balance/prices[i]
            buying_price = prices[i]
            bank_balance = 0
            isholding = True
        elif isholding:
            if prices[i] < (0.95*buying_price) or prices[i] < average_price:
                print("SELL SIGNAL")
                bank_balance = shares_held*prices[i]
                isholding = False
                shares_held = 0
    print(f"Your total amount in your bank balance is £{bank_balance:.2f}")
    total_wealth = bank_balance + (shares_held * prices[-1])
    print(f"Your total wealth is £{total_wealth:.2f}")        
# This converts the 'Close' prices into a list for your function
prices = data['Close'].values.flatten().tolist()
get_trading_signals(prices)
