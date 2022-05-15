from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QComboBox, QSlider, QLabel, QCheckBox, QRadioButton
from PyQt5.QtCore import Qt
from PaintWidget import PaintWidget
from ColorHistory import ColorHistory

class Settings(QWidget):
    def __init__(self, paintWidget: PaintWidget, history: ColorHistory):
        super().__init__()
        self._paintWidget = paintWidget
        self._colorHistory = history
        self._addWidgets()
        self._linkActions()
        self.setFixedHeight(self.minimumSizeHint().height())

    def _addWidgets(self):
        layout = QVBoxLayout()

        sliderLayout = QHBoxLayout()

        self.sizeSlider = QSlider()
        self.sizeSlider.setOrientation(Qt.Horizontal)
        self.sizeSlider.setMinimum(1)
        self.sizeSlider.setMaximum(50)
        self.sizeSlider.setValue(self._paintWidget.curSize)

        sliderLayout.addWidget(QLabel("Brush Size:"))
        sliderLayout.addWidget(self.sizeSlider)

        self.cursorCheckBox = QCheckBox("Circular Cursor: ")
        self.cursorCheckBox.setLayoutDirection(Qt.RightToLeft)

        sliderLayout.addWidget(self.cursorCheckBox)

        layout.addLayout(sliderLayout)

        layout.addSpacing(1)

        radiosLayout = QHBoxLayout()
        radiosLayout.addWidget(QLabel("Brush Styles:"))
        self.solidBrush = QRadioButton("solid")
        self.solidBrush.setChecked(True)
        self.sprayBrush = QRadioButton("spray")
        self.eraseBrush = QRadioButton("erase")

        radiosLayout.addWidget(self.solidBrush)
        radiosLayout.addWidget(self.sprayBrush)
        radiosLayout.addWidget(self.eraseBrush)

        layout.addLayout(radiosLayout)
        layout.addSpacing(1)

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

        layout.addLayout(resizeLayout)

        layout.addSpacing(1)

        buttonsLayout = QHBoxLayout()

        self.clearButton = QPushButton("Clear")

        self.colorButton = QPushButton("Set Color")

        self.saveButton = QPushButton("Save")

        buttonsLayout.addWidget(self.clearButton)
        buttonsLayout.addWidget(self.colorButton)
        buttonsLayout.addWidget(self.saveButton)

        layout.addLayout(buttonsLayout)

        self.setLayout(layout)

    def _linkActions(self):
        self.clearButton.clicked.connect(self._paintWidget.clearImage)
        self.colorButton.clicked.connect(self.changeColor)
        self.saveButton.clicked.connect(self._paintWidget.saveImage)
        self.sizeSlider.valueChanged.connect(self._paintWidget.setBrushSize)
        self.solidBrush.toggled.connect(self.setStyle)
        self.sprayBrush.toggled.connect(self.setStyle)
        self.eraseBrush.toggled.connect(self.setStyle)
        self.cursorCheckBox.setChecked(self._paintWidget.showCursor)
        self.enlargeComboBox.activated[str].connect(self._paintWidget.setEnlargeStyle)
        self.shrinkComboBox.activated[str].connect(self._paintWidget.setShrinkStyle)
        self.cursorCheckBox.stateChanged.connect(self._paintWidget.setShowCursor)

    def changeColor(self):
        if self.eraseBrush.isChecked():
            self.solidBrush.setChecked(True)
            self._paintWidget.setStyle("solid")
        color = self._paintWidget.changeColor()
        self._colorHistory.addColor(color)

    def setStyle(self):
        radio = self.sender()
        if radio.isChecked():
            self._paintWidget.setStyle(radio.text())
