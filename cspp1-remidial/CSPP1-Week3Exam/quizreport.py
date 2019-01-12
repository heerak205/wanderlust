def main():
	numofques = int(input())
	i = 0
	queslist = []
	studid = []
	while i < numofques:
		resp = input().split("|")
		if resp[0] not in studid:
			studid.append(resp[0])
		queslist.append(resp)
		i = i + 1
	totmrk = 0
	studict = {}
	i = 0
	while i < len(studid):
		j = 0
		totmrk = 0
		sum = 0
		while j < len(queslist):
			if int(studid[i]) == int(queslist[j][0]):
				totmrk = totmrk + int(queslist[j][4])
				if queslist[j][2] == queslist[j][3]:
					sum = sum + int(queslist[j][4])
				else:
					sum = sum - int(queslist[j][4])
			j = j + 1
		templist = 0
		if sum<0:
			aggregate = 0.0
		else:
			aggregate = float(round((sum/totmrk)*100))
		templist = templist + aggregate
		studict[int(studid[i])] = templist
		i = i + 1

	prinfin(studict)

def prinfin(studict):
	templist = []
	for each in studict:
		templist.append(each)
	p = sorted(templist)
	# print(templist)
	# print(p)
	for each in p:
		print(str(each) + ": " + str(studict[each]) + "%")


if __name__ == '__main__':
	main()