from operator import itemgetter
global d
d = {}
global countofrooms
countofrooms = 0
global listt
listt = []
global total
total = 6
def reserve(person):
    global countofrooms
    global d
    global total
    countofrooms += 1
    if countofrooms >= total:
        print("All Rooms are reserved")
        return
    if countofrooms not in d.values():
        d[person] = countofrooms
        listt.append(countofrooms)
        print(person + " " + str(countofrooms))
    else:
        reserve(person)
def reserveN(person, rn):
    global total
    global listt
    if rn in listt:
        print("Room is already resverved")
        return
    for everyroom in sorted(listt):
        if int(rn) == int(everyroom):
            print("All Rooms are reserved")
            return
    for everyroom in d.values():
        if int(rn) == int(everyroom) or rn in listt:
            print("Room is already reserved")
            return
        else:
            if int(rn) >= total:
                ("All Rooms are reserved")
                return
    d[person] = int(rn)
    print(person + " " + str(rn))
def display():
    for key, value in sorted(d.items(), key = itemgetter(1)):
        print(key, value)
def build(extra):
    global total
    total += extra
    print("Added " + str(extra) + " more rooms")
def cancelroom(person):
    global d
    global total
    del d[person]
    print(person+" now has no reservations.")
    total = total - 1
    return
def main():
    n = int(input())
    tokens = []
    for i in range(n):
        tokens = input().split(" ")
        if tokens[0] == "reserve":
            reserve(tokens[1])
        elif tokens[0] == "reserveN":
            reserveN(tokens[1], tokens[2])
        elif tokens[0] == "print":
            display()
        elif tokens[0] == "build":
            build(int(tokens[1]))
        elif tokens[0] == "cancel":
            cancelroom(tokens[1])
main()
