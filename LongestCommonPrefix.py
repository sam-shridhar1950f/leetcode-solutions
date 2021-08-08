def LongestCommonPrefix(arrayOfStrings):
    for i in range(len(arrayOfStrings) - 1):
        if arrayOfStrings[i][0] != arrayOfStrings[i + 1][0]:
            return ""
    testWord = arrayOfStrings[0].split("")  # first word in the array
    for string in arrayOfStrings[1::]:
        curWord = string.split("")
        
        
        


