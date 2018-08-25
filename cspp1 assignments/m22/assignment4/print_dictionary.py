'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    '''
    function of print_dictionary
    '''
    new_list = []
    for i in dictionary.keys():
        new_list.append(i)
    new_list.sort()
    for i in new_list:
        print(i, "-", dictionary[i])
def main():
    '''
    main function
    '''
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
