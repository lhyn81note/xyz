import os, sys, logging
_top = sys.modules['__main__']
from PySide6.QtWidgets import (QComboBox, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox)

class CmdWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.filldata()

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(227, 224)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setText(u"选择指令")
        self.verticalLayout.addWidget(self.label)

        self.cmb_cmd = QComboBox(Form)
        self.verticalLayout.addWidget(self.cmb_cmd)

        self.label_2 = QLabel(Form)
        self.label_2.setText(u"参数1")
        self.verticalLayout.addWidget(self.label_2)
        self.cmb_param1 = QComboBox(Form)
        self.verticalLayout.addWidget(self.cmb_param1)
        self.tb_param1 = QLineEdit(Form)
        self.verticalLayout.addWidget(self.tb_param1)

        self.label_3 = QLabel(Form)
        self.label_3.setText(u"参数2")
        self.verticalLayout.addWidget(self.label_3)
        self.cmb_param2 = QComboBox(Form)
        self.verticalLayout.addWidget(self.cmb_param2)
        self.tb_param2 = QLineEdit(Form)
        self.verticalLayout.addWidget(self.tb_param2)

        self.btn_start = QPushButton(Form)
        self.btn_start.setText(u"开始")
        self.btn_start.setStyleSheet('background-color: rgb(0, 255, 0);')
        self.verticalLayout.addWidget(self.btn_start)

        self.btn_stop = QPushButton(Form)
        self.btn_stop.setText(u"停止")
        self.btn_stop.setStyleSheet('background-color: rgb(255, 0, 0);')
        self.verticalLayout.addWidget(self.btn_stop)

    def filldata(self):
        # Clear existing items
        self.cmb_cmd.clear()
        self.cmb_param1.clear()
        self.cmb_param2.clear()

        # Add each PLC point to the comboboxes
        if hasattr(_top, 'PLC') and hasattr(_top.PLC, 'pts'):
            for pt_id, pt in _top.PLC.pts.items():
                # Add item text as pt.name and store pt.id as user data
                self.cmb_cmd.addItem(pt.name, pt.id)
                self.cmb_param1.addItem(pt.name, pt.id)
                self.cmb_param2.addItem(pt.name, pt.id)

        # Connect signals to handle selection changes
        self.cmb_cmd.currentIndexChanged.connect(self.on_cmd_changed)
        self.cmb_param1.currentIndexChanged.connect(self.on_param1_changed)
        self.cmb_param2.currentIndexChanged.connect(self.on_param2_changed)

        # Connect button signals
        self.btn_start.clicked.connect(self.on_start_clicked)
        self.btn_stop.clicked.connect(self.on_stop_clicked)

    def on_cmd_changed(self, index):
        if index >= 0:
            pt_id = self.cmb_cmd.itemData(index)
            pt = _top.PLC.pts.get(pt_id)
            if pt:
                # Display additional information about the selected point
                self.tb_param1.setText(f"Type: {pt.vartype}, IO: {pt.iotype}")

    def on_param1_changed(self, index):
        if index >= 0:
            pt_id = self.cmb_param1.itemData(index)
            pt = _top.PLC.pts.get(pt_id)
            if pt:
                # Display current value of the selected point
                self.tb_param1.setText(str(pt.value))

    def on_param2_changed(self, index):
        if index >= 0:
            pt_id = self.cmb_param2.itemData(index)
            pt = _top.PLC.pts.get(pt_id)
            if pt:
                # Display current value of the selected point
                self.tb_param2.setText(str(pt.value))

    def on_start_clicked(self):
        # Get selected command and parameters
        cmd_index = self.cmb_cmd.currentIndex()
        param1_index = self.cmb_param1.currentIndex()
        param2_index = self.cmb_param2.currentIndex()

        if cmd_index >= 0:
            cmd_id = self.cmb_cmd.itemData(cmd_index)
            cmd_pt = _top.PLC.pts.get(cmd_id)

            if cmd_pt and cmd_pt.iotype == "o":  # Only output points can be written
                # Get parameter values
                param1_value = self.tb_param1.text()
                param2_value = self.tb_param2.text()

                try:
                    # Convert parameter values based on command type
                    if cmd_pt.vartype == "BOOL":
                        value = param1_value.lower() in ["true", "1", "yes", "y"]
                    elif cmd_pt.vartype == "INT" or cmd_pt.vartype == "WORD":
                        value = int(param1_value)
                    elif cmd_pt.vartype == "REAL":
                        value = float(param1_value)
                    else:
                        value = param1_value

                    # Write to PLC
                    result = _top.PLC.write(cmd_id, value)
                    if result:
                        msg = f"命令 {cmd_pt.name} 执行成功，值: {value}"
                        logging.info(msg)
                        QMessageBox.information(self, "执行成功", msg)
                    else:
                        msg = f"命令 {cmd_pt.name} 执行失败"
                        logging.error(msg)
                        QMessageBox.critical(self, "执行失败", msg)
                except Exception as e:
                    msg = f"执行命令时出错: {e}"
                    logging.error(msg)
                    QMessageBox.critical(self, "错误", msg)
            else:
                msg = "所选命令不是输出点或不存在"
                logging.warning(msg)
                QMessageBox.warning(self, "警告", msg)

    def on_stop_clicked(self):
        # Get selected command
        cmd_index = self.cmb_cmd.currentIndex()

        if cmd_index >= 0:
            cmd_id = self.cmb_cmd.itemData(cmd_index)
            cmd_pt = _top.PLC.pts.get(cmd_id)

            if cmd_pt and cmd_pt.iotype == "o":  # Only output points can be written
                try:
                    # Write FALSE or 0 to stop the command
                    if cmd_pt.vartype == "BOOL":
                        value = False
                    else:
                        value = 0

                    # Write to PLC
                    result = _top.PLC.write(cmd_id, value)
                    if result:
                        msg = f"命令 {cmd_pt.name} 已停止"
                        logging.info(msg)
                        QMessageBox.information(self, "停止成功", msg)
                    else:
                        msg = f"停止命令 {cmd_pt.name} 失败"
                        logging.error(msg)
                        QMessageBox.critical(self, "停止失败", msg)
                except Exception as e:
                    msg = f"停止命令时出错: {e}"
                    logging.error(msg)
                    QMessageBox.critical(self, "错误", msg)
            else:
                msg = "所选命令不是输出点或不存在"
                logging.warning(msg)
                QMessageBox.warning(self, "警告", msg)
