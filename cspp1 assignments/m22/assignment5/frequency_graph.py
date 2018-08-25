'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''
def new_freq(temp):
    '''
    replaces numbrs with "#"
    '''
    new_list = []
    while temp > 0:
        new_list.append("#")
        temp -= 1
    return ''.join(new_list)

def frequency_graph(dictionary):
    '''
    frequency_graph function to print out the required output
    '''
    new_list = []
    for i in dictionary.keys():
        new_list.append(i)
    new_list.sort()
    for i in new_list:
        temp = dictionary[i]
        print(i, "-", new_freq(temp))

def main():
    '''
    main function
    '''
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
