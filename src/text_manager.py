import os
import sys
import datetime
import pyperclip

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QProcess
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QFileDialog, QTextEdit, QMessageBox
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu
from pynput.keyboard import Key, Controller

from active_lang import *
from newfile import NewFile

keyb = Controller()

text = ''


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(640, 480))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.tab.setObjectName("tab")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 791, 531))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_2.sizePolicy().hasHeightForWidth())
        self.tab_2.setSizePolicy(sizePolicy)
        self.tab_2.setMinimumSize(QtCore.QSize(640, 480))
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow",
                                                                               "New_file.txt"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow",
                                                                                 "New_file2.txt"))


class FileManager(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        menu_bar = self.menuBar()
        self.tabWidget.removeTab(1)
        self.tabWidget.removeTab(0)
        self.setWindowTitle(TITLE)
        self.setWindowIcon(QIcon('icon.ico'))
        self.encode = 'utf-8'
        self.newfile_created = False
        self.name = ''
        self.docs = 'doc.txt'
        self.docc = False
        self.file_list = []
        self.filename = ''
        self.ch_en = False
        self.app = True
        self.newfile = NewFile()
        self.timer = QtCore.QTime()
        self.readme = False

        # self.centralwidget.setStyleSheet("background-color: #3c3f41;") смена темы

        self.console = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.console.sizePolicy().hasHeightForWidth())
        self.console.setSizePolicy(sizePolicy)
        self.console.setObjectName("console")
        self.horizontalLayout_2.addWidget(self.console)

        self.console.hide()

        with open('temp.txt', 'w+') as file:
            pass

        # file menu buttons
        file_menu = menu_bar.addMenu(FILE_MENU)

        newfile = QAction(NEW_FILE, self)
        newfile.triggered.connect(self.new)
        newfile.setShortcut('Ctrl+N')
        file_menu.addAction(newfile)

        openfile = QAction(OPEN_FILE, self)
        openfile.triggered.connect(self.open)
        openfile.setShortcut('Ctrl+O')
        file_menu.addAction(openfile)

        savefile = QAction(SAVE_FILE, self)
        savefile.triggered.connect(self.saveas)
        savefile.setShortcut('Ctrl+S')
        file_menu.addAction(savefile)

        savefileas = QAction(SAVE_FILE_AS, self)
        savefileas.triggered.connect(self.save)
        file_menu.addAction(savefileas)

        run_menu = QMenu("Запуск", self)
        file_menu.addMenu(run_menu)

        runfile = QAction(RUNFILE, menu_bar)
        runfile.triggered.connect(self.run)
        runfile.setShortcut('Shift+F10')
        run_menu.addAction(runfile)

        runas = QAction(RUNAS, menu_bar)
        runas.triggered.connect(self.runas)
        run_menu.addAction(runas)

        close_con = QAction(CLOSECON, menu_bar)
        close_con.triggered.connect(self.close_con)
        run_menu.addAction(close_con)

        # edit menu buttons
        edit_menu = menu_bar.addMenu(EDIT_MENU)

        undo = QAction(UNDO, self)
        undo.triggered.connect(self.undo)
        edit_menu.addAction(undo)

        redo = QAction(REDO, self)
        redo.triggered.connect(self.redo)
        edit_menu.addAction(redo)

        del_all = QAction(DEL_ALL, self)
        del_all.triggered.connect(self.del_all)
        edit_menu.addAction(del_all)

        time = QAction(TIME, self)
        time.triggered.connect(self.whatstime)
        edit_menu.addAction(time)
        
        close_act_tab = QAction(CLOSE_ACT, self)
        close_act_tab.triggered.connect(self.close_act)
        edit_menu.addAction(close_act_tab)

        close_all = QAction(CLOSE_ALL, self)
        close_all.triggered.connect(self.close_all)
        edit_menu.addAction(close_all)

        encoding = QMenu(ENCODING, self)
        edit_menu.addMenu(encoding)

        utf = QAction(UTF8, menu_bar)
        utf.triggered.connect(self.set_utf)
        encoding.addAction(utf)

        cp = QAction(CP, menu_bar)
        cp.triggered.connect(self.set_cp1252)
        encoding.addAction(cp)

        ascii = QAction(ASCII, menu_bar)
        ascii.triggered.connect(self.set_ascii)
        encoding.addAction(ascii)

        cp437 = QAction(CP437, menu_bar)
        cp437.triggered.connect(self.set_cp437)
        encoding.addAction(cp437)

        # help menu buttons
        help_menu = menu_bar.addMenu(HELP_MENU)

        about = QAction(ABOUT, self)
        about.triggered.connect(self.about)
        help_menu.addAction(about)

        doc = QAction(DOC, self)
        doc.triggered.connect(self.doc)
        help_menu.addAction(doc)

    def open(self):
        if self.newfile_created:
            fname = self.name
            self.app = True
            self.newfile_created = False
        elif self.docc:
            fname = self.docs
            self.docc = False
            self.app = True
        elif self.ch_en:
            fname = self.filename
            self.ch_en = False
            self.app = False
        elif self.readme:
            self.readme = False
            fname = 'README.md'
        else:
            fname = QFileDialog.getOpenFileName(self, OPEN_FILE[1:], '.',
                                                "Text Files (*.txt);;Python Files (*.py);;"
                                                "UI Files (*.ui);;Markdown Files (*.md);;All Files (*)")[0]

        if not fname:
            return
        with open(fname, encoding=self.encode, errors='replace') as f:
            if self.encode in ['ascii', 'cp1252', 'cp437']:
                txt = str(f.read().encode(self.encode, errors='replace'))
            else:
                txt = f.read()
            idx = self.tabWidget.addTab(QTextEdit(), str(fname.split('/')[-1]) + '|' + self.encode)
            self.tabWidget.widget(idx).setPlainText(txt)
            self.tabWidget.setCurrentIndex(idx)
            self.file_list.append(fname)
        self.app = False

    def save(self):
        if self.file_list:
            fname = QFileDialog.getSaveFileName(self, SAVE_FILE[1:], '.',
                                                "All Files (*);;Text Files (*.txt);;Python Files (*.py);;"
                                                "UI Files (*.ui);;Markdown Files (*.md)")[0]
            if not fname:
                return
            txt = self.tabWidget.currentWidget().toPlainText()
            with open(fname, 'w') as f:
                f.write(txt)
        else:
            pass

    def saveas(self):
        idx = self.tabWidget.currentIndex()
        print(self.file_list[idx].split('/')[-1], 'saved!')
        with open(self.file_list[idx], 'w') as clear:
            pass
        with open(self.file_list[idx], 'w') as file:
            file.write(self.tabWidget.currentWidget().toPlainText())

    def new(self):
        os.system('python newfile.py')
        with open('temp.txt', 'r') as file:
            self.name = file.read()
            self.newfile_created = True
        self.open()

    def handle_stderr(self):
        data = self.process.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.console.append(stderr)

    def handle_stdout(self):
        data = self.process.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.console.append(stdout)

    def run(self):
        if self.file_list:
            with open('temp.py', 'w+') as clear:
                pass
            with open('temp.py', 'w') as file:
                file.write(self.tabWidget.currentWidget().toPlainText())

            fname = 'temp.py'
            self.console.show()
            self.console.clear()

            self.console.append(f"[Running your code]\n")
            self.process = QProcess()
            self.process.readyReadStandardOutput.connect(self.handle_stdout)
            self.process.readyReadStandardError.connect(self.handle_stderr)
            self.process.started.connect(self.timer.start)
            self.process.finished.connect(self.finished_code)
            try:
                self.process.start("python", [f"{fname}"])
            except Exception as e:
                warn = QMessageBox()
                warn.setWindowTitle("Error")
                warn.setText(e)
                ex = warn.exec_()
        else:
            QMessageBox().information(self, 'no_files', 'У вас нет открытых файлов.')

    def runas(self):
        fname = QFileDialog.getOpenFileName(self, RUNAS, '.', "Python Files (*.py)")[0]
        self.console.show()
        self.console.clear()

        self.console.append(f"[Running file '{fname}']\n")
        self.process = QProcess()
        self.process.readyReadStandardOutput.connect(self.handle_stdout)
        self.process.readyReadStandardError.connect(self.handle_stderr)
        self.process.started.connect(self.timer.start)
        self.process.finished.connect(self.finished_code)
        try:
            self.process.start(f"python {fname}")
        except Exception as e:
            warn = QMessageBox()
            warn.setWindowTitle("Error")
            warn.setText(e)
            ex = warn.exec_()

    def stop_code(self):
        try:
            self.process.kill()
        except Exception as e:
            warn = QMessageBox()
            warn.setWindowTitle("Error")
            warn.setText(f"{e}")
            ex = warn.exec_()

    def finished_code(self):
        process_time = self.timer.elapsed()
        self.console.append(f"[Finished in {process_time / 1000}s]")
        self.process = None

    def close_con(self):
        self.console.hide()

    def undo(self):
        with keyb.pressed(Key.ctrl):
            keyb.press('z')
            keyb.release('z')

    def redo(self):
        with keyb.pressed(Key.ctrl):
            with keyb.pressed(Key.shift):
                keyb.press('z')
                keyb.release('z')

    def close_act(self):
        if self.file_list:
            idx = self.tabWidget.currentIndex()
            wgt = self.tabWidget.widget(idx)
            self.tabWidget.removeTab(idx)
            del wgt
        else:
            QMessageBox().information(self, 'no_files', 'У вас нет открытых файлов.')

    def close_all(self):
        if self.file_list:
            for i in range(self.tabWidget.count()):
                self.tabWidget.removeTab(0)
            self.file_list.clear()
        else:
            QMessageBox().information(self, 'no_files', 'У вас нет открытых файлов.')
    
    def del_all(self):
        self.tabWidget.widget(self.tabWidget.currentIndex()).setPlainText('')

    def whatstime(self):
        pyperclip.copy(datetime.datetime.now().today().strftime('%H:%M %d-%m-%Y'))
        with keyb.pressed(Key.ctrl):
            keyb.press('v')
            keyb.release('v')

    def change_encoding(self):
        if self.file_list:
            qm = QMessageBox()
            ret = qm.question(self, '', "Хотите поменять кодировку на всех активных файлах?", qm.Yes | qm.No)
            if ret == qm.Yes:
                for file in self.file_list:
                    self.filename = file
                    self.ch_en = True
                    self.open()
                    self.file_list.remove(file)
            else:
                pass

    def set_cp437(self):
        self.encode = 'utf-8'
        self.change_encoding()

    def set_utf(self):
        self.encode = 'utf-8'
        self.change_encoding()

    def set_cp1252(self):
        self.encode = 'cp1252'
        self.change_encoding()

    def set_ascii(self):
        self.encode = 'ascii'
        self.change_encoding()

    def about(self):
        self.readme = True
        self.open()

    def doc(self):
        self.docc = True
        self.open()

    def closeEvent(self, a0: QtGui.QCloseEvent):
        if self.file_list:
            qm = QMessageBox()
            ret = qm.question(self, '', "Вы точно хотите закрыть программу?\n"
                                        "Возможно у вас остались не сохраненные файлы.", qm.Yes | qm.No)
            if ret == qm.Yes:
                try:
                    os.remove('temp.py')
                except FileNotFoundError:
                    pass
                try:
                    os.remove('temp.txt')
                except FileNotFoundError:
                    pass
                a0.accept()
            else:
                a0.ignore()
        else:
            try:
                os.remove('temp.py')
            except FileNotFoundError:
                pass
            try:
                os.remove('temp.txt')
            except FileNotFoundError:
                pass
            a0.accept()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileManager()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
