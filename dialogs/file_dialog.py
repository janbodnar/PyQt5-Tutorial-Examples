#!/usr/bin/python

"""
ZetCode PyQt5 tutorial

In this example, we select a file with a
QFileDialog and display its contents
in a QTextEdit.

Author: Jan Bodnar
Website: zetcode.com
"""

import sys
from pathlib import Path

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication)


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 550, 450)
        self.setWindowTitle('File dialog')
        self.show()

    def showDialog(self):

        home_dir = str(Path.home())

        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
