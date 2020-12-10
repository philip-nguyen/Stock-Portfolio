# Index Investing
import yfinance as yf
import sys


class Logger():
    stdout = sys.stdout
    messages = []

    def start(self):
        sys.stdout = self

    def stop(self):
        sys.stdout = self.stdout

    def write(self, text):
        self.messages.append(text)


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

    log = Logger()
    log.start()
    # Selected stocks for Index Investing
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
        print("Money division: (25%) $", division, sep="")
        printStockInfo(stockSymbol1)

        print("-------------------------- Stock 2 --------------------------")
        division = float(investmentAmount*0.25)
        print("Money division: (25%) $", division, sep="")
        printStockInfo(stockSymbol2)

        print("-------------------------- Stock 3 --------------------------")
        division = float(investmentAmount*0.125)
        print("Money division: (12.5%) $", division, sep="")
        printStockInfo(stockSymbol3)

        print("-------------------------- Stock 4 --------------------------")
        division = float(investmentAmount*0.125)
        print("Money division: (12.5%) $", division, sep="")
        printStockInfo(stockSymbol4)

        print("-------------------------- Stock 5 --------------------------")
        division = float(investmentAmount*0.25)
        print("Money division: (25%) $", division, sep="")
        printStockInfo(stockSymbol5)

    except:
        print("-------------------------- ERROR: Invalid Ticker Symbol --------------------------")

    log.stop()
    message = " ".join(log.messages)
    return message
    #print("\nOUPUT\n", message)


def printStockInfo(stockSymbol):
    stock = yf.Ticker(stockSymbol)

    # Print the Company's name and ticker symbol
    stockInfo = stock.info
    print(f"{stockInfo['shortName']} ({stockSymbol})")

    # Get the current stock value
    # hist = stock.history(period="2d")
    # stockCurrent = float(hist['Open'])
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


print("--------------Output------------")
print(indexInvesting())
