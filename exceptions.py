class RoomError(Exception):
	def __init__(self, *args):
		self.args = args


class FileError(Exception):
	def __init__(self, *args):
		self.args = args


class EarlyStop(Exception):
	def __init__(self, *args):
		self.args = args


class LiveEnd(Exception):
	def __init__(self, *args):
		self.args = args
