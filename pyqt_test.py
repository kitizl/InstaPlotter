#!python3
from PyQt5 import QtGui
import pyqtgraph as pg
import pandas as pd
import numpy as np

app = QtGui.QApplication([])

plotWidget = pg.PlotWidget()


w = QtGui.QWidget()
#uploadBtn = QtGui.QPressButton('Upload')


x = np.random.normal(size=10000)
y = np.random.normal(size=10000)


plotWidget.plot(x,y,pen=None, symbol='o')

layout = QtGui.QGridLayout()
w.setLayout(layout)

layout.addWidget(plotWidget, 0,0)

w.show()
app.exec_()