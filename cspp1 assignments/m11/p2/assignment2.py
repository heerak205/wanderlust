"""#Exercise: Assignment-2
#Implement the updateHand function
"""
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 
    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.
    Has no side effects: does not modify hand.
    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    a_dict = {}
    for var_j in word:
        if var_j in hand:
            a_dict[var_j] = hand[var_j]-1
    return a_dict
def main():
    """
    main function called.
    """
    input_n = input()
    a_dict = {}
    for _ in range(int(input_n)):
        var_data = input()
        l_l = var_data.split()
        a_dict[l_l[0]] = int(l_l[1])
    var_data1 = input()
    print(updateHand(a_dict, var_data1))
if __name__ == "__main__":
    main()
