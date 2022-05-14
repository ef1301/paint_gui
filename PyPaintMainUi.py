from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QComboBox, QSlider, QLabel, QColorDialog, QCheckBox, QRadioButton, QListWidget, QListWidgetItem
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
from PaintWidget import PaintWidget

class PyPaintMainUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyPaint")
        self.move(100, 100)

        self._addWidgets()
        self._linkActions()

    def _addWidgets(self):
        mainLayout = QVBoxLayout()

        self.paintWidget = PaintWidget()
        mainLayout.addWidget(self.paintWidget)

        mainLayout.addSpacing(1)

        sliderLayout = QHBoxLayout()

        sliderLayout.addWidget(QLabel("Circular Cursor:"))
        self.cursorCheckBox = QCheckBox()
        self.cursorCheckBox.setChecked(self.paintWidget.showCursor)
        sliderLayout.addWidget(self.cursorCheckBox)
        sliderLayout.addSpacing(20)

        self.sizeSlider = QSlider()
        self.sizeSlider.setOrientation(Qt.Horizontal)
        self.sizeSlider.setMinimum(1)
        self.sizeSlider.setMaximum(50)
        self.sizeSlider.setValue(self.paintWidget.curSize)

        sliderLayout.addWidget(QLabel("Brush Size:"))
        sliderLayout.addWidget(self.sizeSlider)

        mainLayout.addLayout(sliderLayout)

        mainLayout.addSpacing(1)

        radiosLayout = QHBoxLayout()
        radiosLayout.addWidget(QLabel("Brush Styles:"))
        self.solidBrush = QRadioButton("solid")
        self.solidBrush.setChecked(True)
        self.sprayBrush = QRadioButton("spray")
        self.eraseBrush = QRadioButton("erase")

        radiosLayout.addWidget(self.solidBrush)
        radiosLayout.addWidget(self.sprayBrush)
        radiosLayout.addWidget(self.eraseBrush)

        mainLayout.addLayout(radiosLayout)
        mainLayout.addSpacing(1)


        resizeLayout = QHBoxLayout()

        resizeLayout.addWidget(QLabel("Image/Window Resize Style:"))

        resizeLayout.addWidget(QLabel("Enlarge:"), 0, Qt.AlignRight)
        self.enlargeComboBox = QComboBox()
        self.enlargeComboBox.addItems(["extend", "scale"])
        resizeLayout.addWidget(self.enlargeComboBox)

        resizeLayout.addWidget(QLabel("Shrink:"), 0, Qt.AlignRight)
        self.shrinkComboBox = QComboBox()
        self.shrinkComboBox.addItems(["crop", "scale"])
        resizeLayout.addWidget(self.shrinkComboBox)

        mainLayout.addLayout(resizeLayout)

        mainLayout.addSpacing(1)

        buttonsLayout = QHBoxLayout()

        self.clearButton = QPushButton("Clear")

        self.colorButton = QPushButton("Set Color")

        self.saveButton = QPushButton("Save")

        buttonsLayout.addWidget(self.clearButton)
        buttonsLayout.addWidget(self.colorButton)
        buttonsLayout.addWidget(self.saveButton)

        mainLayout.addLayout(buttonsLayout)

        colorHistoryLayout = QVBoxLayout()
        colorHistoryLayout.addWidget(QLabel("Color History (Click to Reuse)"))
        self.colorHistory = QListWidget()
        self.colorHistory.setFixedWidth(170)
        initialItem = QListWidgetItem("black", self.colorHistory)
        initialItem.setBackground(Qt.black)
        colorHistoryLayout.addWidget(self.colorHistory)

        columnLayout = QHBoxLayout()
        columnLayout.addLayout(mainLayout)
        columnLayout.addSpacing(10)
        columnLayout.addLayout(colorHistoryLayout)

        widget = QWidget()
        widget.setLayout(columnLayout)

        self.setCentralWidget(widget)

    def _linkActions(self):
        self.clearButton.clicked.connect(self.paintWidget.clearImage)
        self.colorButton.clicked.connect(self.changeColor)
        self.saveButton.clicked.connect(self.paintWidget.saveImage)
        self.sizeSlider.valueChanged.connect(self.paintWidget.setBrushSize)
        self.solidBrush.toggled.connect(self.paintWidget.setSolidBrush)
        self.sprayBrush.toggled.connect(self.paintWidget.setSprayBrush)
        self.eraseBrush.toggled.connect(self.paintWidget.setEraseBrush)
        self.enlargeComboBox.activated[str].connect(self.paintWidget.setEnlargeStyle)
        self.shrinkComboBox.activated[str].connect(self.paintWidget.setShrinkStyle)
        self.cursorCheckBox.stateChanged.connect(self.paintWidget.setShowCursor)
        self.colorHistory.currentTextChanged.connect(self.reuseColor)

    def changeColor(self):
        color = self.paintWidget.setColor()
        listItem = QListWidgetItem(color.name(), self.colorHistory)
        listItem.setBackground(color)
        self.colorHistory.clearSelection()

    def reuseColor(self, color):
        self.paintWidget.curColor = QColor(color)
        self.paintWidget.updateCustomCursor()
