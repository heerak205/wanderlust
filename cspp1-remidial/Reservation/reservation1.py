def main():
	n = int(input())
	i = 0
	hotdict = {}
	roomno = 1
	while i<n:
		# print(i)
		b = input().split(" ")
		if len(b) == 2:
			if roomno>5:
				print("All Rooms are reserved")
			elif roomno not in hotdict.keys():
				hotdict.update({roomno:b[1]})
				print(hotdict[roomno] + " " + str(roomno))
			else:
				for m in range(1, 6):
					if m not in hotdict.keys():
						hotdict.update({m:b[1]})
						print(hotdict[m] + " " + str(m))
						break
				# print("Room is already reserved")
		if len(b) == 3:
			if roomno>5:
				print("All rooms are reserved")
			elif int(b[2]) not in hotdict.keys():
				hotdict.update({int(b[2]):b[1]})
				print(hotdict[int(b[2])] + " " + str(b[2]))
			else:
				print("Room is already reserved")
		if len(b) == 1:
			p = sorted(hotdict)
			for each in p:
				print(hotdict[each] + " " + str(each))
		i = i + 1
		roomno= roomno+1

if __name__ == '__main__':
	main()