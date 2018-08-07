# Exercise: Is In
# Write a Python function, isIn(char, aStr), that takes in two arguments a character and String and returns the isIn(char, aStr) which retuns a boolean value.

# This function takes in two arguments character and String and returns one boolean value.

def is_in(char_p, a_str):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    a_p = None
    char_p = char_p.lower()
    c_str = a_str.lower()
    b_str = ''.join(sorted(c_str))
    if len(b_str) == 0:
    	return "String length cannot be 0."
    elif len(b_str) == 1:
    	if char_p in b_str:
    		return True
    	return False
    else:
    	a_p = int(len(b_str)/2)
    	if char_p == b_str[a_p]:
    		return True
    	else:
    		if char_p < b_str[a_p]:
    			return is_in(char_p,b_str[:a_p])
    		return is_in(char_p,b_str[a_p:])
def main():
    """
    is a main function
    """
    data = input()
    data = data.split()
    print(is_in((data[0][0]), data[1]))
if __name__ == "__main__":
    main()
