from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QListWidgetItem
from PyQt5.QtGui import QColor
from PaintWidget import PaintWidget

class ColorHistory(QWidget):
    def __init__(self, paintWidget: PaintWidget):
        super().__init__()
        self._paintWidget = paintWidget
        self._addWidgets()
        self._linkActions()
        self.setFixedWidth(self.minimumSizeHint().width())

    def _addWidgets(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Color History (Click to Reuse)"))
        self.history = QListWidget()
        initialItem = QListWidgetItem("black", self.history)
        initialItem.setBackground(QColor("black"))
        layout.addWidget(self.history)
        self.setLayout(layout)

    def _linkActions(self):
        self.history.currentTextChanged.connect(self._reuseColor)

    def _reuseColor(self, color):
        self._paintWidget.setColor(QColor(color))

    def addColor(self, color):
        listItem = QListWidgetItem(color.name(), self.history)
        listItem.setBackground(color)
        self.history.clearSelection()
