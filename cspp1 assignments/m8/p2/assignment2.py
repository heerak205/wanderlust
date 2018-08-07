"""
# Exercise: Assignment-2
# Write a Python function
# This function takes in one number and returns one number.
"""
def sum_of_digits(n_p):
    '''
    n is positive Integer
    returns: a positive integer, the sum of digits of n.
    '''
    while n_p >= 0:
        if n_p == 0:
            return 0
        return(n_p % 10) + sum_of_digits(n_p//10)
def main():
    """
    calls main function
    """
    n_p = input()
    print(sum_of_digits(int(n_p)))
if __name__ == "__main__":
    main()
