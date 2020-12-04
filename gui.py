# PyQt5 widgets here
from PyQt5.QtWidgets import (QLineEdit, QLabel, QWidget, QCheckBox,
                             QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox)
import sys

class StockPortfolio(QWidget):

    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):

        # create the window
        # win = QMainWindow()
        # set the dimensions and window title
        # setGeometry(X, Y, width, height)
        self.setGeometry(400, 400, 300, 300)
        self.setWindowTitle("Stock Portfolio")

        # Add Label and LineEdit
        investmentLabel = QLabel(self)
        investmentLabel.setText("Amount ($):")
        investmentLabel.setStyleSheet("color: green")
        investmentLabel.adjustSize()
        investmentInput = QLineEdit(self)

        inputBox = QVBoxLayout()
        inputBox.addWidget(investmentLabel)
        inputBox.addWidget(investmentInput)

        # Checkboxes
        EthicalCheckBox = QCheckBox(self)
        EthicalCheckBox.setText("Ethical Investing")
        EthicalCheckBox.setStyleSheet("color: green")
        # EthicalCheckBox.stateChanged.connect(show)
        GrowthCheckBox = QCheckBox(self)
        GrowthCheckBox.setText("Growth Investing")
        GrowthCheckBox.setStyleSheet("color: green")
        IndexCheckBox = QCheckBox(self)
        IndexCheckBox.setText("Index Investing")
        IndexCheckBox.setStyleSheet("color: green")
        QualityCheckBox = QCheckBox(self)
        QualityCheckBox.setText("Quality Investing")
        QualityCheckBox.setStyleSheet("color: green")
        ValueCheckBox = QCheckBox(self)
        ValueCheckBox.setText("Value Investing")
        ValueCheckBox.setStyleSheet("color: green")

        checkBoxes = QVBoxLayout()
        inputBox.addWidget(EthicalCheckBox)
        inputBox.addWidget(GrowthCheckBox)
        inputBox.addWidget(IndexCheckBox)
        inputBox.addWidget(QualityCheckBox)
        inputBox.addWidget(ValueCheckBox)

        # Buttons for submit and reset
        submitButton = QPushButton('Submit')
        resetButton = QPushButton('Reset')
        resetButton.clicked.connect(investmentInput.clear)
        # submitButton.clicked.connect(self.showResult())

        endBox = QHBoxLayout()
        endBox.addWidget(submitButton)
        endBox.addWidget(resetButton)

        # Put all widgets together
        engineForm = QVBoxLayout()
        engineForm.addLayout(inputBox)
        # engineForm.addLayout(checkBoxes)
        engineForm.addLayout(endBox)

        self.setLayout(engineForm)
        # launch the simple PyQt window
        self.show()

    def showResult(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Stock Choices")
        msg.setText("Here's the stocks")
        msgBox = QVBoxLayout()
        msgBox.addWidget(msg)
        retval = msg.exec_()
