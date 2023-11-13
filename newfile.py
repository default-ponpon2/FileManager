import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 142)
        MainWindow.setMinimumSize(QtCore.QSize(410, 142))
        MainWindow.setMaximumSize(QtCore.QSize(410, 142))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem(".txt")
        self.comboBox.addItem(".py")
        self.comboBox.addItem(".ui")
        self.comboBox.addItem(".md")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.filename = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.filename.setObjectName("filename")
        self.gridLayout.addWidget(self.filename, 0, 0, 1, 1)
        self.createButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.createButton.setMaximumSize(QtCore.QSize(400, 25))
        self.createButton.setObjectName("createButton")
        self.gridLayout.addWidget(self.createButton, 1, 0, 1, 2)
        self.result = QtWidgets.QLabel(self.gridLayoutWidget)
        self.result.setText("")
        self.result.setObjectName("result")
        self.gridLayout.addWidget(self.result, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", ".txt"))
        self.comboBox.setItemText(1, _translate("MainWindow", ".py"))
        self.comboBox.setItemText(2, _translate("MainWindow", ".ui"))
        self.createButton.setText(_translate("MainWindow", "Создать"))


class NewFile(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.createButton.clicked.connect(self.create_file)
        self.setWindowTitle('Create New File')

    def create_file(self):
        newfile = open(f'{self.filename.text()}{self.comboBox.currentText()}', 'w+')
        if self.comboBox.currentText() == '.py':
            newfile.write('# New File Created.')
        else:
            newfile.write('New File Created.')
        self.result.setText('File Created')
        newfile.close()
        with open('temp.txt', 'w') as temp:
            pass
        with open('temp.txt', 'w') as temp:
            temp.write(self.filename.text() + self.comboBox.currentText())
        newex.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    newex = NewFile()
    newex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())


