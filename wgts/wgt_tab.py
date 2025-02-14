from __future__ import annotations

from functools import partial
from PySide6.QtWebEngineCore import (QWebEngineFindTextResult, QWebEnginePage)
from PySide6.QtWidgets import QLabel, QMenu, QTabBar, QTabWidget
from PySide6.QtGui import QCursor, QIcon, QKeySequence, QPixmap
from PySide6.QtCore import QUrl, Qt, Signal, Slot

class TabWidget(QTabWidget):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.fix_table=[]
        tab_bar = self.tabBar()
        tab_bar.setTabsClosable(True)
        # tab_bar.setMovable(True)
        tab_bar.setSelectionBehaviorOnRemove(QTabBar.SelectPreviousTab)
        tab_bar.setContextMenuPolicy(Qt.CustomContextMenu)
        self.setDocumentMode(True)
        self.setElideMode(Qt.ElideRight)
        
        self.tabCloseRequested.connect(self.close_tab)
        tab_bar.customContextMenuRequested.connect(self.handle_context_menu_requested)
        tab_bar.tabCloseRequested.connect(self.close_tab)
        self.currentChanged.connect(self.handle_current_changed)

    def handle_current_changed(self, index):
        if index != -1:
            pass
        else:
            pass

    def handle_context_menu_requested(self, pos):
        menu = QMenu()
        index = self.tabBar().tabAt(pos)
        if index != -1:
            action = menu.addAction("关闭标签")
            action.setShortcut(QKeySequence.Close)
            action.triggered.connect(partial(self.close_tab, index))
            menu.addSeparator()
            action = menu.addAction("关闭其他标签")
            action.triggered.connect(partial(self.close_other_tabs, index))
        else:
            menu.addSeparator()
        menu.exec(QCursor.pos())

    def create_tab(self, widget, title, view_id, fixed):
        self.addTab(widget, title)
        idx = self.currentIndex()
        self.fix_table.append((view_id,fixed))


    def close_other_tabs(self, index):
        for i in range(index, self.count() - 1, -1):
            self.close_tab(i)
        for i in range(-1, index - 1, -1):
            self.close_tab(i)

    def close_tab(self, index):
        if not self.fix_table[index][1]: 
            self.removeTab(index)
            del self.fix_table[index]
