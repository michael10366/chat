#chat3

def read_file(filename):
	data = []
	with open(filename, 'r', encoding = 'UTF-8-sig')as f:
		for line in f:
			data.append(line.strip().split(" "))
		return data


def convert(data):
	word = []
	for d in data:
		time = d[0][:5]
		name = d[0][5:]
		chat = d[1:]
		print(time, name, chat)

	return word


def write_file(filename, word):
	with open(filename, 'w', encoding = 'UTF-8-sig') as f:
		for k in word:
			f.write(k + '\n')


def main():
	data = read_file('3.txt')
	word = convert(data)
	print(word)
	write_file('output3.txt', word)


main()

