from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QColor, QPainter

class PaintWidget(QLabel):
    def __init__(self):
        super().__init__()

        image = QPixmap(500, 500)
        image.fill(QColor("white"))
        self.setPixmap(image)

        self.curPos = None
        self.curColor = QColor('black')

    def mouseMoveEvent(self, event):
        if self.curPos is None:
            self.curPos = event.pos()
            return

        painter = QPainter(self.pixmap())
        pen = painter.pen()
        pen.setWidth(5)
        pen.setColor(self.curColor)
        painter.setPen(pen)
        painter.drawLine(self.curPos, event.pos())
        painter.end()
        self.update()

        self.curPos = event.pos()

    def mouseReleaseEvent(self, event):
        self.curPos = None
