from PyQt5.QtWidgets import QMainWindow
from PaintWidget import PaintWidget

class PyPaintMainUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyPaint")
        self.move(100, 100)

        self._addWidgets()

    def _addWidgets(self):
        self.paintWidget = PaintWidget()
        self.setCentralWidget(self.paintWidget)
