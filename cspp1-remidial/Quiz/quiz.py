def main():
	a = input().split(" ")
	# print(a)
	numofques = int(a[1])
	global answerdict
	answerdict = {}
	global optionslist
	optionslist = []
	for i in range(numofques):
		# print("hello", i)
		markslist = []
		b = input().split(":")
		# print(b)
		markslist.append(int(b[3]))
		# print(markslist)
		# print(b[4])
		markslist.append(int(b[4]))
		answerdict[int(b[2])] = markslist
	# print(answerdict)
	c = input().split(" ")
	numofquiz = int(c[1])
	global answerlist
	answerlist = []
	for i in range(numofquiz):
		d = input().split(" ")
		e = optionslist.append(int(d[1]))
	f = optionslist
	i = 0
	keyslist = []
	for key, value in answerdict.items():
		keyslist.append(key)
	global wronglist
	wronglist = []
	global rightlist
	rightlist = []
	scorelist = []
	while i< 4:
		if optionslist[i] == keyslist[i]:
			# printer("question text 1")
			rightlist.append("Correct Answer! - Marks Awarded: "+ str(answerdict[optionslist[i]][0]))
			scorelist.append(answerdict[optionslist[i]][0])
		else:
			rightlist.append("Wrong Answer! - Penalty: "+ str(answerdict[optionslist[i]][1]))
			scorelist.append(answerdict[optionslist[i]][1])
		i = i + 1
	global choice
	choice = "choice 1 choice 2	choice 3 choice 4"
	b = input()
	# print(rightlist)
	# print(wronglist)
	print("|----------------|")
	print("| Load Questions |")
	print("|----------------|")
	print("4 are added to the quiz")
	print("|------------|")
	print("| Start Quiz |")
	print("|------------|")
	print("question text 1(1)")
	print(choice)
	print(" ")
	print("question text 2(2)")
	print(choice)
	print(" ")
	print("question text 3(3)")
	print(choice)
	print(" ")
	print("question text 4(4)")
	print(choice)
	print(" ")
	print("|--------------|")
	print("| Score Report |")
	print("|--------------|")
	print("question text 1")
	print(" "+ rightlist[0])
	print("question text 2")
	print(" "+ rightlist[1])
	print("question text 3")
	print(" "+ rightlist[2])
	print("question text 4")
	print(" "+ rightlist[3])
	sum = 0
	i = 0
	# print(scorelist)
	while i<len(scorelist):
		sum = sum+scorelist[i]
		i = i + 1
	print("Total Score: "+str(sum))	




if __name__ == '__main__':
	main()
