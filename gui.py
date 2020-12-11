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
        self.investmentLabel.setText("Amount ($):")
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

        self.resetButton.clicked.connect(self.investmentInput.clear)
        self.resetButton.clicked.connect(self.outputArea.clear)
        self.submitButton.clicked.connect(self.computeStockPortfolio)
        # self.submitButton.clicked.connect(self.outputArea.clear)

        endBox = QHBoxLayout()
        endBox.addWidget(self.submitButton)
        endBox.addWidget(self.resetButton)

        resultBox = QVBoxLayout()
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

        try:
            investmentAmount = int(self.investmentInput.text())
            self.output = ''
            if self.EthicalCheckBox.isChecked():
                # Start thread to do yfinance API calls
                thread_e = threading.Thread(
                    target=self.setOutput, args=(ethical_investing.invest,))
                thread_e.start()
                thread_e.join()

            if self.GrowthCheckBox.isChecked():
                # TODO: change args to growth_investing.invest function
                thread_g = threading.Thread(
                    target=self.setOutput, args=(ethical_investing.invest,))
                thread_g.start()
                thread_g.join()

            if self.IndexCheckBox.isChecked():
                thread_i = threading.Thread(
                    target=self.setOutput, args=(index_investing.invest,))
                thread_i.start()
                thread_i.join()

            if self.QualityCheckBox.isChecked():
                # TODO: change args to quality_investing.invest function
                thread_q = threading.Thread(
                    target=self.setOutput, args=(ethical_investing.invest,))
                thread_q.start()
                thread_q.join()

            if self.ValueCheckBox.isChecked():
                # TODO: change args to value_investing.invest function
                thread_v = threading.Thread(
                    target=self.setOutput, args=(value_investing.invest,))
                thread_v.start()
                thread_v.join()

        except:
            print("ERROR :(")

        self.showTextAreaResult(self.output)

    def setOutput(self, investmentStrat):
        investmentAmount = int(self.investmentInput.text())
        # storing the function in a var
        investmentOutput = investmentStrat(investmentAmount)
        self.output += investmentOutput

    def showTextAreaResult(self, output):
        self.outputArea.insertPlainText(output)
        self.outputArea.setFont(QFont('Monopace', 10, QFont.Monospace))
