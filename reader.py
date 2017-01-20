# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import time
import configparser


class Ui_MainWindow(QtWidgets.QMainWindow):
    class scrlArea(QtWidgets.QScrollArea):
        itemDropped = QtCore.pyqtSignal()
        def __init__(self, parent):
            super().__init__(parent)
            self.setAcceptDrops(True)
        def dragEnterEvent(self, event):
            if event.mimeData().hasUrls():
                event.acceptProposedAction()
            else:
                super().dragEnterEvent(event)

        def dragMoveEvent(self, event):
            super().dragMoveEvent(event)

        def dropEvent(self, event):
            if event.mimeData().hasUrls():
                for url in event.mimeData().urls():
                    self.localadres = str(url.toLocalFile())
                    self.itemDropped.emit()
                event.acceptProposedAction()
            else:
                super().dropEvent(event)

    def __init__(self):
        super().__init__()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.verticalLayout = QtWidgets.QHBoxLayout()
        self.verticalLayout.setDirection(QtWidgets.QBoxLayout.RightToLeft)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.scrollArea = self.scrlArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.itemDropped.connect(self.dropOpen)

        self.scrollAreaContents = QtWidgets.QWidget()
        self.scrollAreaContents.setEnabled(True)
        self.scrollAreaContents.setGeometry(QtCore.QRect(0, 0, 794, 553))
        self.scrollAreaContents.setObjectName("scrollAreaContents")


        self.front_layout = QtWidgets.QVBoxLayout(self.scrollAreaContents)
        self.front_layout.setContentsMargins(0, 0, 0, 0)
        self.front_layout.setObjectName("front_layout")
        readercr = QtGui.QColor(config['settings']['readercolor'])
        self.scrollArea.setStyleSheet('QWidget { background-color: %s; }' % readercr.name())

        self.scrollArea.setWidget(self.scrollAreaContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuReader = QtWidgets.QMenu(self.menubar)
        self.menuReader.setObjectName("menuReader")
        self.setMenuBar(self.menubar)
        self.color = QtGui.QColor(130, 130, 130)

        self.adres = 0
        self.girdi1 = -1
        self.girdi2 = -1
        self.girdi3 = -1

        # settings
        self.s_widget = QtWidgets.QWidget()
        self.b_widget = QtWidgets.QWidget()

        self.s_layout = QtWidgets.QGridLayout()
        self.b_layout = QtWidgets.QGridLayout()
        self.s_layout.setSpacing(5)

        # preparing
        self.input1 = QtWidgets.QLineEdit()
        self.input2 = QtWidgets.QLineEdit()
        self.input3 = QtWidgets.QLineEdit()

        self.text1 = QtWidgets.QLabel()
        self.text2 = QtWidgets.QLabel()
        self.text3 = QtWidgets.QLabel()

        self.color_button1 = QtWidgets.QPushButton()
        self.color_button1.clicked.connect(self.reader_color)
        self.color_button2 = QtWidgets.QPushButton()
        self.color_button2.clicked.connect(self.resetdefault)

        self.input1.setStyleSheet("QWidget { background-color: rgb(255, 255, 255); }")
        self.input2.setStyleSheet("QWidget { background-color: rgb(255, 255, 255); }")
        self.input3.setStyleSheet("QWidget { background-color: rgb(255, 255, 255); }")

        self.text1.setStyleSheet("QLabel { color: rgb(255, 255, 255); }")
        self.text2.setStyleSheet("QLabel { color: rgb(255, 255, 255); }")
        self.text3.setStyleSheet("QLabel { color: rgb(255, 255, 255); }")

        self.color_button1.setStyleSheet("QWidget { background-color: rgb(51, 56, 66); }")
        self.color_button2.setStyleSheet("QWidget { background-color: rgb(51, 56, 66); }")
        self.color_button1.setStyleSheet("QWidget { color: rgb(255, 255, 255); }")
        self.color_button2.setStyleSheet("QWidget { color: rgb(255, 255, 255); }")

        self.s_button = QtWidgets.QPushButton()
        self.s_button.setStyleSheet("QWidget { background-color: rgb(51, 56, 66); }")
        self.s_button.setStyleSheet("QWidget { color: rgb(255, 255, 255); }")
        self.s_button.setMaximumWidth(70)
        self.s_button.clicked.connect(self.s_apply)

        self.x_button = QtWidgets.QPushButton()
        self.x_button.setStyleSheet("QWidget { background-color: rgb(51, 56, 66); }")
        self.x_button.setStyleSheet("QWidget { color: rgb(255, 255, 255); }")
        self.x_button.setMaximumWidth(70)
        self.x_button.clicked.connect(self.settings_sh)

        self.text1.setText('Scale to H')
        self.text2.setText('Scale to W')
        self.text3.setText('Colors')
        self.color_button1.setText('Reader')
        self.color_button2.setText('Reset')
        self.s_button.setText('Apply')
        self.x_button.setText('Close')
        self.resizeEvent = self.user_resize

        # placement
        self.s_layout.addWidget(self.text1, 1, 0, QtCore.Qt.AlignTop)
        self.s_layout.addWidget(self.text2, 2, 0, QtCore.Qt.AlignTop)
        self.s_layout.addWidget(self.text3, 3, 0, QtCore.Qt.AlignTop)

        self.s_layout.addWidget(self.color_button1, 3, 1)
        self.s_layout.addWidget(self.color_button2, 3, 2)

        self.s_layout.addWidget(self.input1, 1, 1, 1, 2, QtCore.Qt.AlignTop)
        self.s_layout.addWidget(self.input2, 2, 1, 1, 2, QtCore.Qt.AlignTop)
        self.s_layout.setRowStretch(4, 1)

        self.s_layout.addWidget(self.b_widget)
        self.b_layout.setRowStretch(1, 1)
        self.b_layout.addWidget(self.x_button, 2, 1)
        self.b_layout.addWidget(self.s_button, 2, 2)

        # input send
        self.input1.textChanged[str].connect(self.input1_trigger)
        self.input2.textChanged[str].connect(self.input2_trigger)
        self.input3.textChanged[str].connect(self.input3_trigger)

        self.b_widget.setLayout(self.b_layout)
        self.s_widget.setLayout(self.s_layout)
        self.s_widget.setMinimumWidth(200)
        settingscr = QtGui.QColor(config['settings']['settingscolor'])
        self.s_widget.setStyleSheet('QWidget { background-color: %s; }' % settingscr.name())
        self.verticalLayout.addWidget(self.s_widget)
        self.s_widget.hide()

        # Klasör seçme
        self.actionOpen = QtWidgets.QAction(self)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.setShortcut('O')
        self.actionOpen.triggered.connect(self.file_open)

        # Çıkış
        self.actionExit = QtWidgets.QAction(self)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setShortcut('Q')
        self.actionExit.triggered.connect(self.u_exit)

        # Ayarlar
        self.actionSettings = QtWidgets.QAction(self)
        self.actionSettings.setObjectName("actionSetings")
        self.actionSettings.setShortcut('S')
        self.actionSettings.triggered.connect(self.settings_sh)

        # Menüye ekleme
        self.menuReader.addAction(self.actionSettings)
        self.menuReader.addAction(self.actionOpen)
        self.menuReader.addAction(self.actionExit)
        self.menubar.addAction(self.menuReader.menuAction())

        self.retranslateUi()

        # Thread - slots
        self.luder = LoaderThread()
        self.luder.adres = ''
        self.luder.pics.connect(self.add_widget)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Reader"))
        self.menuReader.setTitle(_translate("MainWindow", "Reader"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def user_resize(self, event):
        button_size1 = self.s_widget.width()
        button_size2 = button_size1 / 2
        self.s_button.setMaximumWidth(button_size2)

        sframe_size1 = self.width()
        sframe_size2 = 2 * (sframe_size1 / 5)
        if sframe_size2 > 350:
            self.s_widget.setMaximumWidth(350)
        else:
            self.s_widget.setMaximumWidth(sframe_size2)

    def u_exit(self):
        QtWidgets.qApp.exit()
    # color pickers
    def reader_color(self):
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid() is True:
            config['settings']['readercolor'] = color.name()
            print(color.name())
            self.scrollArea.setStyleSheet('QWidget { background-color: %s; }' % color.name())
            self.saveconfig()
        else:
            pass
    def settings_color(self):
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid() is True:
            config['settings']['settingscolor'] = color.name()
            self.s_widget.setStyleSheet('QWidget { background-color: %s; }' % color.name())
            self.saveconfig()
        else:
            pass

    # setting applies
    def s_apply(self):
        self.p_cleaner()
        self.loader()

    # reader cleanup
    def p_cleaner(self):
        while self.front_layout.count():
            child = self.front_layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                child.layout().deleteLater()

    # input save
    def input1_trigger(self, text):
        try:
            self.girdi1 = int(text)
            self.girdi2 = -1
            self.girdi3 = -1
        except ValueError:
            self.girdi1 = -1

    def input2_trigger(self, text):
        try:
            self.girdi2 = int(text)
            self.girdi1 = -1
            self.girdi3 = -1
        except ValueError:
            self.girdi2 = -1

    def input3_trigger(self, text):
        try:
            self.girdi3 = int(text)
            self.girdi2 = -1
            self.girdi1 = -1
        except ValueError:
            self.girdi3 = -1

    # setting show/hide
    def settings_sh(self):
        settings_status = self.s_widget.isHidden()
        if settings_status is True:
            self.s_widget.show()
        else:
            self.s_widget.hide()

    def resetdefault(self):
        config['settings'] = {'readercolor': '#282C34', 'settingscolor': '#31343F', 'scaleh': '-1', 'scalew': '-1'}
        readercr = QtGui.QColor(config['settings']['readercolor'])
        self.scrollArea.setStyleSheet('QWidget { background-color: %s; }' % readercr.name())
        self.saveconfig()

    # file select
    def file_open(self):
        adres = QtWidgets.QFileDialog.getExistingDirectory()
        if adres is '':
            pass
        else:
            self.p_cleaner()
            self.luder.adres = adres
            self.loader()

    def dropOpen(self):
        if os.path.isfile(self.scrollArea.localadres):
            self.luder.adres = os.path.dirname(self.scrollArea.localadres)
            print(self.luder.adres)
        else:
            self.luder.adres = self.scrollArea.localadres
            print(self.luder.adres)
        self.p_cleaner()
        self.loader()

    # loaders
    def loader(self):
        if self.luder.adres is '':
            pass
        else:
            self.luder.start()

    def add_widget(self, image):
        label = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap.fromImage(image)
        if self.girdi1 is not -1:
            scaled = pixmap.scaledToHeight(self.girdi1, QtCore.Qt.SmoothTransformation)
            label.setPixmap(scaled)
        elif self.girdi2 is not -1:
            scaled = pixmap.scaledToWidth(self.girdi2, QtCore.Qt.SmoothTransformation)
            label.setPixmap(scaled)
        else:
            label.setPixmap(pixmap)
        label.setScaledContents(False)
        label.setAlignment(QtCore.Qt.AlignHCenter)
        self.front_layout.addWidget(label)

    def saveconfig(self):
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

class LoaderThread(QtCore.QThread):
    pics = QtCore.pyqtSignal(object)

    def __init__(self):
        QtCore.QThread.__init__(self)

    def run(self):
        liste = os.listdir(self.adres)
        order = 0
        for i in liste:
            image = QtGui.QImage(self.adres + '/' + liste[order])
            self.pics.emit(image)
            order += 1

if __name__ == "__main__":
    import sys
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'readercolor': '#282C34', 'settingscolor': '#31343F', 'scaleh': '-1', 'scalew': '-1'}
    config.read('config.ini')
    try:
        print(config['settings']['readercolor'])
    except KeyError:
        config['settings'] = {'readercolor': '#282C34', 'settingscolor': '#31343F', 'scaleh': '-1', 'scalew': '-1'}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
