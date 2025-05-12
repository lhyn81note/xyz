# -*- coding: utf-8 -*-
import os,sys,json
from view.graph.v6._view import Ui_Form
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
        
        # 设置本页面的CmdMananger代理
        self.CmdManagerAgent = None

        # 设置下拉菜单
        # breakpoint()
        # flownames = list(map(lambda cmdkey: _top.CmdManager[cmdkey].meta['name'], list(_top.CmdManager.keys())))
        flownames = list(_top.CmdManager.keys())

        self.ui.cmb_flow.addItems(flownames) 
        self.ui.cmb_flow.currentIndexChanged.connect(self.onSelectFlow)

        # 初始化QML控件
        self.qml_flow = QQuickWidget()
        self.qml_flow.setResizeMode(QQuickWidget.ResizeMode.SizeRootObjectToView)
        self.layout_qml = QVBoxLayout(self.ui.wgt_flow)
        self.layout_qml.addWidget(self.qml_flow)
        self.qml_flow.setStyleSheet('margin:0px;\npadding:0px;')

        # 初始化qml根对象
        self.qml_root = None

        # 绑定事件
        self.ui.btn_start.clicked.connect(self.onStart)

        self.SetGraph("测试流程")

    def SetGraph(self, flowname):

        print(f"######### 创建Graph:{flowname} ############")
        for k,v  in _top.CmdManager.items():
            if k==flowname:
                self.CmdManagerAgent = _top.CmdManager.get(flowname)
                break

        if not self.CmdManagerAgent:
            print("流程信息调取出错!")
            return 

        nodes_model, connections_model = self.CmdManagerAgent.genQmlModel()
        self.qml_flow.rootContext().setContextProperty("editable", _top.User=="admin")
        self.qml_flow.rootContext().setContextProperty("nodesData", nodes_model)
        self.qml_flow.rootContext().setContextProperty("connectionsData", connections_model)

        self.qml_flow.setSource(QUrl.fromLocalFile('view/graph/v6/Canvas.qml'))       
        self.qml_root = self.qml_flow.rootObject()
        self.qml_root.evtAny.disconnect()
        self.qml_root.evtAny.connect(self.onAny)

        self.CmdManagerAgent.evtCmdChanged.connect(self.onChildStatusChanged)
        for _, cmdobj in self.CmdManagerAgent.cmdObjs.items():
            self.qml_root.updateNodeStatus(cmdobj.id, cmdobj.status)

        self.ui.lb_flow_desc.setText(self.CmdManagerAgent.meta['desc'])


    @Slot()
    def onSelectFlow(self):
        flowname = self.ui.cmb_flow.currentText()
        self.SetGraph(flowname)   

    @Slot()
    def onStart(self):
        self.CmdManagerAgent.runflow()

    @Slot()
    def onPauseContinue(self):
        self.CmdManagerAgent.pause()

    @Slot()
    def onStop(self):
        self.CmdManagerAgent.stop()

    @Slot(dict)
    def onAny(self, response):
        response = response.toVariant()
        if response["code"] == -2:
            QMessageBox.critical(None, "错误", response["msg"])
        elif response["code"] == -1:
            QMessageBox.warning(None, "警告", response["msg"])
        else:
            # QMessageBox.information(None, "信息", f"{response['type']}\n{response['msg']}\n{response['data']}")
            # print(f"{response['type']}\n{response['msg']}\n{response['data']}")

            if response["type"] == "move":
                self.CmdManagerAgent.nodes[response["data"]["id"]]['x'] = response["data"]["x"]
                self.CmdManagerAgent.nodes[response["data"]["id"]]['y'] = response["data"]["y"]
                self.CmdManagerAgent.saveFlow()
            else:
                pass

    @Slot(str, int)
    def onChildStatusChanged(self, cmd_id, status):
        print(f"Node状态变化: {cmd_id}, {status}")
        self.qml_root.updateNodeStatus(cmd_id, status)