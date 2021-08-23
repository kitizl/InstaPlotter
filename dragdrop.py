from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import pyqtgraph as pg
import pandas as pd
import matplotlib.pyplot as plt

class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drag and Drop")
        self.resize(720, 480)
        self.setAcceptDrops(True)

        self.files = []

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        self.files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            dataFrame = pd.read_csv(f) # reading the data
            print(dataFrame.head())
            headers = dataFrame.columns





            xSeries = dataFrame[headers[0]]
            #plotWidget = pg.plot(title="Plot")
            for i,head in enumerate(headers[1:]):
                #plotWidget.plot(xSeries, dataFrame[head], pen=(i,len(headers)-1))
                plt.scatter(xSeries, dataFrame[head])
            plt.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWidget()
    ui.show()
    sys.exit(app.exec_())