def main():
	n = int(input())
	i = 0
	hotdict = {}
	roomno = 1
	limit = 5
	while i<n:
		# print(i)
		b = input().split(" ")
		if len(b) == 2:
			if b[0] == 'reserve':
				if roomno > limit:
					print("All Rooms are reserved")
				elif roomno not in hotdict.keys():
					hotdict.update({roomno:b[1]})
					print(hotdict[roomno] + " " + str(roomno))
					roomno = roomno + 1
				else:
					for m in range(1, limit+1):
						if m not in hotdict.keys():
							hotdict.update({m:b[1]})
							print(hotdict[m] + " " + str(m))
							roomno = roomno + 1
							break
			if b[0] == "build":
				limit = limit + int(b[1])
				print("Added" + " " + b[1] + " " + "more rooms")
			if b[0] == "cancel":
				print(b[1] + " now has no reservations")
				p = hotdict.keys(b[1])
				del hotdict[p]

				# print("Room is already reserved")
		if len(b) == 3:
			if roomno > limit:
				print("All Rooms are reserved")
			elif int(b[2]) not in hotdict.keys():
				hotdict.update({int(b[2]):b[1]})
				print(hotdict[int(b[2])] + " " + str(b[2]))
				roomno = roomno + 1
			else:
				print("Room is already reserved")
		if len(b) == 1:
			p = sorted(hotdict)
			for each in p:
				print(hotdict[each] + " " + str(each))
		i = i + 1

if __name__ == '__main__':
	main()