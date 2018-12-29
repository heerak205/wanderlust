def main():
	html = list(open("webpage5.html").read().replace(" ", "").replace("\n", ""))
	# print(html)
	image(html)
	# background(html)

def image(arg):
	i = 0
	count = 0
	while(i<len(arg)-1):
		if arg[i] == "<" and arg[i+1] == "i" and arg[i+2] == "m":
			while(True):
				if arg[i] == "c" and arg[i+1] == "=" and arg[i+2] == '"':
					break
				i = i+1
			i = i+3
			res = ""
			# count = 0
			while(arg[i] != '"'):
				res = res + arg[i]
				i = i+1
			print(res)
			count = count + 1
		i = i + 1
	print(count)

def background(arg):
	i = 0
	while(i<len(arg)-1):
		if arg[i] == "-" and arg[i+1] == "c" and arg[i+2] == "o" and arg[i+3] == "l":
			while(True):
				if arg[i] == ":":
					break
				i = i+1
			i = i+1
			res = ""
			while(arg[i] != ';'):
				res= res + arg[i]
				i = i+1
			print(res)

if __name__ == '__main__':
	main()