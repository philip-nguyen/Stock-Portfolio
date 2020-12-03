# Ethical Investing
import yfinance as yf
import datetime


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