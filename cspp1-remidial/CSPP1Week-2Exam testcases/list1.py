def main():
	list2 = input()
	list1 = eval(list2)
	i = 0
	sum = 0
	while i<len(list1):
		if type(list1[i]) == list:
			j = 0
			while j<len(list1[i]):
				if type(list1[i][j]) == list:
					k = 0
					while k<len(list1[i][j]):
						if type(list1[i][j][k]) == list:
							l = 0
							while l<len(list1[i][j][k]):
								sum = sum + list1[i][j][k][l]
								l = l + 1
						else:
							sum = sum + list1[i][j][k]
						k = k + 1
				else:
					sum = sum + list1[i][j]
				j = j+1
		else:
			sum = sum + list1[i]
		i = i + 1
	print(sum)
	a = 0
	res = 0
	while a<len(list2):
		for each in list2:
			if each == '[' or each == ']':
				res = res + 1
	b = (res//2) - 1
	print(b)

if __name__ == '__main__':
	main()