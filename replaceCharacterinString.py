def strReplace(str, char1, char2):
    newStr = " "
    for ele in str:
        if ele == char1:
            newStr = newStr + char2
        else:
            newStr = newStr + ele
    return newStr




str = input()
char1 = input()
char2 = input()

str1 = strReplace(str, char1, char2)
print(str1)