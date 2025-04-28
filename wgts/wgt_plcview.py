from PySide6.QtWidgets import QApplication, QTableView, QComboBox, QSpinBox, QCheckBox, QStyledItemDelegate, QLineEdit, QRadioButton, QPushButton, QMessageBox, QMenu
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex, QDate
import os,sys
_top = sys.modules['__main__']
from libs.device.plc_modbus import MODBUS_AREA, MODBUS_VARTYPE, BYTE_ENDIAN, WORD_ENDIAN, IO
from libs.device.plc_s7 import Pt

class PlcData(QAbstractTableModel):
    
    def __init__(self, pts, parent=None):
        super().__init__(parent)
        self.pts = pts  # List of Pt objects
        self.cmbName_io = ["i", "o"]
        self.cmbName_type = ["BOOL", "INT", "WORD", "REAL"]

    def rowCount(self, parent=QModelIndex()):
        return len(self.pts)

    def columnCount(self, parent=QModelIndex()):
        return 7  # Fixed number of columns for Pt attributes

    def update(self):
        self.beginResetModel()
        self.pts = list(_top.PLC.pts.values())  # Assuming _top.PLC.config['pts'] contains the updated data
        self.endResetModel()

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.DisplayRole or role == Qt.EditRole:
            row = index.row()
            column = index.column()
            # breakpoint()
            pt = self.pts[row]
            if column == 0:
                return pt.id
            elif column == 1:
                return pt.name
            elif column == 2:
                return pt.iotype
            elif column == 3:
                return pt.vartype
            elif column == 4:
                return pt.addr
            elif column == 5:
                return ", ".join(pt.monitor) if pt.monitor else ""
            elif column == 6:
                return pt.value
        return None

    # def setData(self, index, value, role=Qt.EditRole):
    #     if not index.isValid() or role != Qt.EditRole:
    #         return False
    #     row = index.row()
    #     column = index.column()
    #     pt = self.pts[row]
    #     if column == 6:  # Only allow editing the value column
    #         pt.value = value
    #         self.dataChanged.emit(index, index, [Qt.DisplayRole, Qt.EditRole])
    #         return True
    #     return False

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        if index.column() == 6:  # Only the value column is editable
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            headers = ["点ID", "点名称", "IO类型", "数据类型", "地址", "监控信号", "值"]
            return headers[section]
        return super().headerData(section, orientation, role)

class myCellDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        if index.column()==5:
            pt_io = index.model().getdata(index.row(), 1)
            pt_type = index.model().getdata(index.row(), 3)
            if pt_io=='OUT':
                if  pt_type=='Bool':
                    combo = QComboBox(parent)
                    combo.addItems(["True", "False"])
                    return combo
                else:
                    return super().createEditor(parent, option, index)

    def setEditorData(self, editor, index):
        value = index.model().data(index, Qt.EditRole)
        if isinstance(editor, QComboBox):
            print(f"### Editor text now is :: {value} ###")

    def setModelData(self, editor, model, index):
        print(f"### Editor text now is :: {editor.currentText()} ###")
        # pt_index = index.row()
        # pt = _top.PLC.config['pts'][pt_index]
        # print(f"### Out pt :: {pt['name']} ###")
        # if isinstance(editor, QComboBox):
        #     _top.PLC.write_pt(pt, editor.currentText()=='True')
        # elif isinstance(editor, QSpinBox):
        #     if pt['type']==MODBUS_VARTYPE.Int_16 or pt['type']==MODBUS_VARTYPE.Int_32:
        #         _top.PLC.write_pt(pt, int(editor.value()))
        #     elif pt['type']==MODBUS_VARTYPE.Real_32:
        #         _top.PLC.write_pt(pt, float(editor.value()))
        #     else:
        #         raise f"写入类型错误::{pt['type']}"

class PlcTable(QTableView):
    def __init__(self, plcmodel, parent=None):

        super().__init__(parent)
        self.model = plcmodel
        self.setModel(self.model)

        self.setItemDelegate(myCellDelegate())

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.open_menu)
        # self.model.dataChanged.connect(self.update_json)
        # self.clicked.connect(self.show_item_content)

    def open_menu(self, position):
        menu = QMenu(self)
        custom_action = menu.addAction("查看监控曲线")
        custom_action.triggered.connect(self.plot_pt)
        menu.exec_(self.viewport().mapToGlobal(position))

    def plot_pt(self):
        QMessageBox.information(self, "提示", "待实现")
