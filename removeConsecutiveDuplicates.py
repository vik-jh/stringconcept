"""For a given string(str), remove all the consecutive duplicate characters.
Example:
Input String: "aaaa"
Expected Output: "a"

Input String: "aabbbcc"
Expected Output: "abc"""

def uniqueString(string):

    if len(string) == 0:
        return string
    answ = " "

    startIndex = 0
    while startIndex < len(string):
        uniqueChar = string[startIndex]
        nextUniqueChar = startIndex + 1

        while(nextUniqueChar < len(string)) and (string[nextUniqueChar] == uniqueChar):
            nextUniqueChar += 1
        answ +=uniqueChar
        startIndex = nextUniqueChar

    return answ





str = input()
ans = uniqueString(str)
print(ans)