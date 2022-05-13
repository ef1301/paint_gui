from PyQt5.QtWidgets import QLabel, QFileDialog
from PyQt5.QtGui import QPixmap, QColor, QPainter, QPen
from PyQt5.QtCore import Qt, QSize

class PaintWidget(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignLeft)
        self.curImageSize = QSize(500, 500)
        self.setMinimumSize(self.curImageSize)
        self.clearImage()

        self.curPos = None
        self.curColor = QColor('black')
        self.curSize = 5
        self.colorChoices = ['black','red','yellow','blue']
        self.enlargeStyle = "extend"
        self.shrinkStyle = "crop"

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

    def setEnlargeStyle(self, style):
        self.enlargeStyle = style

    def setShrinkStyle(self, style):
        self.shrinkStyle = style

    def clearImage(self):
        image = QPixmap(self.curImageSize)
        image.fill(QColor("white"))
        self.setPixmap(image)

    def saveImage(self):
        fileName, _ = QFileDialog.getSaveFileName(self, "Save Image", "image.png", "PNG(*.png);;")

        if fileName.find(".png") > 0:
            self.pixmap().save(fileName)
        else:
            print("Invalid File Name")

    def extend(self):
        newImage = QPixmap(self.curImageSize)
        newImage.fill(QColor("white"))
        painter = QPainter(newImage)
        painter.drawPixmap(0, 0, self.pixmap())
        painter.end()
        self.setPixmap(newImage)

    def scale(self):
        newImage = self.pixmap().scaled(self.curImageSize)
        self.setPixmap(newImage)

    def resizeEvent(self, event):
        if (self.width() > self.curImageSize.width() or self.height() > self.curImageSize.height()):
            if self.enlargeStyle == "extend":
                self.extend()
            else:
                self.scale()
        else:
            if self.shrinkStyle == "crop":
                self.extend()
            else:
                self.scale()
        self.curImageSize = QSize(self.width(), self.height())
