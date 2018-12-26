"""
In this method :
 * Check there are only 81 values
 * iterate through each row in the sudoku and if you find any duplicate values
 	raise an exception
 * iterate through each column in the sudoku and if you find any duplicate values
	raise an exception
 * iterate through each subgrid(3x3) in the sudoku and if you find any duplicate values
	raise an exception
"""
def validateSudoku(sudoku):
	if len(sudoku) != 81:
		raise Exception("Invalid input")
	elif '.' not in sudoku:
		raise Exception("Given sudoku is solved")
	p = getRowValues(sudoku)
	for i in range(9):
		# print(i)
		# print("length")
		if '.' in p[i]:
			r = p[i].remove('.')

		else:
			r = p[i]
		s = set(r)
		if len(r) != len(s):
			raise Exception("Invalid Sudoku:Duplicate values")
	q = getColumnValues(p)
	for i in range(9):
		if '.' in q[i]:
			r = q[i].remove('.')
		else:
			r = q[i]
		s = set(r)
		if len(r) != len(s):
			raise Exception("Invalid Sudoku:Duplicate values")
	
	# for i in range(9):
	# 	if len(set(p[i])) != 9:
	# 		raise Exception("Invalid input")
	# q = getColumnValues(p)
	# for i in range(9):
	# 	if len(set(q[i])) != 9:
	# 		raise Exception("Invalid input")
"""
This  method should retunn all the values present in the ith row
"""
def getRowValues(r):
	# n = 9
	# #print("HI")
	# for i in range(0, len(r), n):
	# 	yield r[i:i+n]
	# return r
	list3 = []
	list4 = []
	for i in range(82):
		if(i == 81):
			list4.append(list3)
			break
		if(i%9 == 0 and i != 0):
			list4.append(list3)
			list3 = []
		# print(i)
		list3.append(r[i])
	# print(list4)
	return list4

"""
This  method should retunn all the values present in the ith column
"""
def getColumnValues(q):
	list1 = []
	list2 = []
	for i in range (9):
		for j in range(9):
			list1.append(q[j][i])
		list2.append(list1)
		list1 = []
	# print(list2)
	return list2

"""
This  method should retunn all the values present in the i,j th subgrid
"""
def getGridValues(s):
	#c = getRowValues(s)
	#d = getColumnValues(c)
	list5 = []
	list6 = []
	for i in range(3):
		for j in range(3):
			list5.append(s[i][j])
	list6.append(list5)
	list5 = []
	for i in range(3):
		for j in range(3,6):
			list5.append(s[i][j])
	list6.append(list5)
	list5 = []
	for i in range(3):
		for j in range(6,9):
			list5.append(s[i][j])
	list6.append(list5)
	#print(list6)
	list5 = []
	for i in range(3,6):
		for j in range (3):
			list5.append(s[i][j])
	list6.append(list5)
	list5 = []
	for i in range(3,6):
		for j in range(3,6):
			list5.append(s[i][j])
	list6.append(list5)
	list5 = []
	for i in range(3,6):
		for j in range(6,9):
			list5.append(s[i][j])
	list6.append(list5)
	list5 = []
	for i in range(6,9):
		for j in range(3):
			list5.append(s[i][j])
	list6.append(list5)
	list5 = []
	for i in range(6,9):
		for j in range(3,6):
			list5.append(s[i][j])
	list6.append(list5)
	list5 = []
	for i in range(6,9):
		for j in range(6,9):
			list5.append(s[i][j])
	list6.append(list5)
	return list6
	#print(list6)
def gaetparticulatgrid(i, j, list6):
	#particulargrid = []
	if (i >= 0 and i < 3) and (j >= 0 and j < 3):
		return list6[0]
	if (i >= 0 and i < 3) and (j >= 3 and j < 6):
		return list6[1]
	if (i >= 0 and i < 3) and (j >= 6 and j < 9):
		return list6[2]
	if (i >= 3 and i < 6) and (j >= 0 and j < 3):
		return list6[3]
	if (i >= 3 and i < 6) and (j >= 3 and j < 6):
		return list6[4]
	if (i >= 3 and i < 6) and (j >= 6 and j < 9):
		return list6[5]
	if (i >= 6 and i < 9) and (j >= 0 and j < 3):
		return list6[6]
	if (i >= 6 and i < 9) and (j >= 3 and j < 6):
		return list6[7]
	if (i >= 6 and i < 9) and (j >= 6 and j < 9):
		return list6[8]
"""
This method should collect all the available values present for a "."
You should get the values present in row,column,grid.
Then you should return the values that doesnot exist in the previous values.
"""
def possibleValues(r, s, t):
	# print(r)
	# print(s)
	# print(t)
	for row in range(len(r)):
		for each in range(len(r)):
			if r[row][each] == ".":
				eachrow = converttoint(r[row])
				eachcol = converttoint(s[each])
				subgrid1 = converttoint(getparticulatgrid(row, each, getGridValues(r)))
				# print(eachrow)
				# print(eachcol)
				# print(subgrid1)
				possibilities(eachrow, eachcol, subgrid1)
def possibilities(eachrow, eachcol, subgrid1):
	list7 = [1,2,3,4,5,6,7,8,9]
	list8 = []
	for no in list7:
		if no not in eachrow:
			if no not in eachcol:
		 		if no not in subgrid1:
		 			list8.append(no)
	str1 = ""
	str1 = list(map(str, list8))
	str1 = ''.join(str1)
	print(str1)


	

"""
Read the input and store the values in an appropriate data sturcture.
Then travese through each value, if you get a "." then collect the possible values
	
"""
def converttoint(strlist):
	intlist = ''.join(strlist)
	intlist = intlist.replace(".", "")
	intlist = list(intlist)
	inti = list(map(int, intlist))
	return inti

def main():
	q = list(input())
	# print(len(q))

	r = getRowValues(q)
	# print(r)
	s = getColumnValues(r)
	# print(s)
	try:
		validateSudoku(q)
		t = getGridValues(r)
		possibleValues(r, s, t)
	except Exception as e:
		print(e)
	# print(t)

if __name__ == "__main__":
    main()