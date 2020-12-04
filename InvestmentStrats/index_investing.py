# Index Investing
import yfinance as yf


def indexInvesting():
    print("-------------------------- Index Investing --------------------------\n")

    # Get user input for the investment amount
    while True:
        try:
            investmentAmount = int(input("\nEnter the amount you want to invest (Minimum $5000 USD): "))
        except:
            print("Please enter a valid dollar amount!")
            continue

        if investmentAmount < 5000:
            print("Minimum investment amount is $5000 USD!")
        else:
            break

    # Selected stocks for Index Investing
    stockSymbol1 = "VFINX"
    stockSymbol1 = stockSymbol1.upper()

    stockSymbol2 = "FXAIX"
    stockSymbol2 = stockSymbol2.upper()

    stockSymbol3 = "SWPPX"
    stockSymbol3 = stockSymbol3.upper()
    
    try:
        print("-------------------------- Stock 1 --------------------------")
        investment = float(investmentAmount/2)
        print("Money division: $", investment)
        printStockInfo(stockSymbol1)

        print("-------------------------- Stock 2 --------------------------")
        investment = float(investment/2)
        print("Money division: $", investment)
        printStockInfo(stockSymbol2)

        print("-------------------------- Stock 3 --------------------------")
        investment = float(investment/2)
        print("Money division: $", investment)
        printStockInfo(stockSymbol3)

    except:
        print("-------------------------- ERROR: Invalid Ticker Symbol --------------------------")

def printStockInfo(stockSymbol):
        stock = yf.Ticker(stockSymbol)

        # Print the Company's name and ticker symbol
        stockInfo = stock.info
        print(f"{stockInfo['shortName']} ({stockSymbol})")

        # Get the current stock value
        hist = stock.history(period="2d")
        stockCurrent = float(hist['Open'])

        # Get the previous close value
        stockPreviousClose = float(stockInfo['previousClose'])

        # Display the current price, value change and percent change
        print(calcStockInfo(stockCurrent, stockPreviousClose), '\n')
        weeklyTrend = stock.history(period="5d")
        print("Weekly Trend:")
        print(weeklyTrend, '\n')

def calcStockInfo(stockCurrent, stockPreviousClose):
        # Calculate the current price, value change and percent change
        valueChange = round(stockCurrent - stockPreviousClose, 2)
        percentChange = round((valueChange / stockPreviousClose) * 100, 2)
        changeDirection = "+" if (valueChange > 0) else ""
        return f'${stockCurrent:3g} {changeDirection}{valueChange} ({changeDirection}{percentChange}%)'

indexInvesting()