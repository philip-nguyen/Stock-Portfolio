# Value Investing

import yfinance as yf


def valueInvesting():
    print("-------------------------- Value Investing --------------------------\n")

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
    # Consumer credit and insurance business that has a fairly steady performance and has been on the rise.
    stockSymbol1 = "OMF"
    stockSymbol1 = stockSymbol1.upper()

    # Auto-dealer that has had many ups and downs but is slowly on the rise.
    stockSymbol2 = "PAG"
    stockSymbol2 = stockSymbol2.upper()

    # CVS is on the rise due to the current health crisis and are making efforts on reducing the spread of the virus.
    stockSymbol3 = "CVS"
    stockSymbol3 = stockSymbol3.upper()

    # Drug developer owns various blockbuster drugs and is acquiring more.
    stockSymbol4 = "ABBV"
    stockSymbol4 = stockSymbol4.upper()

    # They produce and sell various types of ingredients and operate worldwide.
    stockSymbol5 = "INGR"
    stockSymbol5 = stockSymbol5.upper()

    try:
        print("-------------------------- Stock 1 --------------------------")
        division = float(investmentAmount*0.40)
        print("Money division: (40%) $", division, sep="")
        print("Generating data from yfinance...")
        printStockInfo(stockSymbol1)

        print("-------------------------- Stock 2 --------------------------")
        division = float(investmentAmount*0.20)
        print("Money division: (20%) $", division, sep="")
        print("Generating data from yfinance...")
        printStockInfo(stockSymbol2)

        print("-------------------------- Stock 3 --------------------------")
        division = float(investmentAmount*0.20)
        print("Money division: (20%) $", division, sep="")
        print("Generating data from yfinance...")
        printStockInfo(stockSymbol3)

        print("-------------------------- Stock 4 --------------------------")
        division = float(investmentAmount*0.10)
        print("Money division: (10%) $", division, sep="")
        print("Generating data from yfinance...")
        printStockInfo(stockSymbol4)

        print("-------------------------- Stock 5 --------------------------")
        division = float(investmentAmount*0.10)
        print("Money division: (10%) $", division, sep="")
        print("Generating data from yfinance...")
        printStockInfo(stockSymbol5)

    except:
        print("-------------------------- ERROR: Invalid Ticker Symbol --------------------------")


def printStockInfo(stockSymbol):
    stock = yf.Ticker(stockSymbol)

    # Print the Company's name and ticker symbol
    stockInfo = stock.info
    print(f"{stockInfo['shortName']} ({stockSymbol})")

    # Get the current stock value
    stockCurrent = float(stockInfo['open'])

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


valueInvesting()
