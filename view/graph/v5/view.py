# -*- coding: utf-8 -*-
from _view import Ui_Form
import os,sys,json
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

        nodes_model, connections_model = _top.cmd_manager.genQmlModel()
        # # Example JSON configuration
        # json_str = '''
        # {
        #     "head_node_id": "开始",
        #     "开始": ["002", "003"],
        #     "002": ["004", "005"],
        #     "003": ["006", "007"],
        #     "004": ["end"],
        #     "005": ["003"],
        #     "006": ["end"],
        #     "007": ["end"]
        # }
        # '''
        # # Parse JSON
        # head_node, tree = parse_json(json_str)
        # positions = compute_positions(head_node, tree)
        # nodes_model, connections_model = generate_models(head_node, tree, positions)

        user = "admin"
        self.qml_flow.rootContext().setContextProperty("nodesData", nodes_model)
        self.qml_flow.rootContext().setContextProperty("connectionsData", connections_model)
        self.qml_flow.rootContext().setContextProperty("editable", user=="admin")

        self.qml_flow.setSource(QUrl.fromLocalFile('Canvas.qml'))       
        self.qml_root = self.qml_flow.rootObject()

        self.layout_tags = QVBoxLayout(self.ui.wgt_flow)
        self.layout_tags.addWidget(self.qml_flow)

        self.qml_root.evtAny.connect(self.onInfomation)

    @Slot(dict)
    def onInfomation(self, response):
        # breakpoint()
        response = response.toVariant()
        if response["code"] == -2:
            QMessageBox.critical(None, "错误", response["msg"])
        elif response["code"] == -1:
            QMessageBox.warning(None, "警告", response["msg"])
        else:
            QMessageBox.information(None, "信息", f"{response['type']}\n{response['msg']}\n{response['data']}")