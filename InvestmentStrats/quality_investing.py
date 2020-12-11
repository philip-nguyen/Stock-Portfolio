# Quality Investing

import yfinance as yf


def qualityInvesting():
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

    # Selected stocks for Growth Investing
    # Visa - Global payments technology that facilitates electronic funds transfers 
    stockSymbol1 = "V"
    stockSymbol1 = stockSymbol1.upper()

    # Amazon - E-commerce, cloud computing, digital streaming and AI technologies 
    stockSymbol2 = "AMZN"
    stockSymbol2 = stockSymbol2.upper()

    # Microsoft - Develops, manufactures, licenses, supports and sells computer software, consumer electronics, pcs and related services
    stockSymbol3 = "MSFT"
    stockSymbol3 = stockSymbol3.upper()

    # Salesforce - Provides customer relationship management service, marketing automation analytics and application development 
    stockSymbol4 = "CRM"
    stockSymbol4 = stockSymbol4.upper()

    # Nike - American corporation engaged in the design, development, manufacturing and worldwide marketing and sales of footwear,
    # apparel, equipment, accessories, and services
    stockSymbol5 = "NKE"
    stockSymbol5 = stockSymbol5.upper()


    try:
        print("-------------------------- Stock 1 --------------------------")
        division = float(investmentAmount*0.2)
        print("Money division: (20%) $", division, sep="")
        print("Generating data from yfinance...")
        printStockInfo(stockSymbol1)

        print("-------------------------- Stock 2 --------------------------")
        division = float(investmentAmount*0.2)
        print("Money division: (20%) $", division, sep="")
        print("Generating data from yfinance...")
        printStockInfo(stockSymbol2)

        print("-------------------------- Stock 3 --------------------------")
        division = float(investmentAmount*0.2)
        print("Money division: (20%) $", division, sep="")
        print("Generating data from yfinance...")
        printStockInfo(stockSymbol3)

        print("-------------------------- Stock 4 --------------------------")
        division = float(investmentAmount*0.2)
        print("Money division: (20%) $", division, sep="")
        print("Generating data from yfinance...")
        printStockInfo(stockSymbol4)

        print("-------------------------- Stock 5 --------------------------")
        division = float(investmentAmount*0.2)
        print("Money division: (20%) $", division, sep="")
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


qualityInvesting()
