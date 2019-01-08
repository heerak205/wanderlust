def main():
	a = int(input())
	b = a*5
	i = 0
	global votedict
	votedict = {}
	global queslist
	queslist = []
	while i<b:
		inp = input()
		queslist.append(inp)
		i = i + 1

	voters = int(input())
	c = voters*(a+1)
	j = 0
	global voterlist
	voterlist = []
	while j<c:
		d = input().split(" ")
		voterlist.append(d)
		j = j + 1
	# print(queslist)
	# print(voterlist)
	print(voterdict(voterlist))

def voterdict(lis):
	global votedict
	for each in lis:
		if len(each) == 2:
			if each[1] not in votedict:
				votedict[each[1]] = int(each[0])
			else:
				votedict[each[1]] = votedict.get(each[1]) + int(each[0])
	return votedict

if __name__ == '__main__':
	main()

