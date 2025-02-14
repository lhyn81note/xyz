import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine

app = QApplication(sys.argv)
engine = QQmlApplicationEngine()

# 加载登录窗口 QML 文件
engine.load("view.qml")

if not engine.rootObjects():
    sys.exit(-1)

sys.exit(app.exec())