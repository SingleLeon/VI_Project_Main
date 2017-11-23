#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2017/11/2 9:18
# @Author  :  LuChao
# @Site     : 
# @File     : myDataTableView.py
# @Software  : PyCharm

from PyQt5 import QtCore, QtGui, QtWidgets


class myDataTableView(QtWidgets.QTableView):

    def __init__(self, parent=None):
        super(myDataTableView, self).__init__(parent)
        self.createContextMenu()

    def createContextMenu(self):
        '''

        :return:
        '''
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)
        self.contextMenu = QtWidgets.QMenu(self)
        self.actionA = self.contextMenu.addAction(QtGui.QIcon("images/0.png"), u'|  动作A')

        # 添加二级菜单
        self.second = self.contextMenu.addMenu(QtGui.QIcon("images/0.png"), u"|  二级菜单")
        self.actionD = self.second.addAction(QtGui.QIcon("images/0.png"), u'|  动作A')
        self.actionE = self.second.addAction(QtGui.QIcon("images/0.png"), u'|  动作B')
        self.actionF = self.second.addAction(QtGui.QIcon("images/0.png"), u'|  动作C')
        # 将动作与处理函数相关联
        # 这里为了简单，将所有action与同一个处理函数相关联，
        # 当然也可以将他们分别与不同函数关联，实现不同的功能

        return

    def showContextMenu(self, pos):
        '''''
        右键点击时调用的函数
        '''
        # 菜单显示前，将它移动到鼠标点击的位置
        self.contextMenu.exec_(QtGui.QCursor.pos())  # 在鼠标位置显示
        # self.contextMenu.show()

