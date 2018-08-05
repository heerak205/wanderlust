# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991


def main():
    epsilon = 0.01
    x_num = int(input())
    guess_val = x_num/2.0
    while abs(guess_val*guess_val - x_num) >= epsilon:
        guess_val = guess_val - (((guess_val**2) - x_num)/(2*guess_val))
    print(str(guess_val))
main()

