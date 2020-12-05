# Index Investing
import yfinance as yf


def indexInvesting():
    print("-------------------------- Index Investing --------------------------\n")

    # Get user input for the investment amount
    while True:
        try:
            investmentAmount = int(
                input("\nEnter the amount you want to invest (Minimum $5000 USD): "))
        except:
            print("Please enter a valid dollar amount!")
            continue

        if investmentAmount < 5000:
            print("Minimum investment amount is $5000 USD!")
        else:
            break

    # Selected stocks for Index Investing
    # Very low cost and has assets in around 500 of the largest US companies which span multiple industries.
    stockSymbol1 = "VFINX"
    stockSymbol1 = stockSymbol1.upper()

    # At least 80% of their assets in stocks are included in the S&P 500.
    stockSymbol2 = "FXAIX"
    stockSymbol2 = stockSymbol2.upper()

    # One of the lowest cost index funds, worth investing a little bit into.
    stockSymbol3 = "SWPPX"
    stockSymbol3 = stockSymbol3.upper()

    try:
        print("-------------------------- Stock 1 --------------------------")
        division = float(investmentAmount*0.50)
        print("Money division: (50%) $", division, sep="")
        print("Generating data from yfinance...")
        printStockInfo(stockSymbol1)

        print("-------------------------- Stock 2 --------------------------")
        division = float(investmentAmount*0.25)
        print("Money division: (25%) $", division, sep="")
        print("Generating data from yfinance...")
        printStockInfo(stockSymbol2)

        print("-------------------------- Stock 3 --------------------------")
        division = float(investmentAmount*0.25)
        print("Money division: (25%) $", division, sep="")
        print("Generating data from yfinance...")
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

    # Calculate the current price, value change and percent change
    valueChange = round(stockCurrent - stockPreviousClose, 2)
    percentChange = round((valueChange / stockPreviousClose) * 100, 2)
    changeDirection = "+" if (valueChange > 0) else ""
    print(f'${stockCurrent:3g} {changeDirection}{valueChange} ({changeDirection}{percentChange}%)', "\n")

    weeklyTrend = stock.history(period="5d")
    print("Weekly Trend:")
    print(weeklyTrend, '\n')


indexInvesting()
