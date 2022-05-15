from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
from PaintWidget import PaintWidget
from Settings import Settings
from ColorHistory import ColorHistory

class PyPaintMainUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyPaint")
        self.move(100, 100)

        self._addWidgets()

    def _addWidgets(self):
        mainLayout = QVBoxLayout()

        self.paintWidget = PaintWidget()
        mainLayout.addWidget(self.paintWidget)

        mainLayout.addSpacing(1)

        self.colorHistory = ColorHistory(self.paintWidget)
        self.settings = Settings(self.paintWidget, self.colorHistory)

        mainLayout.addWidget(self.settings)

        columnLayout = QHBoxLayout()
        columnLayout.addLayout(mainLayout)
        columnLayout.addSpacing(10)
        columnLayout.addWidget(self.colorHistory)

        widget = QWidget()
        widget.setLayout(columnLayout)

        self.setCentralWidget(widget)
