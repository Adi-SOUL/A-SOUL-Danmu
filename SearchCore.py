from sys import argv

class SearchFile():

	def __init__(self, filename, savefile, mode, keywords):
		self.filename = filename
		self.savefile = savefile
		self.search_mode = mode
		if '；' in keywords:
			self.keywords_list = keywords.split('；；')
		else:
			self.keywords_list = keywords.split(';;')


	def __file_loader(self):
		msg = '正在读取：' + self.filename
		print(msg)

		self.log = []

		with open(self.filename, 'r', encoding='utf-8') as log_file:
			while True:
				this_line = log_file.readline()
				if not this_line:
					break
				if this_line[-1] == '\n':
					this_line = this_line[:-1]
				try:
					this_line_to_log = []
					info = this_line.split('：：')[1:]
					if len(info) == 3:
						this_line_to_log.append([info[0]])
						mark = 1
					else:
						this_line_to_log.append(['0-0'])
						mark = 0

					user_id = info[mark].split('-')[-1]
					user_name = info[mark][:-len(user_id)-1]
					this_line_to_log.append([user_name, user_id])

					this_line_to_log.append([info[-1]])

					this_line_to_log.append(this_line)

					self.log.append(this_line_to_log)
				except IndexError:
					pass
		print('文件读取完成！')

	def __next_(self, key_word):
		next_raw = [0]*40
		i, j = 0, -1
		next_raw[0] = -1
		while i < len(key_word)-1:
			if j == -1 or key_word[i] == key_word[j]:
				i = i + 1
				j = j + 1
				next_raw[i] = j
			else:
				j = next_raw[j]
		return next_raw

	def __kmp(self, search, key, nexts, find_all, reverse):
		i, j = 0, 0
		s_len, k_len = len(search), len(key)
		result = []
		if find_all:
			while i < s_len and j <= k_len:
				if search[i] == key[j]:
					i += 1
					j += 1
					if j >= k_len:
						result.append(i - k_len)
						j = 0
				else:
					if j == 0:
						i += 1
					else:
						j = nexts[j]
			if not reverse:
				return result
			else:
				return not result
		else:
			while i < s_len and j <= k_len:
				if search[i] == key[j]:
					i += 1
					j += 1
					if j >= k_len:
						if not reverse:
							return [i - k_len]
						else:
							return False
				else:
					if j == 0:
						i += 1
					else:
						j = nexts[j]
			if i == s_len:
				if not reverse:
					return []
				else:
					return True


	def __search(self):
		if 'F' in self.search_mode:
			F = True
			self.search_mode = self.search_mode[:-1]
		else:
			F = False

		if self.search_mode == 'fans':
			mark = 0
			mark_ = 0
		elif self.search_mode == 'id':
			mark = 1
			mark_ = 1
		elif self.search_mode == 'name':
			mark = 1
			mark_ = 0
		elif self.search_mode == 'danmu':
			mark = 2
			mark_ = 0
		else:
			print('错误的关键词！')
			print("关键词仅有：'fans'，'id'，'name'，'danmu'！")
			print("在关键词后加入F执行强制匹配搜索（对id关键词无效）")
			return

		if not F:
			for keyword in self.keywords_list:
				if keyword[-1] == '\n':
					keyword = keyword[:-1]
				for searching in self.log:
					searching_word = searching[mark][mark_]
					if not mark_:
						if not mark:
							if keyword.isdigit():
								print('不支持搜索粉丝牌等级！')
								return

							if keyword == searching_word:
								print(searching[-1])

								with open(self.savefile, 'a', encoding='utf-8') as resfile:
									resfile.write(searching[-1] + '\n')

							elif keyword in searching_word:
								print(searching[-1])

								with open(self.savefile, 'a', encoding='utf-8') as resfile:
									resfile.write(searching[-1] + '\n')
						else:		
							nexts = self.__next_(keyword)
							find = self.__kmp(searching_word, keyword, nexts, False, False)
							if find:
								print(searching[-1])

								with open(self.savefile, 'a', encoding='utf-8') as resfile:
									resfile.write(searching[-1] + '\n')
					else:
						if searching_word == keyword:
							print(searching[-1])

							with open(self.savefile, 'a', encoding='utf-8') as resfile:
								resfile.write(searching[-1] + '\n')
		else:
			for keyword in self.keywords_list:
				if keyword[-1] == '\n':
					keyword = keyword[:-1]
				for searching in self.log:
					searching_word = searching[mark][mark_]
					if not mark_:
						if not mark:
							if keyword.isdigit():
								print('不支持搜索粉丝牌等级！')
								return

							if keyword == searching_word.split('-')[-1]:
								print(searching[-1])

								with open(self.savefile, 'a', encoding='utf-8') as resfile:
									resfile.write(searching[-1] + '\n')
							elif keyword == searching_word:
								print(searching[-1])

								with open(self.savefile, 'a', encoding='utf-8') as resfile:
									resfile.write(searching[-1] + '\n')

						else:		
							if searching_word == keyword:
								print(searching[-1])

								with open(self.savefile, 'a', encoding='utf-8') as resfile:
									resfile.write(searching[-1] + '\n')
					else:
						if searching_word == keyword:
							print(searching[-1])

							with open(self.savefile, 'a', encoding='utf-8') as resfile:
								resfile.write(searching[-1] + '\n')

		print('查找已结束！')
		msg = '文件已经保存到：' + self.savefile
		print(msg)

	def run(self):

		self.__file_loader()
		self.__search()

search = SearchFile(filename=argv[1], savefile=argv[2], mode=argv[3], keywords=argv[4])
search.run()