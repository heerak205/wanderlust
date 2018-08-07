"""
# Exercise: GCDRecr
# Write a Python function, gcdRecur(a, b).
# This function takes in two numbers and returns one number.
"""

def gcd_recur(a_p, b_p):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b_p == 0:
        return a_p
    return gcd_recur(b_p, a_p%b_p)
def main():
    """
    main function
    """
    data = input()
    data = data.split()
    print(gcd_recur(int(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
