def main():
	list2 = input()
	list1 = eval(list2)
	i = 0
	sum = 0
	a = 0
	res = 0
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
								if type(list1[i][j][k]) != str:
									sum = sum + list1[i][j][k][l]
								l = l + 1
						else:
							if type(list1[i][j][k]) != str:
								sum = sum + list1[i][j][k]
						k = k + 1
				else:
					if type(list1[i][j]) != str:
						sum = sum + list1[i][j]
				j = j+1
		else:
			if type(list1[i]) != str:
				sum = sum + list1[i]
		i = i + 1
	print(sum)
	for each in list2:
		if each == '[' or each == ']':
			res = res + 1
	print((res//2)-1)

if __name__ == '__main__':
	main()