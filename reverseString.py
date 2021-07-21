"""Aadil has been provided with a sentence in the form of a string as a function parameter. The task is to implement a function so as to print the sentence such that each word in the sentence is reversed.
Example:
Input Sentence: "Hello, I am Aadil!"
The expected output will print, ",olleH I ma !lidaA"."""

"""def reverseString(string):
    
    if len(string) == 0 or len(string) == 1:
        return string

    str1 = string.split()
    for ele in str1:
        str2 = str1[::-1]
        return str2"""


def reverseEachWord(string) :
	# Your code goes here
    string = string.split()
    for i in string:
        print(i[::-1] , end = " ")


str = input()
ans = reverseEachWord(str)
"print(ans, end=" ")"



