"""
# Assignment-3
At this point, we have written code to generate a random hand and display that
hand to the user. We can also ask the user for a word (Python's input) and score
the word (using your getWordScore). However, at this point we have not written
any code to verify that a word given by a player obeys the rules of the game.
A valid word is in the word list; and it is composed entirely of letters from
the current hand. Implement the isValidWord function.
Testing: Make sure the test_isValidWord tests pass. In addition, you will want
to test your implementation by calling it multiple times on the same hand - what
should the correct behavior be? Additionally, the empty string ('') is not a valid
word - if you code this function correctly, you shouldn't need an additional
check for this condition.
Fill in the code for isValidWord in ps4a.py and be sure you've passed the 
appropriate tests in test_ps4a.py before pasting your function definition here.
"""
def isValidWord(word, hand, var_wordlist):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or wordList.
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    var_count = 0
    var_len = len(var_wordlist)
    if word in var_wordlist:
        for var_i in hand:
            if var_i in word:
                var_count += 1
    if var_count == var_len:
        return True
    return False
def main():
    var_word = input()
    var_n = int(input())
    var_adict = {}
    for var_i in range(var_n):
        var_data = input()
        var_l = var_data.split()
        var_adict[var_l[0]] = int(var_l[1])
    var_l2 = list(input().split())
    print(isValidWord(var_word, var_adict, var_l2))
if __name__ == "__main__":
    main()
