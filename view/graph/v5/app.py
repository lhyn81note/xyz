import sys
import json
from PySide6.QtWidgets import QApplication
import asyncio

from view import Window
from cmd import CmdMananger, Cmd
from plc import Plc


if __name__ == '__main__':

    # Plc初始化
    plc = Plc(config_file="plc.json", addr="172.16.1.95:0:2", protocal="s7", interval=3000)
    plc.load_config()
    plc.connect()
    print(f"PLC is alive: {plc.alive}")

    # CmdMananger初始化
    cmd_manager = CmdMananger("flow01.json", plc)
    cmd_manager.loadFlow()
    cmd_manager.loadCmds()

    # Start Application
    app = QApplication(sys.argv)
    mainwindow = Window()
    mainwindow.show()
    sys.exit(app.exec())