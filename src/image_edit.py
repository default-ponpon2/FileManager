import sys

from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtWidgets
from PIL import Image


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.compressButton = QtWidgets.QPushButton(self.centralwidget)
        self.compressButton.setGeometry(QtCore.QRect(10, 650, 101, 23))
        self.compressButton.setObjectName("compressButton")
        self.quality = QtWidgets.QLabel(self.centralwidget)
        self.quality.setGeometry(QtCore.QRect(10, 620, 71, 21))
        self.quality.setObjectName("quality")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 1261, 591))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pixlabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.pixlabel.setText("")
        self.pixlabel.setObjectName("pixlabel")
        self.verticalLayout.addWidget(self.pixlabel)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 625, 251, 20))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(101, 620, 20, 21))
        self.label_2.setObjectName("label_2")
        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(140, 650, 251, 21))
        self.error.setText("")
        self.error.setObjectName("error")
        self.linEdit = QtWidgets.QSpinBox(self.centralwidget)
        self.linEdit.setGeometry(QtCore.QRect(61, 620, 41, 22))
        self.linEdit.setObjectName("linEdit")
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setGeometry(QtCore.QRect(10, 0, 75, 23))
        self.openButton.setObjectName("openButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.compressButton.setText(_translate("MainWindow", "Сжать"))
        self.quality.setText(_translate("MainWindow", "Качество"))
        self.label_2.setText(_translate("MainWindow", "%"))
        self.openButton.setText(_translate("MainWindow", "Открыть"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))


class ImageCompress(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.linEdit.setMinimum(1)
        self.linEdit.setMaximum(100)
        self.setWindowIcon(QIcon('icon.ico'))
        self.setWindowTitle('Сжатие Изображений')
        self.compressButton.clicked.connect(self.compress)
        self.openButton.clicked.connect(self.open)

        self.closeButton = QtWidgets.QPushButton('Закрыть', self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(100, 0, 75, 23))
        self.closeButton.setObjectName("closeButton")
        self.closeButton.clicked.connect(self.close_pixmap)

    def open(self):
        self.image_name = QFileDialog.getOpenFileName(self, 'Открыть изображение', '.',
                                                      'PNG Pictures (*.png);;JPG, JPEG Pictures (*.jpg, *.jpeg)')[0]
        self.pixmap = QPixmap(self.image_name)
        w = self.pixmap.width()
        h = self.pixmap.height()
        self.w1, self.h1, = w, h
        while w > 1259 and h > 609:
            print(f'Изображение слишком большое: {w} x {h}')
            self.pixmap = self.pixmap.scaled(w // 2, h // 2)
            w //= 2
            h //= 2

        self.pixlabel.setPixmap(self.pixmap)
        self.label.setText(f'Разрешение изображения: {self.w1} x {self.h1}')

    def close_pixmap(self):
        if self.pixlabel == self.pixmap:
            self.pixlabel.clear()
        else:
            QMessageBox().information(self, 'no_picture', 'У вас нет открытых изображений.')

    def compress(self):
        im = Image.open(self.image_name)
        comp_im = im.resize((int(self.w1 * (int(self.linEdit.value()) / 100)),
                            int(self.h1 * (int(self.linEdit.value()) / 100))))

        self.error.setText(f'Изображение сжато до {comp_im.width} x {comp_im.height}')
        fname = QFileDialog.getSaveFileName(self, 'Сохранить изображение', '.',
                                                      'PNG Pictures (*.png);;JPG, JPEG Pictures (*.jpg, *.jpeg)')[0]
        if not fname:
            return
        else:
            comp_im.save(fname)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageCompress()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())


