'''
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
NOTE: String letters are case-sensitive.
Input Format:
The first line of input contains the original string. The next line contains the substring.
Each character in the string is an ascii character.
len(string) 1 to 200

Sample Input
ABCDCDC
CDC

Sample Output
2
'''
def count_substring(string, sub_string):
    len_sub=len(sub_string)
    len_str=len(string)
    out=0
    for i in range(len_str+1):
        if sub_string in string[i:i+len_sub]:
            out+=1
    return out

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
