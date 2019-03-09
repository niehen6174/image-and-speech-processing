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

class Ui_MainWindow3(object):
    def setupUi(self, Ui_MainWindow3):
        Ui_MainWindow3.setObjectName("Ui_MainWindow3")
        Ui_MainWindow3.resize(511, 367)

        self.main_widget = QtWidgets.QWidget(Ui_MainWindow3)  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        self.main_widget.setObjectName("main_widget")

        self.pushbutton_close = QtWidgets.QPushButton(Ui_MainWindow3)
        self.pushbutton_close.setGeometry(QtCore.QRect(30, 20, 30, 30))
        self.pushbutton_close.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Ui_MainWindow3)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 20, 30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushbutton_mini = QtWidgets.QPushButton(Ui_MainWindow3)
        self.pushbutton_mini.setGeometry(QtCore.QRect(130, 20, 30, 30))
        self.pushbutton_mini.setObjectName("pushbutton_mini")
        self.text_label = QtWidgets.QLabel(Ui_MainWindow3)

        #self.text_label.setPlaceholderText("  输入要合成的语句，点击下面的按钮")
        #self.main_layout.addWidget(self.pushbutton_mini)

        self.text_label.setGeometry(QtCore.QRect(80, 130, 351, 91))

        self.text_label.setObjectName("text_label")
        self.pushButton = QtWidgets.QPushButton(Ui_MainWindow3)
        self.pushButton.setGeometry(QtCore.QRect(190, 250, 101, 71))
        self.pushButton.setObjectName("pushbutton_close")
        # self.pushbutton_close = QtWidgets.QPushButton(qtawesome.icon('fa5s.microphone',color='red'),"")
        self.label = QtWidgets.QLabel(Ui_MainWindow3)
        self.label.setGeometry(QtCore.QRect(80, 60, 351, 70))
        # font = QtGui.QFont()
        # font.setPointSize(18)
        # self.label.setFont(font)
        self.label.setObjectName("label")

        #----------------------------------


        spin_icon = qtawesome.icon('fa5s.microphone-alt', color='white')
        self.pushButton.setIcon(spin_icon)#设置图标
        self.pushButton.setIconSize(QtCore.QSize(50,50))



        self.retranslateUi(Ui_MainWindow3)
        QtCore.QMetaObject.connectSlotsByName(Ui_MainWindow3)

    def retranslateUi(self, Ui_MainWindow3):
        _translate = QtCore.QCoreApplication.translate
        Ui_MainWindow3.setWindowTitle(_translate("Ui_MainWindow3", "Ui_MainWindow3"))
        self.pushbutton_close.setText(_translate("Ui_MainWindow3", ""))
        self.pushButton_2.setText(_translate("Ui_MainWindow3", ""))
        self.pushbutton_mini.setText(_translate("Ui_MainWindow3", ""))
        self.pushButton.setText(_translate("Ui_MainWindow3", ""))
        self.label.setText(_translate("Ui_MainWindow3", "语音识别"))
        self.text_label.setText("点击下面的按钮开始录制音频\n再次点击停止录音开始识别")
        self.text_label.setAlignment(Qt.AlignCenter)
        self.label.setAlignment(Qt.AlignCenter)
        Ui_MainWindow3.setWindowOpacity(1) # 设置窗口透明度
        #Ui_MainWindow3.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
        Ui_MainWindow3.setWindowFlag(QtCore.Qt.FramelessWindowHint) # 隐藏边框
        pe = QPalette()
        Ui_MainWindow3.setAutoFillBackground(True)
        pe.setColor(QPalette.Window,Qt.lightGray)  #设置背景色
        #pe.setColor(QPalette.Background,Qt.blue)
        Ui_MainWindow3.setPalette(pe)
        #美化左上角三个按钮
        self.pushbutton_close.setStyleSheet('''QPushButton{background:#F76677;border-radius:15px;}QPushButton:hover{background:red;}''')
        self.pushButton_2.setStyleSheet('''QPushButton{background:#F7D674;border-radius:15px;}QPushButton:hover{background:yellow;}''')
        self.pushbutton_mini.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:15px;}QPushButton:hover{background:green;}''')
        self.main_widget.setStyleSheet('''QWidegt{border-top-right-radius:20px;
                    border-bottom-right-radius:40px;
                                    }''')
        self.label.setStyleSheet('''QLabel{color:white;font-size:40px;font-family:Roman times;}''')
        self.text_label.setStyleSheet('''QLabel{color:darkGray;background:white;border:2px solid #F3F3F5;border-radius:45px;
                font-size:14pt; font-weight:400;font-family: Roman times;} ''')
        self.pushButton.setStyleSheet('''QPushButton{border:none;}
        QPushButton:hover{color:white;
                    border:2px solid #F3F3F5;
                    border-radius:35px;
                    background:darkGray;}''')
        spin_icon = qtawesome.icon('fa5s.microphone-alt', color='black')
        #self.pushButton.setIcon(spin_icon)#设置图标
        Ui_MainWindow3.setWindowIcon(spin_icon)

        Ui_MainWindow3.setWindowOpacity(0.9)
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
    ui = Ui_MainWindow3()
    ui.setupUi(widgets)
    widgets.show()
    sys.exit(app.exec_())