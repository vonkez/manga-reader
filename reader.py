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
    class ScrlArea(QtWidgets.QScrollArea):
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

        self.scrollArea = self.ScrlArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.verticalScrollBar().valueChanged.connect(self.scroll_slot)
        self.scrollArea.itemDropped.connect(self.drop_open)

        self.scrollAreaContents = QtWidgets.QWidget()
        self.scrollAreaContents.setEnabled(True)
        self.scrollAreaContents.setGeometry(QtCore.QRect(0, 0, 794, 553))
        self.scrollAreaContents.setObjectName("scrollAreaContents")

        self.scrollAreaLayout = QtWidgets.QVBoxLayout(self.scrollAreaContents)
        self.scrollAreaLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollAreaLayout.setObjectName("scrollAreaLayout")
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
        scaleh = config['settings']['scaleh']
        scalew = config['settings']['scalew']
        self.line1_value = int(scaleh)
        self.line2_value = int(scalew)
        self.line3_value = -1

        # settings
        self.settings_widget1 = QtWidgets.QWidget()
        self.settings_widget2 = QtWidgets.QWidget()

        self.settings_layout1 = QtWidgets.QGridLayout()
        self.settings_layout2 = QtWidgets.QGridLayout()
        self.settings_layout1.setSpacing(5)

        # preparing
        self.line1 = QtWidgets.QLineEdit()
        self.line2 = QtWidgets.QLineEdit()
        self.line3 = QtWidgets.QLineEdit()
        self.resume_checkbox = QtWidgets.QCheckBox()

        self.text1 = QtWidgets.QLabel()
        self.text2 = QtWidgets.QLabel()
        self.text3 = QtWidgets.QLabel()
        self.text4 = QtWidgets.QLabel()

        self.color_button1 = QtWidgets.QPushButton()
        self.color_button1.clicked.connect(self.reader_color)
        self.reset_button = QtWidgets.QPushButton()
        self.reset_button.clicked.connect(self.reset_default)

        self.line1.setStyleSheet("QWidget { background-color: rgb(255, 255, 255); }")
        self.line2.setStyleSheet("QWidget { background-color: rgb(255, 255, 255); }")
        self.line3.setStyleSheet("QWidget { background-color: rgb(255, 255, 255); }")
        self.resume_checkbox.setStyleSheet("QAbstractButton { background-color: #7A8395;}")

        self.text1.setStyleSheet("QLabel { color: rgb(255, 255, 255); }")
        self.text2.setStyleSheet("QLabel { color: rgb(255, 255, 255); }")
        self.text3.setStyleSheet("QLabel { color: rgb(255, 255, 255); }")
        self.text4.setStyleSheet("QLabel { color: rgb(255, 255, 255); }")

        self.resume_checkbox.setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        self.color_button1.setStyleSheet("QWidget { background-color: rgb(51, 56, 66); }")
        self.reset_button.setStyleSheet("QWidget { background-color: rgb(51, 56, 66); }")
        self.color_button1.setStyleSheet("QWidget { color: rgb(255, 255, 255); }")
        self.reset_button.setStyleSheet("QWidget { color: rgb(255, 255, 255); }")

        self.apply_button = QtWidgets.QPushButton()
        self.apply_button.setStyleSheet("QWidget { background-color: rgb(51, 56, 66); }")
        self.apply_button.setStyleSheet("QWidget { color: rgb(255, 255, 255); }")
        self.apply_button.setMaximumWidth(70)
        self.apply_button.clicked.connect(self.apply)

        self.close_button = QtWidgets.QPushButton()
        self.close_button.setStyleSheet("QWidget { background-color: rgb(51, 56, 66); }")
        self.close_button.setStyleSheet("QWidget { color: rgb(255, 255, 255); }")
        self.close_button.setMaximumWidth(70)
        self.close_button.clicked.connect(self.settings_sh)

        self.text1.setText('Scale to H')
        self.text2.setText('Scale to W')
        self.text3.setText('Colors')
        self.text4.setText('Continue reading')

        self.color_button1.setText('Reader')
        self.reset_button.setText('Reset')
        self.apply_button.setText('Apply')
        self.close_button.setText('Close')
        self.resizeEvent = self.resize_e

        # placement
        self.settings_layout1.addWidget(self.text1, 1, 0, QtCore.Qt.AlignTop)
        self.settings_layout1.addWidget(self.text2, 2, 0, QtCore.Qt.AlignTop)
        self.settings_layout1.addWidget(self.text3, 3, 0, QtCore.Qt.AlignTop)
        self.settings_layout1.addWidget(self.text4, 4, 0, QtCore.Qt.AlignTop)
        self.settings_layout1.addWidget(self.resume_checkbox, 4, 1)

        self.settings_layout1.addWidget(self.color_button1, 3, 1)
        self.settings_layout1.addWidget(self.reset_button, 3, 2)

        self.settings_layout1.addWidget(self.line1, 1, 1, 1, 2, QtCore.Qt.AlignTop)
        self.settings_layout1.addWidget(self.line2, 2, 1, 1, 2, QtCore.Qt.AlignTop)
        self.settings_layout1.setRowStretch(5, 1)
        self.settings_layout1.addWidget(self.settings_widget2)

        self.settings_layout2.setRowStretch(1, 1)
        self.settings_layout2.addWidget(self.close_button, 2, 1)
        self.settings_layout2.addWidget(self.apply_button, 2, 2)

        # input send
        self.line1.textChanged[str].connect(self.input1_trigger)
        self.line2.textChanged[str].connect(self.input2_trigger)
        self.line3.textChanged[str].connect(self.input3_trigger)
        self.resume_checkbox.stateChanged.connect(self.checkbox_trigger)

        self.settings_widget2.setLayout(self.settings_layout2)
        self.settings_widget1.setLayout(self.settings_layout1)
        self.settings_widget1.setMinimumWidth(200)

        if config['settings']['resumereading'] == 'True':
            self.resume_checkbox.setChecked(True)

        settingscr = QtGui.QColor(config['settings']['settingscolor'])
        self.settings_widget1.setStyleSheet('QWidget { background-color: %s; }' % settingscr.name())
        self.verticalLayout.addWidget(self.settings_widget1)
        self.settings_widget1.hide()

        # select folder
        self.actionOpen = QtWidgets.QAction(self)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.setShortcut('O')
        self.actionOpen.triggered.connect(self.file_open)

        # exit
        self.actionExit = QtWidgets.QAction(self)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setShortcut('Q')
        self.actionExit.triggered.connect(self.u_exit)

        # settings
        self.actionSettings = QtWidgets.QAction(self)
        self.actionSettings.setObjectName("actionSetings")
        self.actionSettings.setShortcut('S')
        self.actionSettings.triggered.connect(self.settings_sh)

        # adding actions to menu
        self.menuReader.addAction(self.actionSettings)
        self.menuReader.addAction(self.actionOpen)
        self.menuReader.addAction(self.actionExit)
        self.menubar.addAction(self.menuReader.menuAction())

        self.retranslateUi()

        # Thread - slots
        self.luder = LoaderThread()
        self.luder.adres = ''
        self.luder.pics.connect(self.add_widget)
        self.luder.done.connect(self.resume_reading)

    def scroll_slot(self, value):
        config['%s' % self.luder.adres]['resumepoint'] = str(value)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Reader"))
        self.menuReader.setTitle(_translate("MainWindow", "Reader"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def resize_e(self, event):
        button_size1 = self.settings_widget1.width()
        button_size2 = button_size1 / 2
        self.apply_button.setMaximumWidth(button_size2)
        sframe_size1 = self.width()
        sframe_size2 = 2 * (sframe_size1 / 5)
        if sframe_size2 > 350:
            self.settings_widget1.setMaximumWidth(350)
        else:
            self.settings_widget1.setMaximumWidth(sframe_size2)

    def u_exit(self):
        self.saveconfig()
        QtWidgets.qApp.exit()

    def isVisibleWidget(self, widget):
        if not widget.visibleRegion().isEmpty():
            return True
        return False

    # color pickers
    def reader_color(self):
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            config['settings']['readercolor'] = color.name()
            print(color.name())
            self.scrollArea.setStyleSheet('QWidget { background-color: %s; }' % color.name())
            self.saveconfig()
        else:
            pass

    def settings_color(self):
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            config['settings']['settingscolor'] = color.name()
            self.settings_widget1.setStyleSheet('QWidget { background-color: %s; }' % color.name())
            self.saveconfig()
        else:
            pass

    # setting applies
    def apply(self):
        self.cleaner()
        self.loader()

    # reader cleaner
    def cleaner(self):
        while self.scrollAreaLayout.count():
            child = self.scrollAreaLayout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()

    # input
    def input1_trigger(self, text):
        try:
            self.line1_value = int(text)
            config['settings']['scaleh'] = str(self.line1_value)
            self.line2_value = -1
            config['settings']['scalew'] = str(self.line2_value)
            self.line3_value = -1
            self.saveconfig()
        except ValueError:
            self.line1_value = -1

    def input2_trigger(self, text):
        try:
            self.line2_value = int(text)
            config['settings']['scalew'] = str(self.line2_value)
            self.line1_value = -1
            config['settings']['scaleh'] = str(self.line1_value)
            self.line3_value = -1
            self.saveconfig()
        except ValueError:
            self.line2_value = -1

    def input3_trigger(self, text):
        try:
            self.line3_value = int(text)
            self.line2_value = -1
            self.line1_value = -1
        except ValueError:
            self.line3_value = -1

    def checkbox_trigger(self, state):
        if state == '0':
            config['settings']['resumereading'] = 'False'
        else:
            config['settings']['resumereading'] = 'True'


    # setting show/hide
    def settings_sh(self):
        settings_status = self.settings_widget1.isHidden()
        if settings_status is True:
            self.settings_widget1.show()
        else:
            self.settings_widget1.hide()

    def reset_default(self):
        config['settings'] = {'readercolor': '#282C34', 'settingscolor': '#31343F', 'scaleh': '-1', 'scalew': '-1'}
        readercr = QtGui.QColor(config['settings']['readercolor'])
        self.line1_value = -1
        self.line2_value = -1
        self.scrollArea.setStyleSheet('QWidget { background-color: %s; }' % readercr.name())
        self.apply()
        self.saveconfig()

    def resume_reading(self):
        if self.resume_checkbox.isChecked():
            if config['%s' % self.luder.adres]['resumepoint'] is not '0':
                self.scrollArea.verticalScrollBar().setValue(int(config['%s' % self.luder.adres]['resumepoint']))

    def res(self):
        try:
            self.resume_point = config['%s' % self.luder.adres]['resumepoint']
        except KeyError:
            config['%s' % self.luder.adres] = {'resumepoint': '0'}
        self.saveconfig()

    def file_open(self):
        adres = QtWidgets.QFileDialog.getExistingDirectory()
        if adres is '':
            pass
        else:
            self.luder.adres = adres
            if self.resume_checkbox.isChecked():
                self.res()
            self.cleaner()
            self.loader()

    def drop_open(self):
        if os.path.isfile(self.scrollArea.localadres):
            self.luder.adres = os.path.dirname(self.scrollArea.localadres)
            print(self.luder.adres)
        else:
            self.luder.adres = self.scrollArea.localadres
            print(self.luder.adres)

        if self.resume_checkbox.isChecked():
            self.res()
        self.cleaner()
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
        if self.line1_value is not -1:
            scaled = pixmap.scaledToHeight(self.line1_value, QtCore.Qt.SmoothTransformation)
            label.setPixmap(scaled)
        elif self.line2_value is not -1:
            scaled = pixmap.scaledToWidth(self.line2_value, QtCore.Qt.SmoothTransformation)
            label.setPixmap(scaled)
        else:
            label.setPixmap(pixmap)
        label.setScaledContents(False)
        label.setObjectName('image%s' % self.luder.order)
        label.setAlignment(QtCore.Qt.AlignHCenter)
        self.scrollAreaLayout.addWidget(label)

    def saveconfig(self):
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

class LoaderThread(QtCore.QThread):
    pics = QtCore.pyqtSignal(object)
    done = QtCore.pyqtSignal()

    def __init__(self):
        QtCore.QThread.__init__(self)

    def run(self):
        liste = os.listdir(self.adres)
        self.order = 0
        for i in liste:
            image = QtGui.QImage(self.adres + '/' + liste[self.order])
            self.pics.emit(image)
            self.order += 1
        self.done.emit()

if __name__ == "__main__":
    import sys
    import atexit
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'readercolor': '#282C34', 'settingscolor': '#31343F', 'scaleh': '-1', 'scalew': '-1', 'resumereading': 'False'}
    config.read('config.ini')
    try:
        print(config['settings']['readercolor'])
    except KeyError:
        config['settings'] = {'readercolor': '#282C34', 'settingscolor': '#31343F', 'scaleh': '-1', 'scalew': '-1', 'resumereading': 'False'}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    atexit.register(ui.saveconfig)
    sys.exit(app.exec_())
