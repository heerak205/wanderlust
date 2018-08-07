"""
# Exercise: GCDIter
# Write a Python function, gcdIter(a, b).
# This function takes in two numbers and returns one number.
"""

def gcd_iter(a_p, b_p):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    rem = 1
    while rem != 0:
        rem = a_p%b_p
        a_p = b_p
        b_p = rem
    return a_p
def main():
    """
    calls the function
    """
    data = input()
    data = data.split()
    print(gcd_iter(int(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
