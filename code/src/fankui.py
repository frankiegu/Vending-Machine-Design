# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fankui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(927, 778)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 20, 471, 151))
        font = QtGui.QFont()
        font.setFamily("新蒂下午茶体")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 640, 256, 81))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(17)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 227, 221, 81))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(17)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 446, 221, 81))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(17)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(600, 177, 256, 181))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(600, 386, 256, 192))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(510, 256, 91, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(509, 475, 91, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.shoujihao = QtWidgets.QLineEdit(self.centralwidget)
        self.shoujihao.setGeometry(QtCore.QRect(60, 227, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.shoujihao.setFont(font)
        self.shoujihao.setObjectName("shoujihao")
        self.dingdanid = QtWidgets.QLineEdit(self.centralwidget)
        self.dingdanid.setGeometry(QtCore.QRect(60, 446, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.dingdanid.setFont(font)
        self.dingdanid.setObjectName("dingdanid")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(240, 256, 51, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(240, 476, 51, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.dingdanid_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.dingdanid_2.setGeometry(QtCore.QRect(60, 638, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.dingdanid_2.setFont(font)
        self.dingdanid_2.setObjectName("dingdanid_2")
        self.dingdanid_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.dingdanid_4.setGeometry(QtCore.QRect(290, 638, 221, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.dingdanid_4.setFont(font)
        self.dingdanid_4.setObjectName("dingdanid_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(510, 670, 91, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(240, 670, 51, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(100, 80, 152, 125))
        self.graphicsView.setObjectName("graphicsView")
        #MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 927, 21))
        self.menubar.setObjectName("menubar")
        #MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "客服界面"))
        self.pushButton.setText(_translate("MainWindow", "添加维修记录"))
        self.pushButton_3.setText(_translate("MainWindow", "查看购买订单"))
        self.pushButton_4.setText(_translate("MainWindow", "查看购买明细"))
class fankui_window(QtWidgets.QWidget, Ui_MainWindow):  # 创建子UI类

    def __init__(self):
        super(fankui_window, self).__init__()
        self.setupUi(self)
        self.graphicsView.setStyleSheet("border-image: url(C://Users//Ben//Desktop//xf//facial_emotion_recognition__EMOJIFIER-master//shouhou.png);")

