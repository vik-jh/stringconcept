"""For a given a string(str) and a character X, write a function to remove all the occurrences of X from the given string.
The input string will remain unchanged if the given character(X) doesn't exist in the input string.
Input Format:
The first line of input contains a string without any leading and trailing spaces.

The second line of input contains a character(X) without any leading and trailing spaces."""

def removeRepeatOccurChar(str, chr):
    if len(str) == 0:
        return str
    if chr not in str:
        return str
    ans = " "

    for i in range(len(str)):
        if str[i] == chr:
            continue
        else:
            ans += str[i]
    return ans




str = input()
chr = input()
ans = removeRepeatOccurChar(str, chr)
print(ans)