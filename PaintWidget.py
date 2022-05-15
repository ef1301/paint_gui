from PyQt5.QtWidgets import QLabel, QFileDialog, QColorDialog
from PyQt5.QtGui import QPixmap, QColor, QPainter, QPen, QCursor
from PyQt5.QtCore import Qt, QSize, QPoint, QPointF
import random

class PaintWidget(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignLeft)
        self.curImageSize = QSize(500, 500)
        self.setMinimumSize(self.curImageSize)
        self.clearImage()

        self.curPos = None
        self.brushStyle = "solid"
        self.curColor = QColor('black')
        self.curSize = 15
        self.enlargeStyle = "extend"
        self.shrinkStyle = "crop"

        self.showCursor = True
        self.updateCustomCursor()

    def updateCustomCursor(self):
        pointer = QPixmap(100, 100)
        pointer.fill(Qt.transparent)
        painter = QPainter(pointer)
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        painter.setBrush(self.curColor)
        painter.drawEllipse(QPoint(50, 50), self.curSize / 2, self.curSize / 2)
        painter.end()
        cursor = QCursor(pointer)
        if self.showCursor and self.brushStyle != "spray":
            self.setCursor(cursor)
        else:
            self.unsetCursor()

    def mousePressEvent(self, event):
        if self.brushStyle != "spray":
            self.curPos = event.pos()
            painter = QPainter(self.pixmap())
            painter.setPen(QPen(self.curColor, self.curSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawPoint(self.curPos)
            painter.end()
            self.update()

    def mouseMoveEvent(self, event):
        painter = QPainter(self.pixmap())
        if self.brushStyle == "spray":
            painter.setPen(QPen(self.curColor, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            for n in range(50):
                p = QPointF(random.gauss(0, self.curSize)/2, random.gauss(0, self.curSize)/2)
                painter.drawPoint(event.pos() + p)
        else:
            painter.setPen(QPen(self.curColor, self.curSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.curPos, event.pos())
            self.curPos = event.pos()
        painter.end()
        self.update()

    def mouseReleaseEvent(self, event):
        self.curPos = None

    def setShowCursor(self, val):
        self.showCursor = val
        self.updateCustomCursor()

    def setColor(self, color):
        if self.brushStyle == "erase":
            self.oldColor = color
        else:
            self.curColor = color
            self.updateCustomCursor()

    def setBrushSize(self, size):
        self.curSize = size
        self.updateCustomCursor()

    def setStyle(self, style):
        if self.brushStyle == "erase":
            self.curColor = self.oldColor
        elif style == "erase":
            self.oldColor = self.curColor
            self.curColor = QColor("white")
        self.brushStyle = style
        self.updateCustomCursor()

    def setEnlargeStyle(self, style):
        self.enlargeStyle = style

    def setShrinkStyle(self, style):
        self.shrinkStyle = style

    def changeColor(self):
        color = QColorDialog.getColor()
        self.setColor(color)
        return color

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
        tempImageSize = self.curImageSize
        self.curImageSize = QSize(self.width(), self.height())
        if (self.width() > tempImageSize.width() or self.height() > tempImageSize.height()):
            if self.enlargeStyle == "extend":
                self.extend()
            else:
                self.scale()
        else:
            if self.shrinkStyle == "crop":
                self.extend()
            else:
                self.scale()
