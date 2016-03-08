from PyQt5.QtCore import QPoint, Qt, QTime, QTimer
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Clock(QWidget):
    hourHand = QPolygon([
        QPoint(7, 8),
        QPoint(-7, 8),
        QPoint(0, -40)
    ])

    minuteHand = QPolygon([
        QPoint(7, 8),
        QPoint(-7, 8),
        QPoint(0, -70)
    ])

    hourColor = QColor(127, 127, 127)
    minuteColor = QColor(0, 152, 127, 191)

    def __init__(self, parent=None):
        super(Clock, self).__init__(parent)

        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)


    def paintEvent(self, event):
        side = min(self.width(), self.height())
        time = QTime.currentTime()

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)
        painter.scale(side / 200.0, side / 200.0)

        painter.setPen(Qt.NoPen)
        painter.setBrush(Clock.hourColor)

        painter.save()
        painter.rotate(30.0 * ((time.hour() + time.minute() / 60.0)))
        painter.drawConvexPolygon(Clock.hourHand)
        painter.restore()

        painter.setPen(Clock.hourColor)

        for i in range(12):
            painter.drawLine(88, 0, 96, 0)
            painter.rotate(30.0)

        painter.setPen(Qt.NoPen)
        painter.setBrush(Clock.minuteColor)

        painter.save()
        painter.rotate(6.0 * (time.minute() + time.second() / 60.0))
        painter.drawConvexPolygon(Clock.minuteHand)
        painter.restore()

        painter.setPen(Clock.minuteColor)

        for j in range(60):
            if (j % 5) != 0:
                painter.drawLine(92, 0, 96, 0)
            painter.rotate(6.0)
        

class Ontime(QMainWindow):
    def __init__(self):
        super(Ontime, self).__init__()
        self.setWindowTitle('ontime')

        self.clockArea = Clock()
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
    clock.show()
    sys.exit(app.exec_())

