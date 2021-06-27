#chat
import os


#讀取檔案
def read_file(filename):
	data = []
	with open(filename, 'r', encoding = "UTF-8-sig") as f:
		for line in f:
			data.append(line.strip())
	return data


#轉換
def count(data):
	Allen_chat = []
	Viki_chat = []
	Allen_chat_count = 0
	Viki_chat_count = 0
	Allen_stick_count = 0
	Viki_stick_count = 0
	Allen_image_count = 0
	Viki_image_count =0
	for d in data:
		chat = d.split(" ")
		if chat[1] == 'Allen':
			if chat[2] == '貼圖':
				Allen_stick_count +=1
			elif chat[2] == '圖片':
				Allen_image_count +=1		
			else:
				for c in chat[2:]:
					Allen_chat_count += len(c)
		elif chat[1] == 'Viki':
			if chat[2] == '貼圖':
				Viki_stick_count += 1
			elif chat[2] == '圖片':
				Viki_image_count +=1
			else:
				for c in chat[2:]:
					Viki_chat_count += len(c)	
	return Allen_chat_count, Allen_stick_count, Allen_image_count, Viki_chat_count, Viki_stick_count, Viki_image_count


#寫入程式
def write_file(filename, transdata):
	with open(filename, 'w', encoding = "UTF-8") as f:
		for d in transdata:
			f.write(d + '\n')


def main():
	data = read_file('LINE-Viki.txt')
	Allen_chat_count, Allen_stick_count, Allen_image_count, Viki_chat_count, Viki_stick_count, Viki_image_count = count(data)
	print(count(data))
	print('Allen說了', Allen_chat_count, '個字')
	print('Allen傳了', Allen_stick_count, '個貼圖')
	print('Allen傳了', Allen_image_count, '個圖片')
	print('Viki說了', Viki_chat_count, '個字')
	print('Viki傳了', Viki_stick_count, '個貼圖')
	print('Viki傳了', Viki_image_count, '個圖片')
	# write_file('output.txt', transdata)

main()

 



