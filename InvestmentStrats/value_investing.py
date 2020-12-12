# Value Investing
import yfinance as yf
import datetime

"""
    The invest function takes in an investment amount
    and returns a string var
"""


def invest(investmentAmount):
    print("-------------------------- Value Investing --------------------------\n")
    # Value Investing - investing in stocks that appear to be trading for less than their actual value.

    output = "------------ Value Investing ------------\n"
    output += f'Amount for Strategy: ${investmentAmount}\n'
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
        output += "Money division: (40%) $" + str(division) + "\n"
        print("Generating data from yfinance...")
        output += printStockInfo(stockSymbol1) + "\n"

        print("-------------------------- Stock 2 --------------------------")
        division = float(investmentAmount*0.20)
        output += "Money division: (20%) $" + str(division) + "\n"
        print("Generating data from yfinance...")
        output += printStockInfo(stockSymbol2) + "\n"

        print("-------------------------- Stock 3 --------------------------")
        division = float(investmentAmount*0.20)
        output += "Money division: (20%) $" + str(division) + "\n"
        print("Generating data from yfinance...")
        output += printStockInfo(stockSymbol3) + "\n"

        print("-------------------------- Stock 4 --------------------------")
        division = float(investmentAmount*0.10)
        output += "Money division: (10%) $" + str(division) + "\n"
        print("Generating data from yfinance...")
        output += printStockInfo(stockSymbol4) + "\n"

        print("-------------------------- Stock 5 --------------------------")
        division = float(investmentAmount*0.10)
        output += "Money division: (10%) $" + str(division) + "\n"
        print("Generating data from yfinance...")
        output += printStockInfo(stockSymbol5) + "\n"
        output += "\n\n"

    except:
        print("-------------------------- ERROR: Invalid Ticker Symbol --------------------------")
        return "Error in Value Investing :(\n"

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
