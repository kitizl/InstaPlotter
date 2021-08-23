import sys


from PyQt5 import QtCore, QtGui, QtWidgets

app = QtWidgets.QApplication([])

w = QtGui.QWidget()

b = QtGui.QLabel(w)
b.setText("Hello World!")

headers = ['frequency','channel A', 'channel B']
xseries_selector = QtGui.QComboBox(headers)

w.setGeometry(100,100,200,50)
b.move(50,20)

w.setWindowTitle("PyQt Test")
w.show()
sys.exit(app.exec_())
