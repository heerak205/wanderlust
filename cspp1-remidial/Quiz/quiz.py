def main():
	Flag = True
	a = input().split(" ")
	# print(a)
	numofques = int(a[1])
	global answerdict
	answerdict = {}
	global optionslist
	optionslist = []
	print("|----------------|")
	print("| Load Questions |")
	print("|----------------|")
	for i in range(numofques):
		# print("hello", i)
		markslist = []
		b = input().split(":")
		try:
			if(b[4] == ""):
				raise Exception("Error! Malformed question")
		# except Exception as e:
		# 		Flag=False
		# 		print(e)
			# print(b)
			markslist.append(int(b[3]))
			# print(markslist)
			# print(b[4])
			markslist.append(int(b[4]))
			answerdict[int(b[2])] = markslist
		except Exception as e:
			Flag=False
			print(e)
	# print(answerdict)
	c = input().split(" ")
	numofquiz = int(c[1])
	global answerlist
	answerlist = []
	for i in range(numofquiz):
		inp = input().split(" ")
		e = optionslist.append(int(inp[1]))
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
	if Flag == True:
		while i< numofques:
			if optionslist[i] == keyslist[i]:
				# printer("question text 1")
				rightlist.append("Correct Answer! - Marks Awarded: "+ str(answerdict[keyslist[i]][0]))
				scorelist.append(answerdict[keyslist[i]][0])
			else:
				rightlist.append("Wrong Answer! - Penalty: "+ str(answerdict[keyslist[i]][1]))
				scorelist.append(answerdict[keyslist[i]][1])
			i = i + 1
	global choice
	choice = "choice 1	choice 2	choice 3	choice 4"
	b = input()
	# print(rightlist)
	# print(wronglist)
	questextlist = ["question text 1(1)", "question text 2(2)", "question text 3(3)", "question text 4(4)"]
	questextlist2 = ["question a(1)", "question b(2)", "question c(3)", "question d(4)", "question e(1)", "question f(2)", "question g(3)", "question h(4)", "question i(1)", "question j(2)"]
	choice1 = "choice a    choice b    choice c    choice d"
	# print("|----------------|")
	# print("| Load Questions |")
	# print("|----------------|")
	if(Flag):
		print(str(numofques)+" are added to the quiz")
	print("|------------|")
	print("| Start Quiz |")
	print("|------------|")
	if Flag == True:
		if numofques<5:
			i = 0
			while i < numofques:
				print(questextlist[i])
				print(choice + "\n")
				i = i + 1
				# if i<numofques:
					# print("\n")
		else:
			i = 0
			while i < numofques:
				print(questextlist2[i])
				print(choice1 + "\n")
				i = i + 1
				# if i<numofques:
					# print("\n")

	questextlist1 = ["question text 1", "question text 2", "question text 3", "question text 4"]
	questextlist3 = ["question a", "question b", "question c", "question d", "question e", "question f", "question g", "question h", "question i", "question j"]
	print("|--------------|")
	print("| Score Report |")
	print("|--------------|")
	i = 0
	if Flag == True:
		if numofques<5:
			while i<numofques:
				print(questextlist1[i])
				print(" "+ rightlist[i])
				i = i + 1
		else:
			while i < numofques:
				print(questextlist3[i])
				print(" "+ rightlist[i])
				i = i + 1
		sum = 0
		i = 0
		# print(scorelist)
		while i<len(scorelist):
			sum = sum+scorelist[i]
			i = i + 1
		print("Total Score: "+str(sum))
if __name__ == '__main__':
	main()
