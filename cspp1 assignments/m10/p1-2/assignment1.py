
"""
#Exercise : Assignment-1
#implement the function getAvailableLetters that takes in one parameter
- a list of letters, lettersGuessed.
This function returns a string that is comprised of lowercase English letters
 - all lowercase English letters that are not in lettersGuessed
"""
def var_getavailableletters(var_lettersguessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    p_a = list("abcdefghijklmnopqrstuvwxyz")
    p_b = sorted(var_lettersguessed)
    var_acopy = p_a[:]
    for i in var_acopy:
        if i in p_b:
            p_a.remove(i)
    return ''.join(p_a)
def main():
    '''
    Main function for the given program
    '''
    user_input = input()
    user_input = user_input.split()
    var_data = []
    for var_char in user_input:
        var_data.append(var_char[0])
    print(var_getavailableletters(var_data))
if __name__ == "__main__":
    main()
