'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    '''
    main function
    '''
    no_of_lines = int(input())
    lines_str = ""
    for _ in range(no_of_lines):
        lines_str += input() + "\n"

    print(lines_str)

if __name__ == '__main__':
    main()
