#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
南昌大学
电磁场精确定位系统
2019.12.24
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout
from PyQt5.QtGui import QIcon
import pyqtgraph.opengl as gl


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()  # 界面绘制交给InitUi方法

    def initUI(self):

        xlabel = QLabel('x:')
        ylabel = QLabel('y:')
        zlabel = QLabel('z:')

        xlabel.setFixedSize(80, 15)
        ylabel.setFixedSize(80, 15)
        zlabel.setFixedSize(80, 15)

        blank = QWidget()

        view = gl.GLViewWidget()
        view.setBackgroundColor('w')

        ## create three grids, add each to the view
        xgrid = gl.GLGridItem()
        ygrid = gl.GLGridItem()
        zgrid = gl.GLGridItem()

        """
        xaxis = gl.GLAxisItem()
        yaxis = gl.GLAxisItem()
        zaxis = gl.GLAxisItem()
        """

        view.addItem(xgrid)
        view.addItem(ygrid)
        view.addItem(zgrid)

        ## rotate x and y grids to face the correct direction
        xgrid.rotate(270, 0, 1, 0)
        ygrid.rotate(90, 1, 0, 0)

        """
        ## scale each grid differently
        xgrid.scale(0.2, 0.1, 0.1)
        ygrid.scale(0.2, 0.1, 0.1)
        zgrid.scale(0.2, 0.1, 0.1)
        """
        """
        view.addItem(xaxis)
        view.addItem(yaxis)
        view.addItem(zaxis)
        """

        grid = QGridLayout()

        grid.addWidget(xlabel, 0, 0)
        grid.addWidget(ylabel, 1, 0)
        grid.addWidget(zlabel, 2, 0)
        grid.addWidget(blank,  3, 0)
        grid.addWidget(view, 0, 1, 0, 3)
        self.setLayout(grid)

        # 设置窗口的位置和大小
        self.setGeometry(200, 200, 400, 300)
        # 设置窗口的标题
        self.setWindowTitle('Icon')
        # 设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon('web.png'))

        # 显示窗口
        self.show()


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex  = Example()
    sys.exit(app.exec_())