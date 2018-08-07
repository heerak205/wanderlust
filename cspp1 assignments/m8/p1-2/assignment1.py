"""
# Exercise: Assignment-1
# Write a Python function, factorial(n).
# This function takes in one number and returns one number.
"""
def factorial(n_p):
    '''
    n is positive Integer
    returns: a positive integer, the factorial of n.
    '''
    if n_p == 0:
        return 1
    return n_p*factorial(n_p-1)
def main():
    """
    main function
    """
    a_p = input()
    print(factorial(int(a_p)))
if __name__ == "__main__":
    main()
