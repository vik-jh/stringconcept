"""For a given two strings, 'str1' and 'str2', check whether they are a permutation of each other or not.
Permutations of each other.Two strings are said to be a permutation of each other when either of the string's characters can be rearranged so that it becomes identical to the other one.

Example: 
str1= "sinrtg" 
str2 = "string"

The character of the first string(str1) can be rearranged to form str2 and hence we can say that the given strings are a permutation of each other."""

def isPurmutation(s, t):
    len1 = len(s)
    len2 = len(t)

    if len1 != len2:
        return False
    else:
        for i in range(len2):
            if t[i] not in s:
                return False
        arr = [0]*256
        for char in s:
            ordr = ord(char)
            arr[ordr] = arr[ordr] + 1

        for char in t:
            ordr = ord(char)
            arr[ordr] = arr[ordr] - 1
        for i in range(256):
            if arr[i]!=0:
                return False
            return True


str1 = input()
str2 = input()
ans = isPurmutation(str1, str2)
if ans: 
    print("True")
else:
    print("False")