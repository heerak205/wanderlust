# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    x_num = int(input())
    epsilon = 0.01
    lower = 0.0
    higher = x_num
    bi_val = (higher + lower)/2.0
    while abs(bi_val**2 - x_num) > epsilon:
        if bi_val**2 < x_num:
            lower = bi_val
        higher = bi_val
    bi_val = (higher + lower)/2.0
print(bi_val)
main()
