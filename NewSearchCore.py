from sys import argv, exit
import os

class SearchFile():
	'''
	filename/
	'''
	def __init__(self, filename, mode, keywords):
		'''
		解析搜索内容-->判断是否搜索过-->执行命令
		'''
		self.__log_filename = filename
		self.__raw_mode = mode
		self.__raw_keywords = keywords

		self.__handle_mode_keywords()
		new_search = self.__handle_where_to_save()
		if new_search:
			self.__run()
		else:
			self.__dont_run()

	def __handle_mode_keywords(self):
		'''
		'''
		if self.__raw_mode[0] == 'N':
			self.__new = True
			self.__raw_mode = self.__raw_mode[1:]
		else:
			self.__new = False

		self.__copy_raw_mode = self.__raw_mode

		if self.__raw_mode[-1] == 'C':
			self.__count = True
			self.__raw_mode = self.__raw_mode[:-1]
		else:
			self.__count = False

		if self.__raw_mode[-1] == 'F':
			self.__force = True
			self.__raw_mode = self.__raw_mode[:-1]
		else:
			self.__force = False

		if self.__raw_mode == 'fans':
			self.__mark = 0
			self.__mark_ = 0
		elif self.__raw_mode == 'id':
			self.__mark = 1
			self.__mark_ = 1
		elif self.__raw_mode == 'name':
			self.__mark = 1
			self.__mark_ = 0
		elif self.__raw_mode == 'danmu':
			self.__mark = 2
			self.__mark_ = 0
		elif self.__raw_mode =='user':
			pass
		elif self.__raw_mode == 'total':
			pass
		else:
			print('关键词错误！')
			exit(0)

		if '；；' in self.__raw_keywords:
			self.__keywords_list = self.__raw_keywords.strip('；；').split('；；')
		else:
			self.__keywords_list = self.__raw_keywords.strip(';;').split(';;')

		if self.__raw_mode == 'user':
			self.__keywords_list = ['']

	def __handle_where_to_save(self):
		'''
		'''
		short_log_name = (self.__log_filename.split('/')[-1]).split('.')[0]
		file_name_to_save_list = [short_log_name, self.__copy_raw_mode]
		[file_name_to_save_list.append(part) for part in self.__keywords_list]
		file_name_to_save = '_'.join(file_name_to_save_list) + '.log'


		test_path_list = os.getcwd().split('\\')
		test_path_list.append('result')
		test_path = '/'.join(test_path_list)
		if not os.path.isdir(test_path):
			os.mkdir(test_path)

		test_path_list.append(file_name_to_save)
		self.__file_to_save = '/'.join(test_path_list)


		if os.path.exists(self.__file_to_save):
			if self.__new:
				with open(self.__file_to_save, 'w') as file:
					pass
				return True
			else:
				return False
		else:
			return True

	def __run(self):
		if not self.__count:
			self.__search_force() if self.__force else self.__search_without_force()
		else:
			if self.__raw_mode == 'user':
				self.__count_users()
			elif self.__raw_mode == 'total':
				if self.__raw_keywords == 'T':
					self.__count_total_T()
				elif self.__raw_keywords == 'F':
					self.__count_total_F()
				else:
					print('TF关键词错误！')
					exit(0)
			else:
				self.__count_force() if self.__force else self.__count_without_force()
		print('搜索记录将保存在：'+ self.__file_to_save)

	def __dont_run(self):
		print('搜索记录已经存在于'+ self.__file_to_save)
		with open(self.__file_to_save, 'r', encoding='utf-8') as result_file:
			while True:
				this_line = result_file.readline()
				if not this_line:
					break
				print(this_line, end='')

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

	def __kmp(self, search, key, nexts):
		i, j = 0, 0
		s_len, k_len = len(search), len(key)
		result = []
		while i < s_len and j <= k_len:
			if search[i] == key[j]:
				i += 1
				j += 1
				if j >= k_len:
					return [i - k_len]
			else:
				if j == 0:
					i += 1
				else:
					j = nexts[j]
		if i == s_len:
			return []

	def __search_kmp(self, search, key_word):
		nexts = self.__next_(key_word)
		res = self.__kmp(search, key_word, nexts)
		return res

	def __file_loader(self):
		msg = '正在读取：' + self.__log_filename
		print(msg)

		self.__log = []
		self.__total_danmu_num = 0
		with open(self.__log_filename, 'r', encoding='utf-8') as log_file:
			while True:
				this_line = log_file.readline()
				if not this_line:
					break
				self.__total_danmu_num += 1

				if this_line[-1] == '\n':
					this_line = this_line[:-1]
				try:
					this_line_to_log = []
					if self.__total_danmu_num == 1:
						self.__start_at = this_line.split('：：')[0]
					self.__end_at = this_line.split('：：')[0]
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

					self.__log.append(this_line_to_log)
				except IndexError:
					pass

		print('文件读取完成！')

	def __search_without_force(self):
		self.__file_loader()

		for keyword in self.__keywords_list:
			if keyword[-1] == '\n':
				keyword = keyword
			for searching in self.__log:
				searching_word = searching[self.__mark][self.__mark_]
				if self.__mark_:
					if searching_word == keyword:
						print(searching[-1])
						with open(self.__file_to_save, 'a', encoding='utf-8') as result_file:
							result_file.write(searching[-1]+'\n')
				else:
					if self.__mark:
						if self.__search_kmp(searching_word, keyword):
							print(searching[-1])
							with open(self.__file_to_save, 'a', encoding='utf-8') as result_file:
								result_file.write(searching[-1]+'\n')
					else:
						if keyword.isdigit():
							print('不支持搜索粉丝牌等级！')
							return 
						
						if keyword.split('-')[0].isdigit():
							fans_level = keyword.split('-')[0]
							length = len(fans_level)
							fans_name = keyword[length+1:]
							if self.__search_kmp(searching_word.split('-')[0], fans_level) and self.__search_kmp(searching_word.split('-')[1], fans_name):
								print(searching[-1])
								with open(self.__file_to_save, 'a', encoding='utf-8') as result_file:
									result_file.write(searching[-1])
						elif self.__search_kmp(searching_word, keyword):
							print(searching[-1])
							with open(self.__file_to_save, 'a', encoding='utf-8') as result_file:
								result_file.write(searching[-1]+'\n')

	def __search_force(self):
		self.__file_loader()

		for keyword in self.__keywords_list:
			if keyword[-1] == '\n':
				keyword = keyword[:-1]
			for searching in self.__log:
				searching_word = searching[self.__mark][self.__mark_]
				if self.__mark_:
					if searching_word == keyword:
						print(searching[-1])
						with open(self.__file_to_save, 'a', encoding='utf-8') as result_file:
							result_file.write(searching[-1]+'\n')
				else:
					if self.__mark:
						if searching_word == keyword:
							print(searching[-1])
							with open(self.__file_to_save, 'a', encoding='utf-8') as result_file:
								result_file.write(searching[-1]+'\n')
					else:
						if keyword.isdigit():
							print('不支持搜索粉丝牌等级！')
							return 
						
						if searching_word == keyword or searching_word.split('-')[1] == keyword:
							print(searching[-1])
							with open(self.__file_to_save, 'a', encoding='utf-8') as result_file:
								result_file.write(searching[-1]+'\n')

	def __count_total_T(self):
		self.__file_loader()
		savefile = self.__file_to_save

		num = 0
		res_id = []
		res_full = []
		with open(savefile, 'a', encoding='utf-8') as savefile__:
			savefile__.write('录制开始于{}\n'.format(self.__start_at))
			savefile__.write('录制结束于{}\n'.format(self.__end_at))
			savefile__.write('==================\n')
		print('录制开始于{}\n'.format(self.__start_at))
		print('录制结束于{}\n'.format(self.__end_at))
		print('==================\n')
		for searching in self.__log:
			user_info = '--'.join(searching[1])
			user_id = searching[1][1]
			if user_id not in res_id:
				res_id.append(user_id)
				num = num + 1
				print('找到第{}个用户：'.format(num) + user_info)
				res_full.append(user_info)
				with open(savefile, 'a', encoding='utf-8') as savefile__:
					msg = '第{}个用户：'.format(num) + user_info + '\n'
					savefile__.write(msg)
			else:
				if user_info not in res_full:
					msg = user_info + '   <--请注意，此用户uid在此前已经出现，可能中途换了马甲//此条不计数'
					res_full.append(user_info)
					print(msg)

					with open(savefile, 'a', encoding='utf-8') as savefile__:
						savefile__.write(msg + '\n')

		with open(savefile, 'a', encoding='utf-8') as savefile__:
			savefile__.write('=========\n')
			savefile__.write('一共有{}条弹幕\n'.format(self.__total_danmu_num))
			savefile__.write('统计结束，一共有{}人\n'.format(num))
		print('=========')
		print('一共有{}条弹幕\n'.format(self.__total_danmu_num))
		print('统计结束，一共有{}人'.format(num))
		print('文件已经保存到：' + savefile)

	def __count_total_F(self):
		self.__file_loader()
		savefile = self.__file_to_save

		num = 0
		res_id = []
		res_full = []
		with open(savefile, 'a', encoding='utf-8') as savefile__:
			savefile__.write('录制开始于{}\n'.format(self.__start_at))
			savefile__.write('录制结束于{}\n'.format(self.__end_at))
			savefile__.write('==================\n')
		for searching in self.__log:
			user_info = '--'.join(searching[1])
			user_id = searching[1][1]
			if user_id not in res_id:
				res_id.append(user_id)
				num = num + 1
				res_full.append(user_info)
				with open(savefile, 'a', encoding='utf-8') as savefile__:
					msg = '第{}个用户：'.format(num) + user_info + '\n'
					savefile__.write(msg)
			else:
				if user_info not in res_full:
					msg = user_info + '   <--请注意，此用户uid在此前已经出现，可能中途换了马甲//此条不计数'
					res_full.append(user_info)

					with open(savefile, 'a', encoding='utf-8') as savefile__:
						savefile__.write(msg + '\n')

		with open(savefile, 'a', encoding='utf-8') as savefile__:
			savefile__.write('=========\n')
			savefile__.write('一共有{}条弹幕\n'.format(self.__total_danmu_num))
			savefile__.write('统计结束，一共有{}人\n'.format(num))

	def __count_users(self, log=None):
		id_name = {}
		id_times = {}
		if log == None:
			self.__file_loader()
			log = self.__log

		res_id = []
		res_full = []
		print('开始统计')
		for searching in log:
			user_id = searching[1][1]
			user_name = searching[1][0]
			user_info = '--'.join(searching[1])
			if user_id not in res_id:
				res_id.append(user_id)
				res_full.append(user_info)
				id_name[user_id] = [user_name]
				id_times[user_id] = 1
			else:
				id_times[user_id] += 1
				if user_info not in res_full:
					res_full.append(user_info)
					id_name[user_id].append(user_name)

		res_times = sorted(id_times.items(), key=lambda x:x[1], reverse=True)
		print('统计结束')

		num = 1
		for id__, times in res_times:
			user_info = '，'.join(id_name[id__]) + '--' + str(id__)
			msg = '第{}名是：'.format(num) + user_info + '发送了{}条弹幕'.format(times)
			print(msg)
			num = num + 1
			with open(self.__file_to_save, 'a', encoding='utf-8') as result_file:
				result_file.write(msg+'\n')

	def __count_force(self):
		self.__file_loader()
		num = 0
		to_count = []

		for keyword in self.__keywords_list:
			if keyword[-1] == '\n':
				keyword = keyword[:-1]
			for searching in self.__log:
				searching_word = searching[self.__mark][self.__mark_]
				if self.__mark_:
					if searching_word == keyword:
						print(searching[-1])
						num += 1
						with open(self.__file_to_save, 'a', encoding='utf-8') as result_file:
							result_file.write(searching[-1]+'\n')
				else:
					if self.__mark:
						if searching_word == keyword:
							if self.__raw_mode == 'danmu':
								to_count.append(searching)
							print(searching[-1])
							num += 1
							with open(self.__file_to_save, 'a', encoding='utf-8') as result_file:
								result_file.write(searching[-1]+'\n')
					else:
						if keyword.isdigit():
							print('不支持统计粉丝牌等级！')
							return 
						
						if searching_word == keyword or searching_word.split('-')[1] == keyword:
							num += 1
							print(searching[-1])
							with open(self.__file_to_save, 'a', encoding='utf-8') as result_file:
								result_file.write(searching[-1]+'\n')
		msg = '一共有{}条相关记录'.format(num)
		with open(self.__file_to_save, 'a', encoding='utf-8') as result_file:
			result_file.write(msg+'\n')
		if self.__raw_mode == 'danmu':
			self.__count_users(to_count)

	def __count_without_force(self):
		self.__file_loader()
		num = 0
		to_count = []
		for keyword in self.__keywords_list:
			if keyword[-1] == '\n':
				keyword = keyword
			for searching in self.__log:
				searching_word = searching[self.__mark][self.__mark_]
				if self.__mark_:
					if searching_word == keyword:
						num += 1
						print(searching[-1])
						with open(self.__file_to_save, 'a', encoding='utf-8') as result_file:
							result_file.write(searching[-1]+'\n')
				else:
					if self.__mark:
						if self.__search_kmp(searching_word, keyword):
							num += 1
							if self.__raw_mode == 'danmu':
								to_count.append(searching)
							print(searching[-1])
							with open(self.__file_to_save, 'a', encoding='utf-8') as result_file:
								result_file.write(searching[-1]+'\n')
					else:
						if keyword.isdigit():
							print('不支持搜索粉丝牌等级！')
							return 
						
						if keyword.split('-')[0].isdigit():
							fans_level = keyword.split('-')[0]
							length = len(fans_level)
							fans_name = keyword[length+1:]
							if self.__search_kmp(searching_word.split('-')[0], fans_level) and self.__search_kmp(searching_word.split('-')[1], fans_name):
								num += 1
								print(searching[-1])
								with open(self.__file_to_save, 'a', encoding='utf-8') as result_file:
									result_file.write(searching[-1])
						elif self.__search_kmp(searching_word, keyword):
							num += 1
							print(searching[-1])
							with open(self.__file_to_save, 'a', encoding='utf-8') as result_file:
								result_file.write(searching[-1]+'\n')

		msg = '一共有{}条相关记录'.format(num)
		with open(self.__file_to_save, 'a', encoding='utf-8') as result_file:
			result_file.write(msg+'\n')
		if self.__raw_mode == 'danmu':
			self.__count_users(to_count)

if __name__ == '__main__':
	try:
		keywords = argv[3]
	except IndexError:
		keywords = ''

	doSearch = SearchFile(filename=argv[1], mode=argv[2], keywords=keywords)	