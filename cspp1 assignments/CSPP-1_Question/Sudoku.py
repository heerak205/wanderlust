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
	p = getRowValues(sudoku)
	for i in range(9):
		if len(set(p[i])) != 9:
			raise Exception("Invalid input")
	q = getColumnValues(p)
	for i in range(9):
		if len(set(q[i])) != 9:
			raise Exception("Invalid input")
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
		list3.append(r[i])
	#print(list4)
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
	#print(list2)
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


		

"""
This method should collect all the available values present for a "."
You should get the values present in row,column,grid.
Then you should return the values that doesnot exist in the previous values.
"""
def possibleValues():
	pass
	
"""
Read the input and store the values in an appropriate data sturcture.
Then travese through each value, if you get a "." then collect the possible values

"""


def main():
	q = list(input())
	r = getRowValues(q)
	getColumnValues(r)
	try:
		validateSudoku(q)
	except Exception as e:
		print(e)
	getGridValues(r)

if __name__ == "__main__":
    main()