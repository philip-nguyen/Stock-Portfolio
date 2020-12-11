# Main Function
import gui
import sys
from PyQt5.QtWidgets import QApplication


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# initialize
app = QApplication(sys.argv)

win = gui.StockPortfolio()


sys.exit(app.exec_())   # compulsory line to "cleanly exit"
