#chat
import os


#讀取檔案
def read_file(filename):
	data = []
	with open(filename, 'r', encoding = "UTF-8") as f:
		for line in f:
			data.append(line.strip())
		print(data)
	return data

#轉換
def transform(data):
	name1 = 'Allen'
	name2 = 'Tom'
	transdata = []
	for d in data:
		if name1 in d:
			person = name1
			continue
		if name2 in d:
			person = name2
			continue
		transdata.append(person + ": " + d)
	return transdata

#寫入程式
def write_file(filename, transdata):
	with open(filename, 'w', encoding = "UTF-8") as f:
		for d in transdata:
			f.write(d + '\n')

def main():
	data = read_file('input.txt')
	transdata = transform(data)
	write_file('output.txt', transdata)

main()

