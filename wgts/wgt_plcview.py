from PySide6.QtWidgets import QApplication, QTableView, QComboBox, QSpinBox, QCheckBox, QStyledItemDelegate, QLineEdit, QRadioButton, QPushButton, QMessageBox, QMenu
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex, QDate
import os,sys
_top = sys.modules['__main__']
from libs.device import MODBUS_AREA, MODBUS_VARTYPE, BYTE_ENDIAN, WORD_ENDIAN, IO

class PlcData(QAbstractTableModel):
    def __init__(self, rawdata, parent=None):
        super().__init__(parent)
        self._data = rawdata
        self.cmbName_io = set([pt[1] for pt in rawdata])
        self.cmbName_area = set([pt[2] for pt in rawdata])
        self.cmbName_type = set([pt[3] for pt in rawdata])

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return len(self._data[0]) 

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.DisplayRole or role == Qt.EditRole:
            row = index.row()
            column = index.column()
            return self._data[row][column]
        return None
    
    def setData(self, row, col, value, role=Qt.EditRole):
        index = self.createIndex(row,  col)
        if index.isValid() and role == Qt.EditRole:
            row = index.row()
            column = index.column()
            self._data[row][column] = value
            self.dataChanged.emit(index, index, [Qt.DisplayRole, Qt.EditRole])
            return True
        return False

    def getdata(self, row, col, role=Qt.DisplayRole):
        index = self.createIndex(row,  col)
        if index.isValid():
            return self._data[row][col]
    
    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled

        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            headers = ["点名称", "IO类型", "数据区", "数据类型", "地址", "值"]
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
        pt_index = index.row()
        pt = _top.PLC.config['pts'][pt_index]
        print(f"### Out pt :: {pt['name']} ###")
        if isinstance(editor, QComboBox):
            _top.PLC.write_pt(pt, editor.currentText()=='True')
        elif isinstance(editor, QSpinBox):
            if pt['type']==MODBUS_VARTYPE.Int_16 or pt['type']==MODBUS_VARTYPE.Int_32:
                _top.PLC.write_pt(pt, int(editor.value()))
            elif pt['type']==MODBUS_VARTYPE.Real_32:
                _top.PLC.write_pt(pt, float(editor.value()))
            else:
                raise f"写入类型错误::{pt['type']}"

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
