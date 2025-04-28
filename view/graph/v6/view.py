# -*- coding: utf-8 -*-
import os,sys,json
from view.graph.v5._view import Ui_Form
from PySide6.QtWidgets import (QApplication, QVBoxLayout, QLabel, QMainWindow, QSizePolicy, QWidget, QDialog, QMessageBox)
from PySide6.QtQuickWidgets import QQuickWidget
from PySide6.QtCore import Slot, QUrl, QObject, QAbstractListModel, Qt, QSize, QMimeData
from PySide6.QtQml import QJSValue
_top = sys.modules['__main__']

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

        self.qml_flow = QQuickWidget()
        self.qml_flow.setResizeMode(QQuickWidget.ResizeMode.SizeRootObjectToView)

        nodes_model, connections_model = _top.CmdManager.genQmlModel()

        user = "admin"
        self.qml_flow.rootContext().setContextProperty("editable", user=="admin")
        self.qml_flow.rootContext().setContextProperty("nodesData", nodes_model)
        self.qml_flow.rootContext().setContextProperty("connectionsData", connections_model)

        self.qml_flow.setSource(QUrl.fromLocalFile('view/graph/v5/Canvas.qml'))       
        self.qml_root = self.qml_flow.rootObject()

        self.layout_tags = QVBoxLayout(self.ui.wgt_flow)
        self.layout_tags.addWidget(self.qml_flow)

        self.qml_root.evtAny.connect(self.onAny)
        self.ui.pushButton.clicked.connect(self.onStart)
        _top.CmdManager.evtCmdChanged.connect(self.onChildStatusChanged)

    def updateGraph(self):
        # print("updateGraph")
        self.qml_root.updateGraph()

    @Slot()
    def onStart(self):
        # print("onStart")
        # self.qml_root.start()
        _top.CmdManager.runflow()

    @Slot(dict)
    def onAny(self, response):
        # breakpoint()
        response = response.toVariant()
        if response["code"] == -2:
            QMessageBox.critical(None, "错误", response["msg"])
        elif response["code"] == -1:
            QMessageBox.warning(None, "警告", response["msg"])
        else:
            # QMessageBox.information(None, "信息", f"{response['type']}\n{response['msg']}\n{response['data']}")
            print(f"{response['type']}\n{response['msg']}\n{response['data']}")

            if response["type"] == "move":
                _top.CmdManager.nodes[response["data"]["id"]]['x'] = response["data"]["x"]
                _top.CmdManager.nodes[response["data"]["id"]]['y'] = response["data"]["y"]
                _top.CmdManager.saveFlow()

            else:
                pass

    @Slot(str, int)
    def onChildStatusChanged(self, cmd_id, status):
        print(f"Node状态变化: {cmd_id}, {status}")
        self.qml_root.updateNodeStatus(cmd_id, status)