'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    ''''
    tokenize function to create a search index dictionary
    '''
    a_dict = {}
    string_split = string.split(" ")
    #return string_split
    for each_word in string_split:
        if each_word not in a_dict:
            a_dict[each_word] = 1
        else:
            a_dict[each_word] += 1
    return a_dict
def main():
    '''
    main function
    '''
    no_of_lines = int(input())
    string = input()
    print(tokenize(string))

if __name__ == '__main__':
    main()
