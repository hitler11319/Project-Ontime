from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Clock(QWidget):
    def __init__(self):
        super().__init__()
        







class Ontime(QMainWindow):
    def __init__(self):
        super(Chat, self).__init__()
        self.setWindowTitle('ontime')

        self.clockArea = ClockArea()
        self.setCentralWidget(self.clockArea)

        self.createActions()

    def about(self):
        QMessageBox.about(self, "this is my work")


    def set_thing(self):
        pass
        
    def createActions(self):
        aboutAct = QAction("about", self)
        aboutAct.triggered.connect(self.about)


        setAct = QAction("set", self)
        setAct.triggered.connect(self.set_thing)


        self.statusBar()
        

        self.menuBar().addMenu('about').addAction(aboutAct)
        self.menuBar().addMenu('set').addAction(setAct)

        
        

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    clock = Ontime()
    clcok.show()
    sys.exit(app.exec_())
