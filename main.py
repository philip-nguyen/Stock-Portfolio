# Main Function
import gui
import sys
from PyQt5.QtWidgets import QApplication

# initialize
app = QApplication(sys.argv)

win = gui.StockPortfolio()


sys.exit(app.exec_())   # compulsory line to "cleanly exit"
