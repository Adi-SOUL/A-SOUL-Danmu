# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'danmu.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from aa_png import img as a 
import base64
import os
if not os.path.exists('a.png'):
        tmp = open('a.png', 'wb')
        tmp.write(base64.b64decode(a))
        tmp.close()

class Ui_LiveDanmaku(object):
    def setupUi(self, LiveDanmaku):
        LiveDanmaku.setObjectName("LiveDanmaku")
        LiveDanmaku.setFixedSize(995, 724)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LiveDanmaku.sizePolicy().hasHeightForWidth())
        LiveDanmaku.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(LiveDanmaku)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 520, 211, 101))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("font: 75 28pt \"等线\";\n"
"background-color:rgb(252, 150, 110);\n"
"border-radius: 30px;\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(550, 230, 381, 61))
        self.lineEdit.setStyleSheet("font: 16pt \"等线\";\n"
"border-radius: 30px;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 230, 171, 61))
        self.label.setStyleSheet("font: 16pt \"等线\";\n"
"background-color:rgb(255, 204, 170);\n"
"border-radius: 10px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 340, 181, 61))
        self.label_2.setStyleSheet("font: 16pt \"等线\";\n"
"background-color:rgb(255, 204, 170);\n"
"border-radius: 10px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(800, 340, 131, 61))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("font: 75 15pt \"等线\";\n"
"background-color:rgb(255, 230, 153);\n"
"border-radius: 25px;\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(550, 340, 241, 61))
        self.label_3.setStyleSheet("font: 16pt \"等线\";\n"
"background-color:rgb(255, 240, 185);\n"
"border-radius: 10px;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(510, 30, 271, 141))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("a.png"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(660, 520, 211, 101))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("font: 75 28pt \"等线\";\n"
"background-color:rgb(252, 150, 110);\n"
"border-radius: 30px;\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 40, 271, 621))
        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textBrowser.setStyleSheet("font: 75 28pt \"等线\";\n"
"border-radius: 50px;\n"
"background-color:rgb(242, 231, 255);\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(330, 190, 631, 471))
        self.label_5.setStyleSheet("background-color:rgb(231, 255, 241)")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(-20, -20, 1121, 731))
        self.label_6.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(730, 430, 101, 61))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("font: 75 15pt \"等线\";\n"
"background-color:rgb(255, 192, 192);\n"
"border-radius: 25px;\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(430, 430, 281, 61))
        self.label_7.setStyleSheet("font: 16pt \"等线\";\n"
"background-color:rgb(255, 225, 225);\n"
"border-radius: 10px;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_6.raise_()
        self.label_5.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.pushButton_3.raise_()
        self.textBrowser.raise_()
        self.pushButton_4.raise_()
        self.label_7.raise_()
        LiveDanmaku.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LiveDanmaku)
        self.statusbar.setObjectName("statusbar")
        LiveDanmaku.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(LiveDanmaku)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 995, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        LiveDanmaku.setMenuBar(self.menuBar)
        self.actionCheck_Files = QtWidgets.QAction(LiveDanmaku)
        self.actionCheck_Files.setObjectName("actionCheck_Files")
        self.menu.addAction(self.actionCheck_Files)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(LiveDanmaku)
        QtCore.QMetaObject.connectSlotsByName(LiveDanmaku)

    def retranslateUi(self, LiveDanmaku):
        _translate = QtCore.QCoreApplication.translate
        LiveDanmaku.setWindowTitle(_translate("LiveDanmaku", "LiveDanmaku"))
        self.pushButton.setText(_translate("LiveDanmaku", "开始"))
        self.label.setText(_translate("LiveDanmaku", "房间号"))
        self.label_2.setText(_translate("LiveDanmaku", "输出到文件："))
        self.pushButton_2.setText(_translate("LiveDanmaku", "选择文件"))
        self.label_3.setText(_translate("LiveDanmaku", "（未选择文件）"))
        self.pushButton_3.setText(_translate("LiveDanmaku", "结束"))
        self.textBrowser.setHtml(_translate("LiveDanmaku", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'等线\'; font-size:28pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:16pt; font-weight:600;\">备忘录：</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:16pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Helvetica Neue,Helvetica,Arial,PingFang SC,Hiragino Sans GB,Microsoft YaHei,sans-serif\'; font-size:14pt; font-weight:400; color:#212121;\">向晚大魔王：</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Helvetica Neue,Helvetica,Arial,PingFang SC,Hiragino Sans GB,Microsoft YaHei,sans-serif\'; font-size:14pt; font-weight:400; color:#212121;\">22625025</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system,BlinkMacSystemFont,Helvetica Neue,Helvetica,Arial,PingFang SC,Hiragino Sans GB,Microsoft YaHei,sans-serif\'; font-size:14pt; font-weight:400; color:#212121;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Helvetica Neue,Helvetica,Arial,PingFang SC,Hiragino Sans GB,Microsoft YaHei,sans-serif\'; font-size:14pt; font-weight:400; color:#212121;\">贝拉kira：</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Helvetica Neue,Helvetica,Arial,PingFang SC,Hiragino Sans GB,Microsoft YaHei,sans-serif\'; font-size:14pt; font-weight:400; color:#212121;\">22632424</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system,BlinkMacSystemFont,Helvetica Neue,Helvetica,Arial,PingFang SC,Hiragino Sans GB,Microsoft YaHei,sans-serif\'; font-size:14pt; font-weight:400; color:#212121;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Helvetica Neue,Helvetica,Arial,PingFang SC,Hiragino Sans GB,Microsoft YaHei,sans-serif\'; font-size:14pt; font-weight:400; color:#212121;\">珈乐Carol：</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Helvetica Neue,Helvetica,Arial,PingFang SC,Hiragino Sans GB,Microsoft YaHei,sans-serif\'; font-size:14pt; font-weight:400; color:#212121;\">22634198</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system,BlinkMacSystemFont,Helvetica Neue,Helvetica,Arial,PingFang SC,Hiragino Sans GB,Microsoft YaHei,sans-serif\'; font-size:14pt; font-weight:400; color:#212121;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Helvetica Neue,Helvetica,Arial,PingFang SC,Hiragino Sans GB,Microsoft YaHei,sans-serif\'; font-size:14pt; font-weight:400; color:#212121;\">嘉然今天吃什么：</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Helvetica Neue,Helvetica,Arial,PingFang SC,Hiragino Sans GB,Microsoft YaHei,sans-serif\'; font-size:14pt; font-weight:400; color:#212121;\">22637261</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system,BlinkMacSystemFont,Helvetica Neue,Helvetica,Arial,PingFang SC,Hiragino Sans GB,Microsoft YaHei,sans-serif\'; font-size:14pt; font-weight:400; color:#212121;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Helvetica Neue,Helvetica,Arial,PingFang SC,Hiragino Sans GB,Microsoft YaHei,sans-serif\'; font-size:14pt; font-weight:400; color:#212121;\">乃琳Queen：</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Helvetica Neue,Helvetica,Arial,PingFang SC,Hiragino Sans GB,Microsoft YaHei,sans-serif\'; font-size:14pt; font-weight:400; color:#212121;\">22625027</span></p></body></html>"))
        self.pushButton_4.setText(_translate("LiveDanmaku", "切换"))
        self.label_7.setText(_translate("LiveDanmaku", "当前：不显示粉丝牌"))
        self.menu.setTitle(_translate("LiveDanmaku", "工具"))
        self.actionCheck_Files.setText(_translate("LiveDanmaku", "搜索弹幕"))