# Index Investing
import yfinance as yf
import datetime

"""
    The invest function takes in an investment amount
    and returns a string var
"""


def invest(investmentAmount):
    print("-------------------------- Index Investing --------------------------\n")
    # Index Investing - Stocks mirror the collection of companies and performance of market indexes

    output = "------------ Index Investing ------------\n"
    output += f'Amount for Strategy: ${investmentAmount}\n'
    # Flagship index on the National Stock Exchange of India.
    stockSymbol1 = "^NSEI"
    stockSymbol1 = stockSymbol1.upper()

    # French stock market index that tracks 40 of the largest French stocks.
    stockSymbol2 = "^FCHI"
    stockSymbol2 = stockSymbol2.upper()

    # Capitalization-weighted index that tracks the companies listed in Canada's largest stock exchange.
    stockSymbol3 = "^GSPTSE"
    stockSymbol3 = stockSymbol3.upper()

    # Index that tracks the Russian stock market.
    stockSymbol4 = "IMOEX.ME"
    stockSymbol4 = stockSymbol4.upper()

    # Most widely used index of stocks with small market capitalization.
    stockSymbol5 = "^RUT"
    stockSymbol5 = stockSymbol5.upper()

    try:
        print("-------------------------- Stock 1 --------------------------")
        division = float(investmentAmount*0.25)
        output += "Money division: (25%) $" + str(division) + "\n"
        print("Generating data from yfinance...")
        output += printStockInfo(stockSymbol1) + "\n"

        print("-------------------------- Stock 2 --------------------------")
        division = float(investmentAmount*0.25)
        output += "Money division: (25%) $" + str(division) + "\n"
        print("Generating data from yfinance...")
        output += printStockInfo(stockSymbol2) + "\n"

        print("-------------------------- Stock 3 --------------------------")
        division = float(investmentAmount*0.125)
        output += "Money division: (12.5%) $" + str(division) + "\n"
        print("Generating data from yfinance...")
        output += printStockInfo(stockSymbol3) + "\n"

        print("-------------------------- Stock 4 --------------------------")
        division = float(investmentAmount*0.125)
        output += "Money division: (12.5%) $" + str(division) + "\n"
        print("Generating data from yfinance...")
        output += printStockInfo(stockSymbol4) + "\n"

        print("-------------------------- Stock 5 --------------------------")
        division = float(investmentAmount*0.25)
        output += "Money division: (25%) $" + str(division) + "\n"
        print("Generating data from yfinance...")
        output += printStockInfo(stockSymbol5) + "\n"
        output += "\n\n"

    except:
        print("-------------------------- ERROR: Invalid Ticker Symbol --------------------------")
        return "Error in Index Investing :(\n"

    return output


"""
    The printStockInfo function takes a string stockSymbol
    and returns a string var
"""


def printStockInfo(stockSymbol):
    stock = yf.Ticker(stockSymbol)

    # Print the Company's name and ticker symbol
    stockInfo = stock.info
    output = f"{stockInfo['shortName']} ({stockSymbol})"

    # Get the current stock value
    stockCurrent = float(stockInfo['open'])

    # Get the previous close value
    stockPreviousClose = float(stockInfo['previousClose'])

    # Calculate the current price, value change and percent change
    valueChange = round(stockCurrent - stockPreviousClose, 2)
    percentChange = round((valueChange / stockPreviousClose) * 100, 2)
    changeDirection = "+" if (valueChange > 0) else ""
    output += (f'\n${stockCurrent:3g} {changeDirection}{valueChange} ({changeDirection}{percentChange}%)\n')

    weeklyTrend = stock.history(period="5d")
    output += "Weekly Trend:\n"
    output += weeklyTrend.to_string() + '\n'

    return output


def getStockInfo(stockSymbol):
    # convert symbol to upper case
    stockSymbol = stockSymbol.upper()
    try:
        stock = yf.Ticker(stockSymbol)
        # print the current time
        date = datetime.datetime.now()
        print(date.strftime("%c"))  # %a %m %d %X %Z %Y

        # print the Company's name and ticker symbol
        stockInfo = stock.info
        print(stockInfo)
        print(f"{stockInfo['longName']} ({stockSymbol})")

        # Calculate and display the current price, value change and percent change
        stockPreviousClose = float(stockInfo['previousClose'])
        stockCurrent = float(stockInfo['open'])
        valueChange = round(stockCurrent - stockPreviousClose, 2)
        percentChange = round((valueChange / stockPreviousClose) * 100, 2)
        changeDirection = "+" if (valueChange > 0) else ""
        print(
            f'${stockCurrent} {changeDirection}{valueChange} ({changeDirection}{percentChange}%)')
    except:
        print("---ERROR: Invalid Ticker Symbol---")
