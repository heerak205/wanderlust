def main():
	list2 = input()
	list1 = eval(list2)
	i = 0
	sum = 0
	res = 0
	if len(list1) == 1:
		print(0)
	else:
		while i<len(list1):
			if type(list1[i]) == list:
				j = 0
				while j<len(list1[i]):
					if type(list1[i][j]) == list:
						k = 0
						print(list1[i][j])
						while k<len(list1[i][j]):
							if type(list1[i][j][k]) == list:
								l = 0
								print(list1[i][j][k])
								while l<len(list1[i][j][k]):
									if type(list1[i][j][k][l]) == list:
										m = 0
										print(list1[i][j][k][l])
										if type(list1[i][j][k][l][m]) == int:
												sum = sum + list1[i][j][k][l][m]
												break
										else:
											while m<len(list1[i][j][k][l]):
												if type(list1[i][j][k][l][m]) == list:
													n = 0
													print(list1[i][j][k][l][m])
													while n<len(list1[i][j][k][l][m]):
														if type(list1[i][j][k][l][m][n]) == list:
															o = 0
															while o<len(list1[i][j][k][l][m][n]):
																if type(list1[i][j][k][l][m][n][o]) == list:
																	p = 0
																	while p<len(list1[i][j][k][l][m][n][o]):
																		sum = sum + list1[i][j][k][l][m][n][o][p]
																		# print(list1[i][j][k][l][m][n][o][p])
																		p = p + 1
																else:
																	sum = sum + list1[i][j][k][l][m][n][o]
																o = o + 1
														# print(list1[i][j][k][l][m][n])
														if type(list1[i][j][k][l][m][n]) != str:
															sum = sum + list1[i][j][k][l][m][n]
														n = n + 1
											# print(list1[i][j][k][l][m])
											if type(list1[i][j][k][l][m]) != str:
												sum = sum + list1[i][j][k][l][m]
											m = m + 1
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