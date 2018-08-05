# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

'''This program evaluates the square root of a number.'''
def main():
    '''Main function.'''
epsilon = 0.01
step = 0.1
square = int(input())
guess = 0.0
while guess <= square:
    if abs(guess**2-square) < epsilon:
        break
    else:
        guess += step
print(str(guess))
if __name__ == "__main__":
    main()
