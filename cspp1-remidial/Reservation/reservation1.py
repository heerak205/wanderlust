def main():
	n = int(input())
	i = 0
	hotdict = {}
	# p = len(hotdict)
	# print(p)
	roomno = 1
	roomlist = []
	staticlist = [1, 2, 3, 4, 5]
	while i<=n:
		b = input().split(" ")
		if len(b) == 2:
			if roomno>5:
				print("All rooms are reserved")
			# elif roomno not in hotdict.keys():
			# 	hotdict.update({roomno:b[1]})
			# 	print(hotdict[roomno] + " " + str(roomno))
			else:
				m = roomno - 1
				n = roomno + 1
				if m not in hotdict.keys():
					hotdict.update({m:b[1]}) 
					print(hotdict[m] + " " + str(m))
				elif m+1 not in hotdict.keys():
					hotdict.update({m+1:b[1]})
					print(hotdict[m+1] + " " + str(m+1))
				elif n not in hotdict.keys():
					hotdict.update({n:b[1]})
					print(hotdict[n] + " " + str(n))
				else:
					print("Room is already reserved")
		if len(b) == 3:
			if roomno>5:
				print("All rooms are reserved")
			elif int(b[2]) not in hotdict.keys():
				roomlist.append(int(b[2]))
				hotdict.update({int(b[2]):b[1]})
				print(hotdict[int(b[2])] + " " + str(b[2]))
			else:
				print("Room is already reserved")
		if len(b) == 1:
			p = sorted(hotdict)
			for each in p:
				print(hotdict[each] + " " + str(each))

		roomlist.append(roomno)
		i = i + 1
		roomno = roomno + 1

if __name__ == '__main__':
	main()