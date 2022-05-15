# PyPaint

![PyPaint GUI](./images/GUI.png)

## Description

A painting GUI with the following functionalities and widgets:
* **Label Widget (QLabel)**
* **Slider Widget (QSlider):** Change Brush Size
* **Checkbox Widget (QCheckBox):** Toggle Circular Drawing Cursor
* **Radio Widget (QRadioButton):** Change Brush Style (Solid, Spray, Erase)
* **ComboBox Widget (QComboBox):** Image/WIndow Resize Style
  * Enlarge (extend, scale)
  * Shrink (crop, scale)
* **Button (QPushButton):** Clear Canvas, Change Brush Color, Save Canvas as png
* **Color, MessageBox, File Widget (QColorDialog, QMessageBox, QFileDialog)**
* **List Widget (QListWidget, QListWidgetItem):** Color History

### Dependencies

* PyQt5
* random

### Executing program

* How to run the program
* Step-by-step bullets
```
python main.py
```
## Classes & Functions
* **PyPaintMainUi:** Encapsulates PaintWidget, Settings, and Color History
* **PaintWidget:** Encapsulates canvas and painting functionalities
  * updateCustomCursor(self)
  * mousePressEvent(self, event)
  * mouseMoveEvent(self, event)
  * mouseReleaseEvent(self, event)
  * setShowCursor(self, val)
  * setColor(self, color)
  * setBrushSize(self, size)
  * setSolidBrush(self)
  * setSprayBrush(self)
  * setEraseBrush(self)
  * setEnlargeStyle(self, style)
  * setShrinkStyle(self, style)
  * changeColor(self)
  * clearImage(self)
  * saveImage(self)
  * extend(self)
  * scale(self)
  * resizeEvent(self, event)
* **Settings:** Encapsulates brush size, cursor, brush styles, image/window resize, clear, colors, and save settings
  * _addWidgets(self)
  * _linkActions(self)
  * changeColor(self)
* **ColorHistory:** Encapsulates color history list and reuse color functionalities
  * _addWidgets(self)
  * _linkActions(self)
  * _reuseColor(self, color)
  * addColor(self, color)

## Authors

Contributors names
[@Adeebur Rahman](https://github.com/adeeburrahman)
[@Darren Liang](https://github.com/dliang2)
[@Emily Fang](https://github.com/ef1301)