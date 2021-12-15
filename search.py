from search_ui import Ui_Form
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QDialog
from PyQt5.QtCore import QThread, QObject, pyqtSignal
from PyQt5 import QtCore
from PyQt5 import QtWidgets
import sys
import os
import subprocess


class search(QThread):
	def __init__(self, logfile, savefile, mode, keyword):
		super().__init__()
		cmd_path = os.getcwd().split('\\')
		[cmd_path.append(i) for i in ['Core', 'SearchCore.exe']]
		cmd_path = '/'.join(cmd_path)
		self.cmd = ' '.join([cmd_path, logfile, savefile, mode, keyword])

	def run(self):
		subprocess.run(self.cmd)


class SearchWindow(QMainWindow, Ui_Form):

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pushButton.clicked.connect(self.__search)
		self.pushButton_2.clicked.connect(self.__open_file)
		self.filename = ''
		self.started = False
		self._translate = QtCore.QCoreApplication.translate

	def __open_file(self):
		if not self.started:
			filename, filetype = QFileDialog.getOpenFileName(self, 'file', os.getcwd(), "文本文档(*.txt);;日志文件(*.log)")

			self.filename = filename
			self.short_name = filename.split('/')[-1]

			if self.short_name != '':
				self.label_3.setText(self._translate("Form", self.short_name))
		else:
			self.__show_dialog_critical('当前有未结束任务！')

	def __show_dialog_critical(self, text):
		QtWidgets.QMessageBox.critical(self, '出现错误！', text)

	def __show_dialog_information(self, text):
		QtWidgets.QMessageBox.information(self, '注意！', text)

	def __search(self):

		if self.started:
			self.__show_dialog_critical('当前任务未结束！')
			return

		if self.filename == '':
			self.__show_dialog_critical('请选择日志文件！')
			return

		keyword = self.lineEdit.text()
		
		if keyword == '':
			self.__show_dialog_critical('请输入搜索命令！')
			return
		else:
			if '：' in keyword:
				mode = keyword.split('：')[0]
				lenght = len(mode)+1
				keyword = keyword[lenght:]
			else:
				self.__show_dialog_critical('请使用：（全角）分割命令与关键词！')
				return

		savefile = os.getcwd().split('\\')
		name = '_'.join([mode, keyword])
		savefile.append('search_result')
		test_path = '/'.join(savefile)
		if not os.path.isdir(test_path):
			os.mkdir(test_path)
		savefile.append(name)
		savefile = '/'.join(savefile) + '.log'

		self.thread = search(self.filename, savefile, mode, keyword)
		self.thread.start()


	def closeEvent(self, event):
		reply =QtWidgets.QMessageBox.question(self, '提示',"确定退出？", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

		if reply == QtWidgets.QMessageBox.Yes:
			subprocess.Popen("TASKKILL /F /im SearchCore.exe /T")
			event.accept()
		else:
			event.ignore()
