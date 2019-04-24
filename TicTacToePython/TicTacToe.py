'''
Created on Apr 22, 2019

@author: Jesse Bahr

@
'''
    
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Square(QWidget):
    
    def __init__(self, x, y, *args, **kwargs):
        super(Square, self).__init__(*args, **kwargs)
    
        self.setFixedSize(QSize(100, 100))
    
        self.x = x
        self.y = y
        
        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(self.x, self.y)
#         button.clicked.connect(self.on_click)

        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        #sizePolicy.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
        button.setSizePolicy(sizePolicy)
        
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(QPen(Qt.black, 10, Qt.SolidLine))
        
        qp.drawLine(10, 10, 20, 20)
        qp.end()




class TicTacToeWindow(QMainWindow):
    
    PLAYER_WIN_SCORE   = 10
    COMPUTER_WIN_SCORE = -10
    TIE_SCORE          = 0
    
    def __init__(self, *args, **kwargs):  
        super(TicTacToeWindow, self).__init__(*args, **kwargs)
        
        # Set the sides of the application
        self.top    = 100
        self.left   = 100
        self.right  = 700
        self.bottom = 500   
        
        w = QWidget()     
         
        hBox = QHBoxLayout()
        vBox = QVBoxLayout()
         
        vBox.addLayout(hBox)
 
        self.grid = QGridLayout()
        self.grid.setSpacing(1)
 
        vBox.addLayout(self.grid)
        w.setLayout(vBox)
        self.setCentralWidget(w)
 
        self.init_map()
         
        self.setGeometry(self.top, self.left, self.right, self.bottom)
        self.setWindowTitle("Tic Tac Toe")

        self.show()       
        
    def init_map(self):
        # Add positions to the map
        for x in range(0, 3):
            for y in range(0, 3):
                w = Square(x, y)
                self.grid.addWidget(w, y, x)
                       
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        
        qp.drawLine(10, self.get_height()/3, self.get_width() - 10, self.get_height()/3)
        qp.drawLine(10, (self.get_height()*2)/3, self.get_width() - 10, (self.get_height()*2)/3)
        qp.drawLine(self.get_width()/3, 10, self.get_width()/3, self.get_height() - 10)
        qp.drawLine((self.get_width()*2)/3, 10, (self.get_width()*2)/3, self.get_height() - 10)
        qp.end()
        
    def get_height(self):
        return self.bottom - self.top
    
    def get_width(self):
        return self.right - self.left

    
if __name__ == '__main__':
    
    app = QApplication([])
    window = TicTacToeWindow()
    app.exec_()