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
    if exp == 1:
        return base
    return base*iter_power(base, exp-1)


def main():
    """
    main function that calls
    """
    data = input()
    data = data.split()
    print(iter_power(float(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
