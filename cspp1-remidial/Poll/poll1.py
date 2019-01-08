def main():
	a = int(input())
	b = a*5
	queslist = []
	quesdict = {}
	for i in range(0, b):
		c = input()
		queslist.append(c)
	# print(queslist)
	newqueslist = []
	i = 0
	while i<len(queslist):
		newlist1 = []
		for j in range(i, i+5):
			newlist1.append(queslist[j])
		newqueslist.append(newlist1)
		i = i + 5
	# print(newqueslist)
	queslist1 = newqueslist
	i = 0
	d = 1
	while i<len(newqueslist):
		quesdict[d] = newqueslist[i]
		d = d + 1
		i = i + 1
	# print(quesdict)
	adict = {}
	noofpart = int(input())
	# print(noofpart)
	totpart = noofpart*(a+1)
	# print(totpart)
	i = 0
	partlist = []
	while i<totpart:
		inp = input().split(" ")
		if len(inp) == 2:
			partlist.append(inp)
		i = i + 1
	# print(partlist)
	for each in partlist:
		if int(each[0]) not in adict:
			adict[int(each[0])] = each[1]
		else:
			if adict.get(int(each[0])) == each[1]:
				adict[int(each[0])] = each[1]
	# print(adict)
	for each in adict:
		print(("Highest number of votes for question : Who should be the next Prime Minister? : ")+ adict[each])


if __name__ == '__main__':
	main()