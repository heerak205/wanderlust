def main():
	a = int(input())
	i= 0
	count = 0
	countlist = []
	# countlist1 = []
	while i < a:
		# count = count + 1
		b = input().split(" ")
		if len(b) == 2:
			count = count + 1
			reserve(b[1], count, countlist)
			countlist.append(count)
		if len(b) == 3:
			reserveN(b[1], b[2], countlist)
			countlist.append(b[2])
		i = i + 1
		

rumno = ['1', '2', '3', '4', '5']
def reserve(name, count, countlist):
	if count in countlist :
		print("Room is already reserved")
	elif len(countlist) == len(rumno) :
		print("All rooms are reserved")
	else:
		print(name + " " + str(count))


def reserveN(name, roomno, countlist):
	if roomno in countlist:
		print("Room is already reserved")
	else:
		print(name + " " + str(roomno))

if __name__ == '__main__':
	main()


