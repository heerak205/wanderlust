def main():
	list1 = eval(input())
	print(list1)
	p = len(list1)
	print(p)
	i = 0
	sum = 0
	while i < len(list1):
		j = 0
		while j<len(list1[i]):
			if len(str(list1[i][j]))>1:
				k = 0
				while k<len(list1[i][j]):
					if len(str(list1[i][j][k])) > 1:
						print(len(str(list1[i][j][k])))
						l = 0
						while l<len(str(list1[i][j][k][l])):
							sum = sum + int(list1[i][j][k][l])
							l = l + 1
					sum = sum + int(list1[i][j][k])
					k = k + 1

			sum = sum + int(list1[i][j])
			j = j + 1
		i = i + 1

if __name__ == '__main__':
	main()