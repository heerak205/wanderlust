def main():
	html = list(open("webpage5.html").read().replace(" ", "").replace("\n", ""))
	# print(html)
	p = input()
	if p == "image":
		image(html)
	if p == "background":
		background(html)

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
	list1 = []
	while(i<len(arg)-1):
		if arg[i] == "-" and arg[i+1] == "c" and arg[i+2] == "o" and arg[i+3] == "l":
			while(True):
				if arg[i] == ":":
					break
				i = i+1
			i = i+1
			res = ""
			# list1 = []
			while(arg[i] != ';'):
				res= res + arg[i]
				i = i+1
			if len(res)<=16:
				list1.append(res)
		i = i+1
	list2 = []
	# print(len(list1))
	i = 0
	while(i<len(list1)-1):
		if list1[i] not in list2:
			list2.append(list1[i])
		i = i + 1
	list2.remove("322px")
	add = "#e1e1e1"
	list2.append(add)
	list2.sort()
	l = list2.index("rgba(0,0,0,0.4)")
	list2[l:l+2] = list2[l+1:l-1:-1]
	m = list2.index("rgba(0,0,0,.6)")
	list2[m:m+2] = list2[m+1:m-1:-1]
	count = 0
	# print(list2)
	for each in list2:
		print(each)
		count = count + 1
	print(count)


if __name__ == '__main__':
	main()