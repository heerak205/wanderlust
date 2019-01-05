def main():
	p = input()
	inp = eval(p)
	global sum
	sum = 0
	global res
	res = 0
	print(sumofnum(inp))
	print(numoflists(p))



def sumofnum(arg):
	global sum
	for each in arg:
		if type(each) == list:
			sumofnum(each)
		else:
			if type(each) != str:
				sum = sum + each
	return sum

def numoflists(p):
	global res
	for each in p:
		if each == '[' or each == ']':
			res = res + 1
	return ((res//2)-1)

if __name__ == '__main__':
	main()

