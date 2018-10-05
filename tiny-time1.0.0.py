import os
import sys
import os.path
import tinify

tinify.key = '13IJ0rVnu6qHdZICv2WBEAFfKHdFQMRy'
save_path = 'E:/python_dump'


class tinyTime(object):
	"""convertor for CD website images"""
	def __init__(self, arg):
		super (tinyTime, self).__init__()
		self.arg = arg

		return

	def compressFile(inputURL):
		print("compress_file-------------------------------------")
		filename = inputURL.split('/')[-1].strip()
		url = inputURL
		print(url)
		print("Getting:" + filename)
		complete_file = os.path.join(save_path, filename)
		source = tinify.from_url(url)
		print("---almost there---")
		source.to_file(complete_file)
		print("---Success?---")
		return

with open('images_all.txt') as f:
	lines = f.readlines()
	my_list = list(lines)
	url_list = my_list


#loop through the list and define
#len(my_list) replace 2 below 
for i in range(0, 2):
	print('...')
	print('...Found something...')
	url_raw = url_list[i]
	inputURL = url_raw
	print('...')
	print(my_list.index(url_list[i]))
#	print(inputURL)

	tinyTime.compressFile(inputURL)	


