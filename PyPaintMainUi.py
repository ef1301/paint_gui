from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QComboBox
from PaintWidget import PaintWidget

class PyPaintMainUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyPaint")
        self.move(100, 100)

        self._addWidgets()
        self._linkButtons()

    def _addWidgets(self):
        mainLayout = QVBoxLayout()

        self.paintWidget = PaintWidget()
        mainLayout.addWidget(self.paintWidget)

        buttonsLayout = QHBoxLayout()

        self.clearButton = QPushButton("Clear")

        self.colorComboBox = QComboBox()
        self.colorComboBox.addItems(['black','red','yellow','blue'])

        buttonsLayout.addWidget(self.clearButton)
        buttonsLayout.addWidget(self.colorComboBox)

        mainLayout.addLayout(buttonsLayout)

        widget = QWidget()
        widget.setLayout(mainLayout)

        self.setCentralWidget(widget)

    def _linkButtons(self):
        self.clearButton.clicked.connect(self.paintWidget.clearImage)
        self.colorComboBox.activated.connect(self.paintWidget.setColor)
