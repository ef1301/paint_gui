import sys
from PyQt5.QtWidgets import QApplication
from PyPaintMainUi import PyPaintMainUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PyPaintMainUi()
    window.show()
    sys.exit(app.exec())
