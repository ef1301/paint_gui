from PyQt5.QtWidgets import QLabel, QFileDialog
from PyQt5.QtGui import QPixmap, QColor, QPainter, QPen
from PyQt5.QtCore import Qt

class PaintWidget(QLabel):
    def __init__(self):
        super().__init__()

        self.clearImage()

        self.curPos = None
        self.curColor = QColor('black')
        self.curSize = 5
        self.colorChoices = ['black','red','yellow','blue']

    def mouseMoveEvent(self, event):
        if self.curPos is None:
            self.curPos = event.pos()
            return

        painter = QPainter(self.pixmap())
        painter.setPen(QPen(self.curColor, self.curSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        painter.drawLine(self.curPos, event.pos())
        painter.end()
        self.update()

        self.curPos = event.pos()

    def mouseReleaseEvent(self, event):
        self.curPos = None

    def setColor(self, color):
        self.curColor = QColor(self.colorChoices[color])

    def setBrushSize(self, size):
        self.curSize = size

    def clearImage(self):
        image = QPixmap(500, 500)
        image.fill(QColor("white"))
        self.setPixmap(image)

    def saveImage(self):
        fileName, _ = QFileDialog.getSaveFileName(self, "Save Image", "image.png", "PNG(*.png);;")

        if fileName.find(".png") > 0:
            self.pixmap().save(fileName)
        else:
            print("Invalid File Name")
