# Quality Investing

import yfinance as yf
import datetime

def invest(invest)

    print("-------------------------- Quality Investing --------------------------")
    # Quality Investment Stocks Traits
    # Good Management - Ability to see opportunities and capitalize on them
    # Strong Balance Sheet - Ability to withstand adverse conditions or unexpected challenges 
    # Enterprise Life Cycle - In the global economy this company is always reinvesting in new technology 
    # Economic Moat - Barriers to entry for other competitors, advantages this particular has over other companies

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
        output = "Money division: (20%) $" + str(division) + "\n"
        print("Generating data from yfinance...")
        output += printStockInfo(stockSymbol1) + "\n"

        print("-------------------------- Stock 2 --------------------------")
        division = float(investmentAmount*0.2)
        output += "Money division: (20%) $" + str(division) + "\n"
        print("Generating data from yfinance...")
        output += printStockInfo(stockSymbol2) + "\n"

        print("-------------------------- Stock 3 --------------------------")
        division = float(investmentAmount*0.2)
        output += "Money division: (20%) $" + str(division) + "\n"
        print("Generating data from yfinance...")
        output += printStockInfo(stockSymbol3) + "\n"

        print("-------------------------- Stock 4 --------------------------")
        division = float(investmentAmount*0.2)
        output += "Money division: (20%) $" + str(division) + "\n"
        print("Generating data from yfinance...")
        output += printStockInfo(stockSymbol4) + "\n"

        print("-------------------------- Stock 5 --------------------------")
        division = float(investmentAmount*0.2)
        output += "Money division: (20%) $" + str(division) + "\n"
        print("Generating data from yfinance...")
        output += printStockInfo(stockSymbol5) + "\n"
        output += "\n\n"

    except:
        print("-------------------------- ERROR: Invalid Ticker Symbol --------------------------")
        return "Error in Quality Investing \n"

    return output 


def printStockInfo(stockSymbol):
    stock = yf.Ticker(stockSymbol)

    # Print the Company's name and ticker symbol
    stockInfo = stock.info
    output = (f"{stockInfo['shortName']} ({stockSymbol})")

    # Get the current stock value
    stockCurrent = float(stockInfo['open'])

    # Get the previous close value
    stockPreviousClose = float(stockInfo['previousClose'])

    # Calculate the current price, value change and percent change
    valueChange = round(stockCurrent - stockPreviousClose, 2)
    percentChange = round((valueChange / stockPreviousClose) * 100, 2)
    changeDirection = "+" if (valueChange > 0) else ""
    output += (f'\n${stockCurrent:3g} {changeDirection}{valueChange} ({changeDirection}{percentChange}%)', "\n")

    weeklyTrend = stock.history(period="5d")
    output += ("Weekly Trend:\n")
    output += weeklyTrend.toString() + '\n'

    return output

