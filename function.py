from itertools import product
import multiprocessing

class MainFunctions(object):
	def read_dict(self, path):
		with open(path,"r") as f:
			data = f.read()
			return data

	def Dictionary_Generator_3(self, one_Content, two_Content, three_Content, file_name):
		try:
			tmp_lists = []
			tmp_lists.clear()
			fileName = str(file_name)+".txt"
			times = 0
			for i in product(one_Content, two_Content, three_Content):
				tmp_i = i[0]+i[1]+i[2]+"\n"
				tmp_lists.append(tmp_i)
				times += 1
				# 清理内存
				if(times == 50000000):
					with open(fileName, mode="a", encoding="UTF-8") as f:
						f.writelines(tmp_lists)
						times = 0
						tmp_lists.clear()
			with open(fileName, mode="a", encoding="UTF-8") as f:
				f.writelines(tmp_lists)
		except Exception as e:
			print(e)

	def Dictionary_Generator_2(self, one_Content, two_Content, file_name):
		try:
			tmp_lists = []
			tmp_lists.clear()
			fileName = str(file_name)+".txt"
			times = 0
			for i in product(one_Content, two_Content):
				tmp_i = i[0]+i[1]+"\n"
				tmp_lists.append(tmp_i)
				times += 1
				# 清理内存
				if(times == 50000000):
					with open(fileName, mode="a", encoding="UTF-8") as f:
						f.writelines(tmp_lists)
						times = 0
						tmp_lists.clear()
			with open(fileName, mode="a", encoding="UTF-8") as f:
				f.writelines(tmp_lists)
		except Exception as e:
			print(e)

	def Dictionary_Generator_add(self, file_name):
		add_pwds = self.read_dict(".\\db\\weak_pwds.txt")
		fileName = str(file_name)+".txt"
		with open(fileName, mode="a", encoding="UTF-8") as f:
			for i in add_pwds:
				f.write(i)

	def select_method(self, A_Content, B_Content, C_Content, key, file_name):
		try:
			key = str(key)
			if(key[0] == "1"):
				option_D = multiprocessing.Process(target=self.Dictionary_Generator_3, args=(A_Content, C_Content, B_Content, file_name))
				option_D.start()
				option_D.join()
				self.Dictionary_Generator_add(file_name)

			if(key[1] == "1"):
				option_C = multiprocessing.Process(target=self.Dictionary_Generator_3, args=(A_Content, B_Content, C_Content, file_name))
				option_C.start()
				option_C.join()
				self.Dictionary_Generator_add(file_name)

			if(key[2] == "1"):
				option_B = multiprocessing.Process(target=self.Dictionary_Generator_2, args=(A_Content, C_Content, file_name))
				option_B.start()
				option_B.join()
				self.Dictionary_Generator_add(file_name)

			if(key[3] == "1"):
				option_A = multiprocessing.Process(target=self.Dictionary_Generator_2, args=(A_Content, B_Content, file_name))
				option_A.start()
				option_A.join()
				self.Dictionary_Generator_add(file_name)

		except Exception as e:
			print(e)


if __name__ == "__main__":
	pass



