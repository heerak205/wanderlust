def two_pair(hand):
	k = []
	for c,s in hand:
		k += c
	l = list(set(k))
	if len(l) == 3:
		if k.count(l[0]) == 2 and k.count(l[1]) == 2:
			return True
		elif k.count(l[0]) == 2 and k.count(l[2]) == 2:
			return True
		elif k.count(l[1]) == 2 and k.count(l[2]) == 2:
			return True
	else:
		return False