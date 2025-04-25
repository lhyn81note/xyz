import sys
import json
from PySide6.QtWidgets import QApplication

from view import Window

if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainwindow = Window()
    mainwindow.show()
    sys.exit(app.exec())
