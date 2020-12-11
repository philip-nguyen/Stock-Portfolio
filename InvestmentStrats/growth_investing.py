# Growth Investing

import yfinance as yf
import datetime 

def invest(investmentAmount):
    print("-------------------------- Growth Investing --------------------------\n")
    # Stocks you buy because you believe the stock's price could increase substantially -- usually an uncapped amount with enormous upside potential
    # Traits: Market capitalization less than $20 billion
    # Revenue growth of at least 20% over the past three years
    # An antifragile balance sheet that will allow it to grow stronger in the face of economic crises 
    # Founder-led companies where insiders own lots of stock 
    # An identifiable moat protecting the company from its competition
    

    # Selected stocks for Growth Investing
    # Mercadolibre - leading e-commerce player in Latin America
    stockSymbol1 = "MELI"
    stockSymbol1 = stockSymbol1.upper()

    # Axon - stun gun and law enforcement body cam producer 
    stockSymbol2 = "AAXN"
    stockSymbol2 = stockSymbol2.upper()

    # Shopify - E-commerce operations platform for merchants
    stockSymbol3 = "SHOP"
    stockSymbol3 = stockSymbol3.upper()

    # Ellie Mae - Mortage-industry software provider
    stockSymbol4 = "EFC"
    stockSymbol4 = stockSymbol4.upper()

    # Paycom - HR department manager
    stockSymbol5 = "PAYC"
    stockSymbol5 = stockSymbol5.upper()


    try:
        print("-------------------------- Stock 1 --------------------------")
        division = float(investmentAmount*0.2)
        output = "Money division: (20%) $" + str(division) + "\n"
        print("Generating data from yfinance...")
        output += printStockInfo(stockSymbol1) + "\n"

        print("-------------------------- Stock 2 --------------------------")
        division = float(investmentAmount*0.2)
        output = "Money division: (20%) $" + str(division) + "\n"
        print("Generating data from yfinance...")
        output += printStockInfo(stockSymbol2) + "\n"

        print("-------------------------- Stock 3 --------------------------")
        division = float(investmentAmount*0.2)
        output = "Money division: (20%) $" + str(division) + "\n"
        print("Generating data from yfinance...")
        output += printStockInfo(stockSymbol3) + "\n"

        print("-------------------------- Stock 4 --------------------------")
        division = float(investmentAmount*0.2)
        output = "Money division: (20%) $" + str(division) + "\n"
        print("Generating data from yfinance...")
        output += printStockInfo(stockSymbol4) + "\n"

        print("-------------------------- Stock 5 --------------------------")
        division = float(investmentAmount*0.2)
        output = "Money division: (20%) $" + str(division) + "\n"
        print("Generating data from yfinance...")
        output += printStockInfo(stockSymbol5) + "\n"

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
    output += (f'${stockCurrent:3g} {changeDirection}{valueChange} ({changeDirection}{percentChange}%)', "\n")

    weeklyTrend = stock.history(period="5d")
    output += ("Weekly Trend:\n")
    output += (weeklyTrend.toString(), '\n')

    return output

