# PyQt5 widgets here
from PyQt5.QtWidgets import (QLineEdit, QLabel, QWidget, QCheckBox, QPlainTextEdit,
                             QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox)
from PyQt5.QtGui import QFont
from InvestmentStrats import (ethical_investing, growth_investing, index_investing,
                              quality_investing, value_investing)
import threading
import sys


class StockPortfolio(QWidget):

    def __init__(self):
        super().__init__()
        self.investmentLabel = QLabel(self)
        self.investmentInput = QLineEdit(self)
        self.EthicalCheckBox = QCheckBox(self)
        self.GrowthCheckBox = QCheckBox(self)
        self.IndexCheckBox = QCheckBox(self)
        self.QualityCheckBox = QCheckBox(self)
        self.ValueCheckBox = QCheckBox(self)
        self.submitButton = QPushButton('Submit')
        self.resetButton = QPushButton('Reset')
        self.infoButton = QPushButton('Info')
        self.outputArea = QPlainTextEdit(self)
        self.output = ''
        self.UI()

    def UI(self):

        # create the window
        # win = QMainWindow()
        # set the dimensions and window title
        # setGeometry(X, Y, width, height)
        self.setGeometry(50, 100, 725, 700)
        self.setWindowTitle("Stock Portfolio")

        # Add Label and LineEdit
        # investmentLabel = QLabel(self)
        self.investmentLabel.setText("Amount (> $5000):")
        self.investmentLabel.setStyleSheet("color: green")
        # self.investmentLabel.adjustSize()
        # self.investmentInput = QLineEdit(self)

        inputBox = QVBoxLayout()
        inputBox.addWidget(self.investmentLabel)
        inputBox.addWidget(self.investmentInput)

        # Checkboxes

        self.EthicalCheckBox.setText("Ethical Investing")
        self.EthicalCheckBox.setStyleSheet("color: green")

        self.GrowthCheckBox.setText("Growth Investing")
        self.GrowthCheckBox.setStyleSheet("color: green")

        self.IndexCheckBox.setText("Index Investing")
        self.IndexCheckBox.setStyleSheet("color: green")

        self.QualityCheckBox.setText("Quality Investing")
        self.QualityCheckBox.setStyleSheet("color: green")

        self.ValueCheckBox.setText("Value Investing")
        self.ValueCheckBox.setStyleSheet("color: green")

        checkBoxes = QVBoxLayout()
        checkBoxes.addWidget(self.EthicalCheckBox)
        checkBoxes.addWidget(self.GrowthCheckBox)
        checkBoxes.addWidget(self.IndexCheckBox)
        checkBoxes.addWidget(self.QualityCheckBox)
        checkBoxes.addWidget(self.ValueCheckBox)

        # Buttons for submit and reset

        self.resetButton.clicked.connect(self.resetForm)
        self.submitButton.clicked.connect(self.outputArea.clear)
        self.submitButton.clicked.connect(self.computeStockPortfolio)
        self.infoButton.clicked.connect(self.displayInfo)

        endBox = QHBoxLayout()
        endBox.addWidget(self.submitButton)
        endBox.addWidget(self.resetButton)
        endBox.addWidget(self.infoButton)

        resultBox = QVBoxLayout()
        self.outputArea.setReadOnly(True)
        resultBox.addWidget(self.outputArea)

        # Put all widgets together
        engineForm = QVBoxLayout()
        engineForm.addLayout(inputBox)
        engineForm.addLayout(checkBoxes)
        engineForm.addLayout(endBox)
        engineForm.addLayout(resultBox)

        self.setLayout(engineForm)
        # launch the simple PyQt window
        self.show()

    def computeStockPortfolio(self):
        self.output = ''
        numChecked = self.EthicalCheckBox.isChecked() + self.GrowthCheckBox.isChecked() \
                + self.IndexCheckBox.isChecked() + self.QualityCheckBox.isChecked() \
                + self.ValueCheckBox.isChecked()
        try:
            # IF there is 1-2 check boxes checked and there is an investment input
            if 0 < numChecked <= 2 and self.investmentInput.text() \
                    and float(self.investmentInput.text()) >= 5000.0:

                if self.EthicalCheckBox.isChecked():
                    # Start thread to do yfinance API calls
                    thread_e = threading.Thread(
                        target=self.setOutput, args=(ethical_investing.invest, numChecked,))
                    thread_e.start()
                    thread_e.join()

                if self.GrowthCheckBox.isChecked():
                    thread_g = threading.Thread(
                        target=self.setOutput, args=(growth_investing.invest, numChecked,))
                    thread_g.start()
                    thread_g.join()

                if self.IndexCheckBox.isChecked():
                    thread_i = threading.Thread(
                        target=self.setOutput, args=(index_investing.invest, numChecked,))
                    thread_i.start()
                    thread_i.join()

                if self.QualityCheckBox.isChecked():
                    thread_q = threading.Thread(
                        target=self.setOutput, args=(quality_investing.invest, numChecked,))
                    thread_q.start()
                    thread_q.join()

                if self.ValueCheckBox.isChecked():
                    thread_v = threading.Thread(
                        target=self.setOutput, args=(value_investing.invest, numChecked,))
                    thread_v.start()
                    thread_v.join()

            elif not self.investmentInput.text():
                self.showTextAreaResult("Error: No Investment Input...\nPlease input an Investment")
            elif float(self.investmentInput.text()) < 5000.0:
                self.showTextAreaResult("Error: Minimum Investment is $5000")
            elif numChecked > 2:
                self.showTextAreaResult("Error: Please select only 2 Investment Strategies")
            elif numChecked <= 0:
                self.showTextAreaResult("Error: Please select 1-2 Investment Strategies")


        except:
            print("ERROR :(")

        self.showTextAreaResult(self.output)

    def setOutput(self, investmentStrat, numChecked):
        # Split the investment evenly between the strategies
        investmentAmount = float(self.investmentInput.text()) / numChecked
        # storing the function in a var
        investmentOutput = investmentStrat(investmentAmount)
        self.output += investmentOutput

    def showTextAreaResult(self, output):
        self.outputArea.insertPlainText(output)
        self.outputArea.setFont(QFont('Monopace', 12, QFont.Monospace))

    def resetForm(self):
        self.EthicalCheckBox.setChecked(False)
        self.GrowthCheckBox.setChecked(False)
        self.IndexCheckBox.setChecked(False)
        self.QualityCheckBox.setChecked(False)
        self.ValueCheckBox.setChecked(False)
        self.investmentInput.clear()
        self.outputArea.clear()

    def displayInfo(self):
        infoMsg = QMessageBox()
        # infoMsg.setIcon(QMessageBox.Information)
        infoMsg.setFont(QFont('Monopace', 12, QFont.Monospace))
        infoMsg.setStyleSheet("color: white; min-width: 600px")

        infoMsg.setWindowTitle("Information")

        ethical = "Ethical Investing:\n" \
                  "Uses the practice of using one's ethical principles as the primary " \
                  "filter for the selection of securities investing\n" \
                  "Mappings:\nNEE - NextEra Energy Inc\nGE - General Electic\nNPIFF - Northland Power Inc\n\n"
        growth = "Growth Investing:\n" \
                 "A stock-buying strategy that focuses on companies " \
                 "expected to grow at an above-average rate compared to their industry or the market.\n" \
                 "Mappings:\nMELI - Mercadolibre\nAAXN - Axon\nSHOP - Shopify\nEFC - Ellie Mae\nPAYC - Paycom\n\n"
        index = "Index Investing:\n" \
                "A passive investment strategy that seeks to " \
                "replicate the returns of a benchmark index.\n" \
                "Mappings:\n^NSEI - Nat Stock Exchange of India Index\n^FCHI - French Stock Market Index\n" \
                "^GSPTSE - Canada's largest stock exchange\nIMOEX.ME - Russian Stock Market Index\n" \
                "^RUT - Index of stocks with small market capitalization\n\n"
        quality = "Quality Investing:\n" \
                  "An investment strategy based on a set of clearly defined fundamental " \
                  "criteria that seeks to identify companies with outstanding quality characteristics\n" \
                  "Mappings:\nV - Visa\nAMZN - Amazon\nMSFT - Microsoft\nCRM - Salesforce\nNKE - Nike\n\n"
        value = "Value Investing:\n" \
                "An investment strategy that involves picking stocks that appear to be " \
                "trading for less than their intrinsic or book value.\n" \
                "Mappings:\nQMF - Consumer credit and insurance\nPAG - Auto-dealer\nCVS - Customer Value Store\n" \
                "ABBV - Drug developer\nINGR - Ingredient Vendor\n\n"

        infoMsg.setText(ethical + growth + index + quality + value)
        retval = infoMsg.exec_()