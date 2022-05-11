from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QComboBox, QSlider, QLabel
from PyQt5.QtCore import Qt
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

        sliderLayout = QHBoxLayout()

        self.sizeSlider = QSlider()
        self.sizeSlider.setOrientation(Qt.Horizontal)
        self.sizeSlider.setMinimum(1)
        self.sizeSlider.setMaximum(50)
        self.sizeSlider.setValue(5)

        sliderLayout.addWidget(QLabel("Brush Size:"))
        sliderLayout.addWidget(self.sizeSlider)

        mainLayout.addLayout(sliderLayout)

        buttonsLayout = QHBoxLayout()

        self.clearButton = QPushButton("Clear")

        self.colorComboBox = QComboBox()
        self.colorComboBox.addItems(['black','red','yellow','blue'])

        self.saveButton = QPushButton("Save")

        buttonsLayout.addWidget(self.clearButton)
        buttonsLayout.addWidget(self.colorComboBox)
        buttonsLayout.addWidget(self.saveButton)

        mainLayout.addLayout(buttonsLayout)

        widget = QWidget()
        widget.setLayout(mainLayout)

        self.setCentralWidget(widget)

    def _linkButtons(self):
        self.clearButton.clicked.connect(self.paintWidget.clearImage)
        self.colorComboBox.activated.connect(self.paintWidget.setColor)
        self.saveButton.clicked.connect(self.paintWidget.saveImage)
        self.sizeSlider.valueChanged.connect(self.paintWidget.setBrushSize)
