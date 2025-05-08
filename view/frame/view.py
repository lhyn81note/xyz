
import os,sys
_top = sys.modules['__main__']
from view.frame._view import Ui_MainWindow
from PySide6.QtCore import (QDateTime, Qt)
from PySide6.QtGui import (QPainter, QAction,QIcon,QPixmap, QKeySequence, QColor, QPalette)
from PySide6.QtWidgets import (QTabBar,QWidget, QHeaderView, QHBoxLayout, QTableView,QSizePolicy,QMenuBar,QMenu, QToolBar,QToolButton)
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from functools import partial

class Window(QMainWindow):
    def __init__(self, menus=None, title=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        if menus:
            bar = QToolBar()
            for btn_name, acts in menus.items():
                btn = QToolButton()
                btn.setText(btn_name)
                if len(acts)>0:
                    btn.setPopupMode(QToolButton.MenuButtonPopup)
                    for act in acts:
                        action = QAction(QIcon(f"res/icon/{act['icon']}"), act['title'], self)
                        action.triggered.connect(partial(self.dispach, act, act['view_id']))
                        btn.addAction(action)
                bar.addWidget(btn)
            self.addToolBar(bar)
        
        self.hlayout = QHBoxLayout(self.ui.wgt_view)
        self.wgt_tabs = _top.TabWidget(self)
        self.hlayout.addWidget(self.wgt_tabs)
        _logo = QPixmap("res/image/xlt.png").scaled(self.ui.logo.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.logo.setPixmap(_logo)
        if title:
            self.setWindowTitle(title)
        
        self.wgt_tabs.create_tab(_top.Views["view_index"]['obj'](), _top.Views["view_index"]['title'], view_id="view_index", fixed=True)


        _top.Broker.addSubscriber(_top.CoreProvider.MsgSubscriber(self.update_plc, "View_index"), _top.MsgType.alarm)

    
    def dispach(self, act, view_id):
        print(view_id)
        if act['pop']:
            diag = _top.Views[view_id]['obj']()
            diag.setWindowTitle(_top.Views[view_id]['title'])
            diag.exec()
        else:
            if any(item[0]==view_id for item in self.wgt_tabs.fix_table):
                pass
            else:
                self.wgt_tabs.create_tab(_top.Views[view_id]['obj'](), _top.Views[view_id]['title'], view_id=view_id, fixed=act['fixed'])


    def update_plc(self,msg):
        
        if msg['source']=='PLC':

            if msg['subject']=='connect':
                if msg['content']==True:
                    self.ui.lb_status_plc.setStyleSheet('background-color: rgb(0, 255, 0);')
                else:
                    self.ui.lb_status_plc.setStyleSheet('background-color: rgb(255, 0, 0);')
            elif msg['subject']=='alarm':
                self.ui.lb_info.setStyleSheet('color: rgb(255, 0, 0);')
                self.ui.lb_info.setText(msg['content'])

            self.ui.lb_info.update()

        elif msg['source']=='Serial':
            pass
        else:
            pass
