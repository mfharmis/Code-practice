'''
https://www.hackerrank.com/challenges/merge-the-tools/
Consider the following:

. A string, s, of length n where s = coc1 . . . Cn-1.
. An integer, k, where k is a factor of n.

We can split s into n/k substrings where each subtring, ti, consists of a contiguous block of
k characters in s. Then, use each ti to create string ui such that:
. The characters in uj are a subsequence of the characters in ti.

. Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once. In other words, if the character at some index j in
ti occurs at a previous index < j in ti, then do not include the character in string ui.

Given s and k, print " lines where each line i denotes string ui.

Example
s='AAABCADDE'
k=3

There are three substrings of length 3 to consider: 'AAA', 'BCA' and 'DDE'. The first substring is all 'A' characters, so u1 = 'A'. The second substring has all distinct characters,
so u2 = 'BCA'. The third substring has 2 different characters, so u3 = 'DE'. Note that a subsequence maintains the original order of characters encountered. The order of characters
in each subsequence shown is important.

Sample Input:
STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3

Sample Output
AB
CA
AD
Explanation:
Split s into n/k = 9/3 = 3 equal parts of length k = 3. Convert each ti to ui by removing
any subsequent occurrences of non-distinct characters in ti:

1. to = "AAB" > u0 = "AB"

2. t1="CAA" -> u1="CA"

3. t2="ADA" -> u2 = "AD"

Print each uj on a new line.

'''
def merge_the_tools(string, k):
    out_string = ""
    n=0
    for x in string:
        if x not in out_string:
            out_string +=x
        n+=1
        if n==k:
            print (out_string)
            n=0
            out_string=""


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
