"""
#Exercise: Assignment-4
#We are now ready to begin writing the code that interacts with the player.
We'll be implementing the playHand function. This function allows the user
to play out a single hand. First, though, you'll need to implement the helper
calculateHandlen function, which can be done in under five lines of code.
"""
def var_calculatehandlen(hand):
    """
    Returns the length (number of letters) in the current hand.
    hand: dictionary (string int)
    returns: integer
    """
    var_sum = 0
    for letters in hand:
        var_sum = var_sum + hand[letters]
    return var_sum
def main():
    """
    This is the main function
    """
    var_n = input()
    var_adict = {}
    for var_i in range(int(var_n)):
        var_data = input()
        var_l = var_data.split()
        var_adict[var_l[0]] = int(var_l[1])
    print(var_calculatehandlen(var_adict))
if __name__ == "__main__":
    main()
