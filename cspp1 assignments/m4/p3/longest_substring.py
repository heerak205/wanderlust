'''Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course.
If you have time, come back to this problem after you've had a break and cleared your head.'''

def main():
    s = input()
    temp_start = 0
    start = 0
    count = 0
    end = 0
    max_count=0
    for i in range(len(s)-1):
        if s[i]<=s[i+1]:
            count += 1
        else:
            count = 0
        if max_count < count:
            max_count = count
            temp_start = i
    start = temp_start - max_count + 1
    print(s[start:start+max_count+1])

main()
