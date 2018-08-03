# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube
"""
perfect cube
"""
def main():
    s_number = int(input("n"))
    i = 1
    while i**3 < s_number:
        i += 1
    if i**3 == s_number:
        print("its a perfect cube")
    else:
        print("its not a perfect cube")
main()
	
