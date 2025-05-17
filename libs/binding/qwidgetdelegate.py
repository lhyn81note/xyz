from PySide6.QtSql import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
# 自定义delegate类，用于自定义TableView的列编辑器
class QComboBoxWidgetDelegate (QStyledItemDelegate):
    def __init__(self, parent,value_data):
           super(QComboBoxWidgetDelegate, self).__init__(parent)
           self.value_data = value_data

    def createEditor(self, parent, option, index): 
        combo = QComboBox(parent)
        for idx,label in enumerate(self.value_data):
            combo.addItem(label)
        return combo
    
    def setEditorData(self, editor, index):  
        # 从model中读数据，更新Editor的显示值 
        # 读取当前节点的值
        value = index.model().data(index, Qt.EditRole)   
        if isinstance(value,int):
            value = str(value)
        if value:   # 如果不在combo中，添加进来。
            if not editor.findText(value):
                editor.addItem(value)
            editor.setCurrentText(value)   # 将选择值设为current
        else:
             editor.setCurrentIndex(0)

    def setModelData(self, editor, model, index):   
        # 从editor值更新model数据
        model.setData(index, editor.currentText(),  Qt.EditRole)
        
    def commitAndCloseEditor(self):
        """Commits the data and closes the editor. :) """
        editor = self.sender()
        # The commitData signal must be emitted when we've finished editing
        self.commitData.emit(editor)
        #delegate完成编辑后，应发送closeEditor ()信号通知其它组件。
        self.closeEditor.emit(editor)

class QCheckBoxWidgeDelegate (QStyledItemDelegate):
    def __init__(self, parent):
           super(QCheckBoxWidgeDelegate, self).__init__(parent)

    def createEditor(self, parent, option, index): 
        chkbox = QCheckBox(parent)
        return chkbox
    
    def setEditorData(self, editor, index):  
        # 从model中读数据，更新Editor的显示值 
        # 读取当前节点的值
        value = index.model().data(index, Qt.EditRole)   
        type_value = type(value)
        if value==1:
            editor.setChecked(value)
        else:
            editor.setChecked(False)         

    def setModelData(self, editor, model, index):   
        # 从editor值更新model数据
        model.setData(index, editor.isChecked(),  Qt.EditRole)
        
    def commitAndCloseEditor(self):
        """Commits the data and closes the editor. :) """
        editor = self.sender()
        # The commitData signal must be emitted when we've finished editing
        self.commitData.emit(editor)
        #delegate完成编辑后，应发送closeEditor ()信号通知其它组件。
        self.closeEditor.emit(editor)
class QDateTimeEditWidgeDelegate (QStyledItemDelegate):
    def __init__(self, parent):
           super(QDateTimeEditWidgeDelegate, self).__init__(parent)

    def createEditor(self, parent, option, index): 
        dateEdit = QDateTimeEdit(QDate.currentDate(),parent)
        dateEdit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        return dateEdit
    
    def setEditorData(self, editor, index):  
        # 从model中读数据，更新Editor的显示值 
        # 读取当前节点的值
        value = index.model().data(index, Qt.EditRole)   
        if isinstance(value,str) and value is not None:
            datetime = QDateTime.fromString(value, "yyyy-MM-dd HH:mm:ss")
            editor.setDateTime(datetime)
        else:
            editor.setDateTime(QDateTime.currentDateTime())         

    def setModelData(self, editor, model, index):   
        # 从editor值更新model数据
        model.setData(index, editor.dateTime() , Qt.EditRole)
        
    def commitAndCloseEditor(self):
        """Commits the data and closes the editor. :) """
        editor = self.sender()
        # The commitData signal must be emitted when we've finished editing
        self.commitData.emit(editor)
        #delegate完成编辑后，应发送closeEditor ()信号通知其它组件。
        self.closeEditor.emit(editor)

class QDateEditWidgeDelegate (QStyledItemDelegate):
    def __init__(self, parent):
           super(QDateEditWidgeDelegate, self).__init__(parent)

    def createEditor(self, parent, option, index): 
        dateEdit = QDateEdit(QDate.currentDate(),parent)
        dateEdit.setDisplayFormat("yyyy-MM-dd")
        return dateEdit
    
    def setEditorData(self, editor, index):  
        # 从model中读数据，更新Editor的显示值 
        # 读取当前节点的值
        value = index.model().data(index, Qt.EditRole)   
        if isinstance(value,str) and value is not None:
            datetime = QDate.fromString(value, "yyyy-MM-dd")
            editor.setDate(datetime)
        else:
            editor.setDate(QDate.currentDate())         

    def setModelData(self, editor, model, index):   
        # 从editor值更新model数据
        model.setData(index, editor.date() , Qt.EditRole)
        
    def commitAndCloseEditor(self):
        """Commits the data and closes the editor. :) """
        editor = self.sender()
        # The commitData signal must be emitted when we've finished editing
        self.commitData.emit(editor)
        #delegate完成编辑后，应发送closeEditor ()信号通知其它组件。
        self.closeEditor.emit(editor)


class QTimeEditWidgeDelegate (QStyledItemDelegate):
    def __init__(self, parent):
           super(QTimeEditWidgeDelegate, self).__init__(parent)

    def createEditor(self, parent, option, index): 
        dateEdit = QTimeEdit(QTime.currentTime(),parent)
        dateEdit.setDisplayFormat("HH:mm:ss")
        return dateEdit
    
    def setEditorData(self, editor, index):  
        # 从model中读数据，更新Editor的显示值 
        # 读取当前节点的值
        value = index.model().data(index, Qt.EditRole)   
        if isinstance(value,str) and value is not None:
            datetime = QTime.fromString(value, "HH:mm:ss")
            editor.setTime(datetime)
        else:
            editor.setTime(QTime.currentTime())         

    def setModelData(self, editor, model, index):   
        # 从editor值更新model数据
        model.setData(index, editor.time() , Qt.EditRole)
        
    def commitAndCloseEditor(self):
        """Commits the data and closes the editor. :) """
        editor = self.sender()
        # The commitData signal must be emitted when we've finished editing
        self.commitData.emit(editor)
        #delegate完成编辑后，应发送closeEditor ()信号通知其它组件。
        self.closeEditor.emit(editor)