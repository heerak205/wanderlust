from collections import Counter
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
		inp = input()
		partlist.append(inp)
		i = i + 1
	# print(partlist)
	major = Counter(partlist)
	# print(major)
	adict1 = {}
	adict2 = {}
	adict3 = {}
	adict4 = {}
	for key, value in major.items():
		p = key.split(" ")
		# print(p)
		if len(p) == 2:
			if int(p[0]) == 1 :
				adict1[p[1]] = value
			elif int(p[0]) == 2 :
				adict2[p[1]] = value
			elif int(p[0]) == 3:
				adict3[p[1]] = value
			else:
				adict4[p[1]] = value

	# print(adict1)
	# print(adict2)
	# print(adict3)
	# print(adict4)
	list1 = []
	for key, value in adict1.items():
		list1.append(value)
	for each in adict1:
		if adict1[each] == max(list1):
			print("Highest number of votes for question : Who should be the next Prime Minister? : "+each)
	list2 = []
	if len(adict2) != 0:
		for key, value in adict2.items():
			list2.append(value)
		for each in adict2:
			if adict2[each] == max(list2):
				print("Highest number of votes for question : Who will be the next cm for Telangana? : "+each)
	list3 = []
	if len(adict3) != 0:
		for key, value in adict3.items():
			list3.append(value)
		for each in adict3:
			if adict3[each] == max(list3):
				print("Highest number of votes for question : Who will be the next cm for AP? : "+each)

if __name__ == '__main__':
	main()