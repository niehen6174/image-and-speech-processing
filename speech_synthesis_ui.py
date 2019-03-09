# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'speech_synthesis.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
import sys
import qtawesome

class Ui_MainWindow2(object):
    def setupUi(self, Ui_MainWindow2):
        Ui_MainWindow2.setObjectName("Ui_MainWindow2")
        Ui_MainWindow2.resize(511, 367)

        self.main_widget = QtWidgets.QWidget(Ui_MainWindow2)  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        self.main_widget.setObjectName("main_widget")

        self.pushbutton_close = QtWidgets.QPushButton(Ui_MainWindow2)
        self.pushbutton_close.setGeometry(QtCore.QRect(30, 20, 30, 30))
        self.pushbutton_close.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Ui_MainWindow2)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 20, 30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushbutton_mini = QtWidgets.QPushButton(Ui_MainWindow2)
        self.pushbutton_mini.setGeometry(QtCore.QRect(130, 20, 30, 30))
        self.pushbutton_mini.setObjectName("pushbutton_mini")
        self.textEdit = QtWidgets.QLineEdit(Ui_MainWindow2)

        self.textEdit.setPlaceholderText("  输入要合成的语句，点击下面的按钮")
        #self.main_layout.addWidget(self.pushbutton_mini)

        self.textEdit.setGeometry(QtCore.QRect(80, 130, 351, 91))

        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Ui_MainWindow2)
        self.pushButton.setGeometry(QtCore.QRect(190, 250, 101, 71))
        self.pushButton.setObjectName("pushbutton_close")
        # self.pushbutton_close = QtWidgets.QPushButton(qtawesome.icon('fa5s.microphone',color='red'),"")
        self.label = QtWidgets.QLabel(Ui_MainWindow2)
        self.label.setGeometry(QtCore.QRect(80, 60, 351, 70))
        # font = QtGui.QFont()
        # font.setPointSize(18)
        # self.label.setFont(font)
        self.label.setObjectName("label")

        #----------------------------------


        spin_icon = qtawesome.icon('fa5s.microphone', color='white')
        self.pushButton.setIcon(spin_icon)#设置图标
        self.pushButton.setIconSize(QtCore.QSize(50,50))



        self.retranslateUi(Ui_MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(Ui_MainWindow2)

    def retranslateUi(self, Ui_MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        Ui_MainWindow2.setWindowTitle(_translate("Ui_MainWindow2", "Ui_MainWindow2"))
        self.pushbutton_close.setText(_translate("Ui_MainWindow2", ""))
        self.pushButton_2.setText(_translate("Ui_MainWindow2", ""))
        self.pushbutton_mini.setText(_translate("Ui_MainWindow2", ""))
        self.pushButton.setText(_translate("Ui_MainWindow2", ""))
        self.label.setText(_translate("Ui_MainWindow2", "语音合成"))

        self.label.setAlignment(Qt.AlignCenter)
        Ui_MainWindow2.setWindowOpacity(1) # 设置窗口透明度
        #Ui_MainWindow2.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
        Ui_MainWindow2.setWindowFlag(QtCore.Qt.FramelessWindowHint) # 隐藏边框
        pe = QPalette()
        Ui_MainWindow2.setAutoFillBackground(True)
        pe.setColor(QPalette.Window,Qt.lightGray)  #设置背景色
        #pe.setColor(QPalette.Background,Qt.blue)
        Ui_MainWindow2.setPalette(pe)
        #美化左上角三个按钮
        self.pushbutton_close.setStyleSheet('''QPushButton{background:#F76677;border-radius:15px;}QPushButton:hover{background:red;}''')
        self.pushButton_2.setStyleSheet('''QPushButton{background:#F7D674;border-radius:15px;}QPushButton:hover{background:yellow;}''')
        self.pushbutton_mini.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:15px;}QPushButton:hover{background:green;}''')
        self.main_widget.setStyleSheet('''QWidegt{border-top-right-radius:20px;
                    border-bottom-right-radius:40px;
                                    }''')
        self.label.setStyleSheet('''QLabel{color:white;font-size:40px;font-family:Roman times;}''')
        self.textEdit.setStyleSheet('''QLineEdit{background:white;border:2px solid #F3F3F5;border-radius:45px;
                font-size:14pt; font-weight:400;font-family: "宋体";} ''')
        self.pushButton.setStyleSheet('''QPushButton{border:none;}
        QPushButton:hover{color:white;
                    border:2px solid #F3F3F5;
                    border-radius:35px;
                    background:darkGray;}''')
        Ui_MainWindow2.setWindowOpacity(0.9)  #设置透明度
        spin_icon = qtawesome.icon('fa5s.microphone', color='black')
        #self.pushButton.setIcon(spin_icon)#设置图标
        Ui_MainWindow2.setWindowIcon(spin_icon)
    def mousePressEvent(self, event):
        if event.button()==QtCore.Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  #更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widgets = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(widgets)
    widgets.show()
    sys.exit(app.exec_())