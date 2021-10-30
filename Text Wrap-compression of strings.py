'''You are given a string s and width w.
Your task is to wrap the string into a paragraph of width w
Sample input
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ.'''
import textwrap

def wrap(string, max_width):
    return "\n".join([string[i:i+max_width]for i in range(0,len(string)+1,max_width)])

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
'''In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .

You are given a string . Suppose a character '' occurs consecutively  times in the string. Replace these consecutive occurrences of the character '' with  in the string.

For a better understanding of the problem, check the explanation.

Input Format

A single line of input consisting of the string .

Output Format

A single line of output consisting of the modified string'''
from itertools import groupby
a = input()
#x = itertools.groupby(a)
for k,g in groupby(a):
    print(( len(list(g)),int(k)),end=" ")

    
