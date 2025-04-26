import sys
import json
from PySide6.QtWidgets import QApplication
import asyncio

from view import Window
from cmd import CmdMananger, Cmd


if __name__ == '__main__':

    cmd_manager = CmdMananger()
    cmd_manager.loadFlow("flow01.json")
    cmd_manager.loadCmds()

    # Start Application
    app = QApplication(sys.argv)
    mainwindow = Window()
    mainwindow.show()
    sys.exit(app.exec())