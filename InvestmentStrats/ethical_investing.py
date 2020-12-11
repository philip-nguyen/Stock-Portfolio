# Ethical Investing
import yfinance as yf
import datetime

"""
    The invest function takes in an investment amount
    and returns a string var
"""
def invest(investmentAmount):
    # Ethical Investing - investing in companies that promote
    # ethical practices and ethical products.
    # Choices include prominent wind energy companies

    # General Electric - electric company
    stockSymbol1 = "NEE"
    stockSymbol1 = stockSymbol1.upper()

    # NextEra Energy Inc - generates electricity through wind, solar and natural gas
    stockSymbol2 = "GE"
    stockSymbol2 = stockSymbol2.upper()

    # Northland Power Inc - diversified energy company with assets in wind, natural gas and solar
    stockSymbol3 = "NPIFF"
    stockSymbol3 = stockSymbol3.upper()

    try:
        print("-------------------------- Stock 1 --------------------------")
        division = float(investmentAmount*0.6)
        output = "Money division: (60%) $" + str(division) + "\n"
        print("Generating data from yfinance...")
        output += printStockInfo(stockSymbol1) + "\n"

        print("-------------------------- Stock 2 --------------------------")
        division = float(investmentAmount * 0.2)
        output += "Money division: (20%) $" + str(division) + "\n"
        print("Generating data from yfinance...")
        output += printStockInfo(stockSymbol2) + "\n"

        print("-------------------------- Stock 3 --------------------------")
        division = float(investmentAmount * 0.2)
        output += "Money division: (20%) $" + str(division) + "\n"
        print("Generating data from yfinance...")
        output += printStockInfo(stockSymbol3) + "\n"
        output += "\n\n"

    except:
        print("-------------------------- ERROR: Invalid Ticker Symbol --------------------------")
        return "Error in Ethical Investing :(\n"

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
    print(weeklyTrend)
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
        print(stockInfo);
        print(f"{stockInfo['longName']} ({stockSymbol})")

        # Calculate and display the current price, value change and percent change
        stockPreviousClose = float(stockInfo['previousClose'])
        stockCurrent = float(stockInfo['open'])
        valueChange = round(stockCurrent - stockPreviousClose, 2)
        percentChange = round((valueChange / stockPreviousClose) * 100, 2)
        changeDirection = "+" if (valueChange > 0) else ""
        print(f'${stockCurrent} {changeDirection}{valueChange} ({changeDirection}{percentChange}%)')
    except:
        print("---ERROR: Invalid Ticker Symbol---")