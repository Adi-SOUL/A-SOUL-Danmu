from aiowebsocket.converses import AioWebSocket
from asyncio.streams import IncompleteReadError
import asyncio
from sys import exit
from zlib import decompress
import json
from time import time, asctime
from requests import post
 

class LiveEnd(Exception):
	def __init__(self, *args):
		self.args = args


class LiveDanmaku():

	def __init__(self, room_id:int, log_file:str):
		self.url = 'wss://broadcastlv.chat.bilibili.com:2245/sub'
		self.roomid = self.__get_real_id(room_id)
		self.heartbeat = '00000010001000010000000200000001'
		self.data_raw = self.__get_data_raw()
		self.__dont_stop = True
		self.__log_file = open(log_file, 'a', encoding='utf-8')

	def __get_real_id(self, room_id):

		room_id_url = 'https://api.live.bilibili.com/room/v1/Room/room_init?id={}'.format(room_id)
		headers = {
			'Host' : 'api.live.bilibili.com',
			'User-Agent' : 'Mozilla/5.0'
		}
		raw_room_info = post(url=room_id_url, headers=headers).json()['data']
		self.status = str(raw_room_info['live_status'])
		roomid = raw_room_info['room_id']
		return str(roomid)

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
					msg = asctime() + '：' +json_data['info'][2][1] + '：' + json_data['info'][1]
					self.__log_file.write(msg+'\n')

				elif json_data['cmd'] == 'PREPARING':
					raise LiveEnd

	async def __get_danmaku(self, websocket):
		start = time()
		while self.__dont_stop:
			try:
				recv_text = await websocket.receive()
				self.__decode_danmaku(recv_text)
			except TypeError:
				pass
			except IncompleteReadError:
				raise LiveEnd

			now = time()
			if now - start > 60:
				await websocket.send(bytes.fromhex(self.heartbeat))
				print('Sent HeartBeat.')
				start = now

	async def start(self):
		url = self.url
		async with AioWebSocket(url) as aws:
			converse = aws.manipulator
			await converse.send(bytes.fromhex(self.data_raw))
			tasks = [self.__get_danmaku(converse)]
			await asyncio.wait(tasks)

	async def run(self):
		if self.status != '1':
			raise LiveEnd

		return  self.start
		'''try:
			asyncio.get_event_loop().run_until_complete(self.__start())
		except KeyboardInterrupt:
			self.__log_file.close()
			print('QUIT')
		'''
	def stop(self):
		self.__dont_stop = False
		self.__log_file.close()

if __name__ == '__main__':
	d = LiveDanmaku('3044248', 'test.log')
	d.run()