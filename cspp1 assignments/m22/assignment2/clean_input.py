'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    '''
	cleans string
	'''
    clean_s = re.sub("[^a-zand^1-10and^A-Z]", "", string)
    return clean_s
def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
