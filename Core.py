from aiowebsocket.converses import AioWebSocket
import asyncio
from sys import exit, argv
from zlib import decompress
import json
from time import time, asctime
from requests import post


class LiveDanmaku():

	def __init__(self, room_id, log_file, fans):
		self.url = 'wss://broadcastlv.chat.bilibili.com:2245/sub'
		self.roomid = room_id
		self.heartbeat = '00000010001000010000000200000001'
		self.data_raw = self.__get_data_raw()
		self.log_file_name = log_file
		self.fans = fans


	def __get_data_raw(self):
		data_raw = '000000{headerLen}0010000100000007000000017b22726f6f6d6964223a{roomid}7d'
		data_raw = data_raw.format(headerLen=hex(27 + len(self.roomid))[2:], 
			roomid=''.join(map(lambda x: hex(ord(x))[2:], list(self.roomid))))
		return data_raw

	def __decode_danmaku(self, data):
		packet_length = int(data[:4].hex(), 16)
		ver = int(data[6:8].hex(), 16)
		op = int(data[8:12].hex(), 16)

		if len(data) > packet_length:
			self.__decode_danmaku(data[packet_length:])
			data = data[:packet_length]

		if ver == 2:
			data = decompress(data[16:])
			self.__decode_danmaku(data)
			return

		if not ver:
			if op == 5:
				json_data = json.loads(data[16:].decode('utf-8', errors='ignore'))
				if json_data['cmd'] == 'DANMU_MSG':
					try:
						fans_info = str(json_data['info'][3][0]) + '-' + json_data['info'][3][1]
					except:
						fans_info = '0-0'
					msg = asctime() + '：：' + fans_info + '：：' + json_data['info'][2][1] + '-' + str(json_data['info'][2][0]) + '：：' + json_data['info'][1]
					print(msg)
					with open(self.log_file_name, 'a', encoding='utf-8') as file: 
						file.write(msg+'\n')

	def __decode_danmaku_without_fans(self, data):
		packet_length = int(data[:4].hex(), 16)
		ver = int(data[6:8].hex(), 16)
		op = int(data[8:12].hex(), 16)

		if len(data) > packet_length:
			self.__decode_danmaku_without_fans(data[packet_length:])
			data = data[:packet_length]

		if ver == 2:
			data = decompress(data[16:])
			self.__decode_danmaku_without_fans(data)
			return

		if not ver:
			if op == 5:
				json_data = json.loads(data[16:].decode('utf-8', errors='ignore'))
				if json_data['cmd'] == 'DANMU_MSG':
					msg = asctime() + '：：' + json_data['info'][2][1] + '-' + str(json_data['info'][2][0]) + '：：' + json_data['info'][1]
					print(msg)
					with open(self.log_file_name, 'a', encoding='utf-8') as file: 
						file.write(msg+'\n')

	async def __get_danmaku(self, websocket):
		start = time()
		while True:
			try:
				recv_text = await websocket.receive()
				self.__decode_danmaku(recv_text)
			except TypeError:
				pass

			now = time()
			if now - start > 60:
				await websocket.send(bytes.fromhex(self.heartbeat))
				start = now

	async def __get_danmaku_without_fans(self, websocket):
		start = time()
		while True:
			try:
				recv_text = await websocket.receive()
				self.__decode_danmaku_without_fans(recv_text)
			except TypeError:
				pass

			now = time()
			if now - start > 60:
				await websocket.send(bytes.fromhex(self.heartbeat))
				start = now

	async def __start(self):
		url = self.url
		async with AioWebSocket(url) as aws:
			converse = aws.manipulator
			await converse.send(bytes.fromhex(self.data_raw))
			tasks = [self.__get_danmaku(converse)]
			await asyncio.wait(tasks)

	async def __start_without_fans(self):
		url = self.url
		async with AioWebSocket(url) as aws:
			converse = aws.manipulator
			await converse.send(bytes.fromhex(self.data_raw))
			tasks = [self.__get_danmaku_without_fans(converse)]
			await asyncio.wait(tasks)

	def run(self):
		if self.fans == '1':
			asyncio.get_event_loop().run_until_complete(self.__start())
		else:
			asyncio.get_event_loop().run_until_complete(self.__start_without_fans())


dan = LiveDanmaku(room_id=argv[1], log_file=argv[2], fans=argv[3])
dan.run()