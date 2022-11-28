from PyQt5 import QtWidgets, uic, QtCore
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint
import csv

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('main_window.ui', self)
        self.plot()
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        t = []
        u = []
        t = x
        t = t[1:]
        t.append(t[-1]+50)

        u = y
        u = u[1:]
        u.append(randint(0,100))

        self.data_1.setData(t, u)
         
        
    def plot(self):
        global x, y
        x = []
        y = []
        checker = 0
        with open('sample4.csv','r') as file1:
            lines = csv.reader(file1, delimiter = ',')
            next(lines)
            for i in lines:
                xe = int(i[0])
                ye = int(i[1])
                x.append(xe)
                y.append(ye)

# I commented out the rest of the plots to just focus on the changing plot for the first widget

        self.widget.plot(x, y)
        self.data_1 = self.widget.plot(x, y)
        #self.widget_2.plot(x, y)
        #self.widget_3.plot(x, y)
        #self.widget_4.plot(x, y)
  
  


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


