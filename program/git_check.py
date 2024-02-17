# python 3.12.2 
# "请在充分理解本程序后再使用。\n 本程序使用带来的影响由操作者自行承担。"
import os

def text_check(file_path, file_name):
	'''
		文本标点符号检查
	'''

	# 测试文本保留
	if file_name == "backup.txt":
		print("\t", file_name, "系统默认设置跳过")
		return

	# 使用 open() 函数以只读模式打开我们的文本文件
	with open(file_path, 'r',encoding='UTF-8') as file:
		# with 保证在语法结束后文件被关闭

		# 使用 read() 函数读取文件内容并将它们存储在一个新变量中
		data = file.read()

		# 使用 replace() 函数搜索和替换文本
		data = data.replace('，', ',')
		data = data.replace('；', ';')
		data = data.replace('。', '.')
		data = data.replace(r'.$', r'.\ $')
		data = data.replace(r',$', r',\ $')

	# 以只写模式打开我们的文本文件以写入替换的内容
	with open(file_path, 'w',encoding='UTF-8') as file:

		# 在我们的文本文件中写入替换的数据
		file.write(data)
	
	print("\t", file_name, "文本规范已检查和修改")




# 主程序
if __name__ == '__main__':
	# 确认选项：
	print("请在充分理解本程序后再使用。\n本程序使用带来的影响由操作者自行承担。\n同意请输入y或Y,或输入其他字符结束本程序：")
	jud = input()
	if jud != 'y' and jud != 'Y':
		print("程序未正常运行！")
		os._exit(0)
	# 获取当前路径
	base_path = os.path.dirname(os.path.realpath(__file__))
	print("\n当前文件夹：", base_path)

	# 获取当前路径下所有的文件名
	filedir = os.listdir(base_path)

	print("批处理文件：\n", filedir, '\n')
	# print('.py' in filedir[0])

	# 文本规范检查(txt, tex)
	print('文本规范检查(txt, tex):\n')
	for file_name in filedir:
		# 文本替换
		if ".txt" in file_name or ".tex" in file_name:
			file_path = os.path.join(base_path, file_name)
			text_check(file_path, file_name)

	# tex编译文件删除项	
	print('\ntex编译文件删除:')
	# 需要删去的文件类型
	keywords = ['.pdf', 'synctex.gz', '.aux', '.log',]
	print(keywords, "\n")
	
	# 计数
	i = 0
	for file_name in filedir:
		# 检查每一个文件是否是keywords指定的类型
		if any(j in file_name and j for j in keywords) == True:
			file_path = os.path.join(base_path, file_name)
			os.remove(file_path)
			print("\t", file_name, '已删除')
			i = i + 1
	
	if i == 0:
		print("\t没有需要删除的文件:(\n")
		print("程序执行结束\n")
	else:
		print("\n程序执行结束\n")
	