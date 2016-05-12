# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'workflow.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mwWorkFlow(object):
    def setupUi(self, mwWorkFlow):
        mwWorkFlow.setObjectName("mwWorkFlow")
        mwWorkFlow.resize(876, 700)
        mwWorkFlow.setStyleSheet("QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #d7801a;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QListView\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(images/ui/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QGroupBox {\n"
"    background-color: #323232;\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 5px; /* leave space at the top for the title */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px ;\n"
"     /*background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #FF0ECE, stop: 1 #FFFFFF);*/\n"
"    \n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(images/ui/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image: url(images/ui/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}      ")
        self.centralwidget = QtWidgets.QWidget(mwWorkFlow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 761, 661))
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaContents = QtWidgets.QWidget()
        self.scrollAreaContents.setGeometry(QtCore.QRect(0, 0, 754, 654))
        self.scrollAreaContents.setObjectName("scrollAreaContents")
        self.stackWorkFlow = QtWidgets.QStackedWidget(self.scrollAreaContents)
        self.stackWorkFlow.setGeometry(QtCore.QRect(10, 4, 751, 701))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.stackWorkFlow.sizePolicy().hasHeightForWidth())
        self.stackWorkFlow.setSizePolicy(sizePolicy)
        self.stackWorkFlow.setStyleSheet("")
        self.stackWorkFlow.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackWorkFlow.setObjectName("stackWorkFlow")
        self.Home = QtWidgets.QWidget()
        self.Home.setObjectName("Home")
        self.label_3 = QtWidgets.QLabel(self.Home)
        self.label_3.setGeometry(QtCore.QRect(40, 110, 381, 16))
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(self.Home)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 171, 51))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/images/images/ui/pixi_logo_new.png"))
        self.label_9.setObjectName("label_9")
        self.lblWelcome = QtWidgets.QLabel(self.Home)
        self.lblWelcome.setGeometry(QtCore.QRect(10, 80, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lblWelcome.setFont(font)
        self.lblWelcome.setObjectName("lblWelcome")
        self.stackWorkFlow.addWidget(self.Home)
        self.runAll = QtWidgets.QWidget()
        self.runAll.setObjectName("runAll")
        self.gbCheck = QtWidgets.QGroupBox(self.runAll)
        self.gbCheck.setGeometry(QtCore.QRect(10, 40, 101, 121))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.gbCheck.sizePolicy().hasHeightForWidth())
        self.gbCheck.setSizePolicy(sizePolicy)
        self.gbCheck.setStyleSheet("")
        self.gbCheck.setTitle("")
        self.gbCheck.setCheckable(False)
        self.gbCheck.setObjectName("gbCheck")
        self.chkAllStatic = QtWidgets.QCheckBox(self.gbCheck)
        self.chkAllStatic.setGeometry(QtCore.QRect(14, 24, 70, 17))
        self.chkAllStatic.setCheckable(True)
        self.chkAllStatic.setChecked(False)
        self.chkAllStatic.setTristate(False)
        self.chkAllStatic.setObjectName("chkAllStatic")
        self.chkAllPng = QtWidgets.QCheckBox(self.gbCheck)
        self.chkAllPng.setGeometry(QtCore.QRect(14, 44, 70, 17))
        self.chkAllPng.setObjectName("chkAllPng")
        self.btnRunAll = QtWidgets.QPushButton(self.gbCheck)
        self.btnRunAll.setGeometry(QtCore.QRect(12, 80, 75, 23))
        self.btnRunAll.setObjectName("btnRunAll")
        self.lblRunSku_2 = QtWidgets.QLabel(self.runAll)
        self.lblRunSku_2.setGeometry(QtCore.QRect(0, 10, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lblRunSku_2.setFont(font)
        self.lblRunSku_2.setStyleSheet("")
        self.lblRunSku_2.setObjectName("lblRunSku_2")
        self.stackWorkFlow.addWidget(self.runAll)
        self.SKU = QtWidgets.QWidget()
        self.SKU.setObjectName("SKU")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.SKU)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 50, 233, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.hbSkuEnter = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.hbSkuEnter.setContentsMargins(0, 0, 0, 0)
        self.hbSkuEnter.setObjectName("hbSkuEnter")
        self.lblSkuEnter = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lblSkuEnter.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lblSkuEnter.setFont(font)
        self.lblSkuEnter.setObjectName("lblSkuEnter")
        self.hbSkuEnter.addWidget(self.lblSkuEnter)
        self.leSkuEnter = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leSkuEnter.sizePolicy().hasHeightForWidth())
        self.leSkuEnter.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.leSkuEnter.setFont(font)
        self.leSkuEnter.setText("")
        self.leSkuEnter.setMaxLength(4)
        self.leSkuEnter.setClearButtonEnabled(False)
        self.leSkuEnter.setObjectName("leSkuEnter")
        self.hbSkuEnter.addWidget(self.leSkuEnter)
        spacerItem = QtWidgets.QSpacerItem(75, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hbSkuEnter.addItem(spacerItem)
        self.btnLoadSku = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnLoadSku.setMinimumSize(QtCore.QSize(75, 0))
        self.btnLoadSku.setObjectName("btnLoadSku")
        self.hbSkuEnter.addWidget(self.btnLoadSku)
        self.lblRunSku = QtWidgets.QLabel(self.SKU)
        self.lblRunSku.setGeometry(QtCore.QRect(0, 10, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lblRunSku.setFont(font)
        self.lblRunSku.setObjectName("lblRunSku")
        self.cbNameTypes = QtWidgets.QComboBox(self.SKU)
        self.cbNameTypes.setEnabled(False)
        self.cbNameTypes.setGeometry(QtCore.QRect(30, 90, 121, 22))
        self.cbNameTypes.setObjectName("cbNameTypes")
        self.gbGarments = QtWidgets.QGroupBox(self.SKU)
        self.gbGarments.setEnabled(True)
        self.gbGarments.setGeometry(QtCore.QRect(30, 120, 701, 521))
        self.gbGarments.setObjectName("gbGarments")
        self.scrollGarms = QtWidgets.QScrollArea(self.gbGarments)
        self.scrollGarms.setGeometry(QtCore.QRect(10, 20, 681, 491))
        self.scrollGarms.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollGarms.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollGarms.setWidgetResizable(False)
        self.scrollGarms.setObjectName("scrollGarms")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 681, 484))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollGarms.setWidget(self.scrollAreaWidgetContents)
        self.stackWorkFlow.addWidget(self.SKU)
        self.scrollArea.setWidget(self.scrollAreaContents)
        mwWorkFlow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mwWorkFlow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 876, 21))
        self.menubar.setObjectName("menubar")
        self.menuMain = QtWidgets.QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        mwWorkFlow.setMenuBar(self.menubar)
        self.dwTools = QtWidgets.QDockWidget(mwWorkFlow)
        self.dwTools.setMinimumSize(QtCore.QSize(100, 29))
        self.dwTools.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dwTools.setObjectName("dwTools")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.dockWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(6, 20, 91, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnHome = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnHome.setObjectName("btnHome")
        self.verticalLayout.addWidget(self.btnHome)
        self.btnShowRunAll = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnShowRunAll.setObjectName("btnShowRunAll")
        self.verticalLayout.addWidget(self.btnShowRunAll)
        self.btnShowSku = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnShowSku.setObjectName("btnShowSku")
        self.verticalLayout.addWidget(self.btnShowSku)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.dwTools.setWidget(self.dockWidgetContents)
        mwWorkFlow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dwTools)
        self.actionQuit = QtWidgets.QAction(mwWorkFlow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionTools = QtWidgets.QAction(mwWorkFlow)
        self.actionTools.setObjectName("actionTools")
        self.menuMain.addAction(self.actionQuit)
        self.menuView.addAction(self.actionTools)
        self.menubar.addAction(self.menuMain.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(mwWorkFlow)
        self.stackWorkFlow.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(mwWorkFlow)
        mwWorkFlow.setTabOrder(self.leSkuEnter, self.btnLoadSku)
        mwWorkFlow.setTabOrder(self.btnLoadSku, self.cbNameTypes)
        mwWorkFlow.setTabOrder(self.cbNameTypes, self.chkAllStatic)
        mwWorkFlow.setTabOrder(self.chkAllStatic, self.chkAllPng)
        mwWorkFlow.setTabOrder(self.chkAllPng, self.btnRunAll)
        mwWorkFlow.setTabOrder(self.btnRunAll, self.btnHome)
        mwWorkFlow.setTabOrder(self.btnHome, self.btnShowRunAll)
        mwWorkFlow.setTabOrder(self.btnShowRunAll, self.btnShowSku)
        mwWorkFlow.setTabOrder(self.btnShowSku, self.pushButton_3)
        mwWorkFlow.setTabOrder(self.pushButton_3, self.scrollArea)

    def retranslateUi(self, mwWorkFlow):
        _translate = QtCore.QCoreApplication.translate
        mwWorkFlow.setWindowTitle(_translate("mwWorkFlow", "InkPixi Web Art Workflow Thing"))
        self.label_3.setText(_translate("mwWorkFlow", "Some stuff here, maybe instructions, a menu, resources, or whateves..."))
        self.lblWelcome.setText(_translate("mwWorkFlow", "lblWelcome"))
        self.chkAllStatic.setText(_translate("mwWorkFlow", "Static"))
        self.chkAllPng.setText(_translate("mwWorkFlow", "PNG"))
        self.btnRunAll.setText(_translate("mwWorkFlow", "Run"))
        self.lblRunSku_2.setText(_translate("mwWorkFlow", "Run All SKU\'s"))
        self.lblSkuEnter.setText(_translate("mwWorkFlow", "Enter SKU:"))
        self.leSkuEnter.setPlaceholderText(_translate("mwWorkFlow", "SKU"))
        self.btnLoadSku.setText(_translate("mwWorkFlow", "Load"))
        self.lblRunSku.setText(_translate("mwWorkFlow", "Individual SKU"))
        self.gbGarments.setTitle(_translate("mwWorkFlow", "Garments"))
        self.menuMain.setTitle(_translate("mwWorkFlow", "Menu"))
        self.menuEdit.setTitle(_translate("mwWorkFlow", "Edit"))
        self.menuView.setTitle(_translate("mwWorkFlow", "View"))
        self.dwTools.setWindowTitle(_translate("mwWorkFlow", "Tools"))
        self.btnHome.setText(_translate("mwWorkFlow", "Home"))
        self.btnShowRunAll.setText(_translate("mwWorkFlow", "Run All"))
        self.btnShowSku.setText(_translate("mwWorkFlow", "SKU"))
        self.pushButton_3.setText(_translate("mwWorkFlow", "PushButton"))
        self.actionQuit.setText(_translate("mwWorkFlow", "&Quit"))
        self.actionQuit.setToolTip(_translate("mwWorkFlow", "Exit Application"))
        self.actionTools.setText(_translate("mwWorkFlow", "Tools"))

import image_rc
