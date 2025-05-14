from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QGridLayout
from PyQt5 import uic
import sys
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        #Load ui file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file = os.path.join(script_dir, "tictactoe.ui")
        uic.loadUi(ui_file, self)
        
        #set counter for turns
        self.turn = 0

        self.label0 = self.findChild(QLabel, "label0")
        self.resetButton = self.findChild(QPushButton, "resetButton")

        # 00 01 02
        # 10 11 12
        # 20 21 22

        #first row
        self.zero0 = self.findChild(QPushButton, "zero0")
        self.zero1 = self.findChild(QPushButton, "zero1")
        self.zero2 = self.findChild(QPushButton, "zero2")
        #second row
        self.one0 = self.findChild(QPushButton, "one0")
        self.one1 = self.findChild(QPushButton, "one1")
        self.one2 = self.findChild(QPushButton, "one2")
        #third row
        self.two0 = self.findChild(QPushButton, "two0")
        self.two1 = self.findChild(QPushButton, "two1")
        self.two2 = self.findChild(QPushButton, "two2")


        #trigger actions
        self.zero0.clicked.connect(lambda: self.gridFill(self.zero0))
        self.zero1.clicked.connect(lambda: self.gridFill(self.zero1))
        self.zero2.clicked.connect(lambda: self.gridFill(self.zero2))

        self.one0.clicked.connect(lambda: self.gridFill(self.one0))
        self.one1.clicked.connect(lambda: self.gridFill(self.one1))
        self.one2.clicked.connect(lambda: self.gridFill(self.one2))

        self.two0.clicked.connect(lambda: self.gridFill(self.two0))
        self.two1.clicked.connect(lambda: self.gridFill(self.two1))
        self.two2.clicked.connect(lambda: self.gridFill(self.two2))

        self.resetButton.clicked.connect(lambda: self.startOver())

        #Show
        self.show()


    def gridFill(self, gridUnit):
        if self.turn % 2 == 0:
            mark = "X"
            outStatement = "O's Turn!"
        else:
            mark = "O"
            outStatement = "X's Turn!"

        gridUnit.setText(mark)
        gridUnit.setEnabled(False)

        self.label0.setText(outStatement) 
        self.turn += 1

        #Check win
        self.checkWin()


    
    def checkWin(self):
        self.khichdi()
        # 00 01 02
        # 10 11 12
        # 20 21 22

        #Across Horizontally
        '''
        - - -
        - - -
        - - -
        '''
        #first row
        if self.zero0.text() and self.zero0.text() == self.zero1.text() == self.zero2.text():
           self.win(self.zero0, self.zero1, self.zero2)

        #Second row
        if self.one0.text() and self.one0.text() == self.one1.text() == self.one2.text():
           self.win(self.one0, self.one1, self.one2)

        #Third row
        if self.two0.text() and self.two0.text() == self.two1.text() == self.two2.text():
           self.win(self.two0, self.two1, self.two2)

        #Across Vertically
        '''
        | | |
        | | |
        | | |
        '''

        #first col
        if self.zero0.text() and self.zero0.text() == self.one0.text() == self.two0.text():
           self.win(self.zero0, self.one0, self.two0)

        #Second col
        if self.zero1.text() and self.zero1.text() == self.one1.text() == self.two1.text():
           self.win(self.zero1, self.one1, self.two1)

        #Third col
        if self.zero2.text() and self.zero2.text() == self.one2.text() == self.two2.text():
           self.win(self.zero2, self.one2, self.two2)

        #Across Diagonally
        '''

        LEFT
        \ - -
        - \ -
        - - \ 

        OR

        RIGHT
        - - /
        - / -
        / - -

        '''
        #left diagonal
        if self.zero0.text() and self.zero0.text() == self.one1.text() == self.two2.text():
           self.win(self.zero0, self.one1, self.two2)

        #right diagonal
        if self.zero2.text() and self.zero2.text() == self.one1.text() == self.two0.text():
           self.win(self.zero2, self.one1, self.two0)




    def win(self, gridUnitA,gridUnitB,gridUnitC):
        #Change color to green
        gridUnitA.setStyleSheet('QPushButton {color: green;}')
        gridUnitB.setStyleSheet('QPushButton {color: green;}')
        gridUnitC.setStyleSheet('QPushButton {color: green;}')

        #Winner Label
        self.label0.setText(f"{gridUnitA.text()} Wins!!!")

        #Freeze the board
        self.freeze()

    def khichdi(self):
        if (
            self.zero0.text() and self.zero1.text() and self.zero2.text() and
            self.one0.text() and self.one1.text() and self.one2.text() and
            self.two0.text() and self.two1.text() and self.two2.text()
        ):
            self.label0.setText("It's a Draw!")
            self.freeze()

    def freeze(self):
        gridUnits = [
            self.zero0, self.zero1, self.zero2, 
            self.one0, self.one1, self.one2, 
            self.two0, self.two1, self.two2
        ]
        for gridUnit in gridUnits:
            gridUnit.setEnabled(False)


    def startOver(self):
        gridUnits = [
            self.zero0, self.zero1, self.zero2, 
            self.one0, self.one1, self.one2, 
            self.two0, self.two1, self.two2
        ]
        for gridUnit in gridUnits:
            gridUnit.setText("")
            gridUnit.setEnabled(True)

            #Reset the color
            gridUnit.setStyleSheet('QPushButton {color: #797979;}')  #797979 default color

        #Reset the counter
        self.turn = 0

        #Reset the label
        self.label0.setText("X Goes First!")


app = QApplication(sys.argv)
ui = MainWindow()
app.exec_()
