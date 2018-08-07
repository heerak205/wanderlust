"""
# Exercise: PowerIter
# Write a Python function, for base^exp
# This function takes in two numbers and returns one number.
"""

def iter_power(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    h_p = 1
    while exp > 0:
        h_p = h_p*base
        exp -= 1
    return h_p
def main():
    """
    main function that calls
    """
    data = input()
    data = data.split()
    print(iter_power(float(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
