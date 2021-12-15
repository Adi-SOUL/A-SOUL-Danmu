from fin_1_1 import Ui_LiveDanmaku
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QDialog, QApplication
from PyQt5.QtCore import QThread, QObject, pyqtSignal
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from time import sleep
from requests import post
import subprocess
from exceptions import LiveEnd, RoomError, FileError, EarlyStop
import os
import asyncio
import sys
from search import SearchWindow

class Check(QThread):

	trigger = pyqtSignal(str)

	def __init__(self, roomid):
		super().__init__()
		self.room_id = roomid

	def run(self):
		stop = False
		while not stop:
			room_id_url = 'https://api.live.bilibili.com/room/v1/Room/room_init?id={}'.format(self.room_id)
			headers = {
				'Host' : 'api.live.bilibili.com',
				'User-Agent' : 'Mozilla/5.0'
			}
			try:
				raw_room_info = post(url=room_id_url, headers=headers).json()['data']
				status = str(raw_room_info['live_status'])
			except:
				status = '1'

			if status != '1':
				self.trigger.emit('finish')
				stop = True

			sleep(1)


class Get(QThread):
	def __init__(self, roomid, log_file, fans):
		super().__init__()
		cmd_path = os.getcwd().split('\\')
		[cmd_path.append(i) for i in ['Core', 'LiveCore.exe']]
		cmd_path = '/'.join(cmd_path)
		self.cmd = ' '.join([cmd_path, roomid, log_file, str(fans)])

	def run(self):
		subprocess.run(self.cmd)


class Window(QMainWindow, Ui_LiveDanmaku):

	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.pushButton.clicked.connect(self.__start)
		self.pushButton_2.clicked.connect(self.__open_file)
		self.pushButton_3.clicked.connect(self.__stop)
		self.pushButton_4.clicked.connect(self.__change_fans)
		self.actionCheck_Files.triggered.connect(self.__show_subwindow)

		self._translate = QtCore.QCoreApplication.translate
		self.started = False
		self.filename = ''
		self.short_name = ''
		self.thread = None
		self.fans = 0

	def __get_room_info(self, room_id):
		room_id_url = 'https://api.live.bilibili.com/room/v1/Room/room_init?id={}'.format(room_id)
		headers = {
			'Host' : 'api.live.bilibili.com',
			'User-Agent' : 'Mozilla/5.0'
		}
		raw_room_info = post(url=room_id_url, headers=headers).json()['data']
		status = str(raw_room_info['live_status'])
		roomid = raw_room_info['room_id']
		return str(roomid), status

	def __show_dialog_critical(self, text):
		QtWidgets.QMessageBox.critical(self, '出现错误！', text)

	def __show_dialog_information(self, text):
		QtWidgets.QMessageBox.information(self, '注意！', text)

	def __show_subwindow(self):
		self.subwindow = SearchWindow()
		self.subwindow.show()

	def __open_file(self):
		if not self.started:
			filename, filetype = QFileDialog.getOpenFileName(self, 'file', os.getcwd(), "文本文档(*.txt);;日志文件(*.log)")

			self.filename = filename
			self.short_name = filename.split('/')[-1]

			if self.short_name != '':
				self.label_3.setText(self._translate("LiveDanmaku", self.short_name))
		else:
			self.__show_dialog_critical('当前有未结束任务！')

	def __change_fans(self):
		if self.started:
			self.__show_dialog_critical('请先关闭任务再进行切换！')
			return

		if self.fans:
			self.fans = 0
			self.label_7.setText(self._translate("LiveDanmaku", '当前：不显示粉丝牌'))
		else:
			self.fans = 1
			self.label_7.setText(self._translate("LiveDanmaku", '当前：显示粉丝牌'))	


	def __start(self):
		try:
			raw_room = self.lineEdit.text()
			self.roomid, self.status = self.__get_room_info(raw_room)
		except TypeError:
			self.__show_dialog_critical('请输入正确的房间号！')
			self.lineEdit.setText(self._translate("LiveDanmaku", ''))
			return	

		try:
			if self.started:
				raise Exception
		except Exception:
			self.__show_dialog_critical('当前有正在进行的任务！')
			return

		try:
			if self.short_name == '':
				raise FileError
			if self.roomid == '':
				raise RoomError
			if self.status != '1':
				raise LiveEnd
			'''
			run here
			'''
			self.thread_run = Get(self.roomid, self.filename, self.fans)
			self.thread_run.start()

			# subprocess.Popen('cls')

			if not self.started:
				self.__show_dialog_information('开始录制！')
				self.started = True
			'''
			check here
			'''
			self.thread = Check(raw_room)
			self.thread.trigger.connect(self.__finsh)
			self.thread.start()

		except FileError:
			self.__show_dialog_critical('请选择文件位置！')
			return 
		except RoomError:
			self.__show_dialog_critical('请输入房间号！')	
			return
		except LiveEnd:
			self.__show_dialog_information('当前直播间未在直播！')
			self.lineEdit.setText(self._translate("LiveDanmaku", ''))
			return 

	def __finsh(self, finish):
		if finish == 'finish':
			subprocess.Popen("TASKKILL /F /im LiveCore.exe /T")
			msg = '录制已经结束，文件已经保存到：' + self.filename
			self.__show_dialog_information(msg)
			self.roomid = ''
			self.lineEdit.setText(self._translate("LiveDanmaku", ''))
			self.filename = ''
			self.label_3.setText(self._translate("LiveDanmaku", "（未选择文件）"))

	def __stop(self):
		try:
			if self.thread == None:
				raise EarlyStop
		except EarlyStop:
			self.__show_dialog_critical('请先开始记录！')
			return

		if self.started:
			subprocess.Popen("TASKKILL /F /im LiveCore.exe /T")
			self.started = False
			msg = '录制已经结束，文件已经保存到：' + self.filename
			self.roomid = ''
			self.lineEdit.setText(self._translate("LiveDanmaku", ''))
			self.filename = ''
			self.label_3.setText(self._translate("LiveDanmaku", "（未选择文件）"))

			self.__show_dialog_information(msg)
		else:
			self.__show_dialog_critical('请先开始记录！')

	def closeEvent(self, event):
		reply =QtWidgets.QMessageBox.question(self, '提示',"确定退出？", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

		if reply == QtWidgets.QMessageBox.Yes:
			if self.started:
				subprocess.Popen("TASKKILL /F /im LiveCore.exe /T")
			sys.exit(0)
			event.accept()
		else:
			event.ignore()