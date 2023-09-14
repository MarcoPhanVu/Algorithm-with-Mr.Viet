

wholeStr = input("Please type in the whole string: ")
if wholeStr == "":
    wholeStr = "ababaabbbaab"
    print(f'Then your whole string will be: {wholeStr}')
    
subStr = input("Please type in the sub string: ")
if subStr == "":
    subStr = "ab*"
    print(f'Then your sub string will be: {subStr}')

def convertToNum(string): # only for this problem
    str = list(string)

    for i in range(len(str)):
        match str[i]:
            case "a":
                str[i] = 1
            case "b":
                str[i] = -1
            case "*":
                str[i] = 0
            case _:
                print('Other character than "a", "b" and "*" are unavailable for now')     

    return str
    
wholeList = convertToNum(wholeStr)
subList = convertToNum(subStr)

print("Matching position(s): ")

def checkMatchSubList(subList, wholeList):
    matchedPosition = []
    wholeLen = len(wholeList)
    subLen = len(subList)
    totalChars = 0
    tempCount = 0
    
    for i in range(subLen): # get K characters
        if subList[i] != 0:
            totalChars += 1;
    
    
    for i in range(wholeLen - subLen): # remove unnecessary amount of comparisons
        tempCount = 0
        for j in range(subLen):
            tempCount += wholeList[i + j] * subList[j]
        
        if (tempCount == totalChars):
            matchedPosition.append(i)
    
    return matchedPosition


print(checkMatchSubList(subList, wholeList))
