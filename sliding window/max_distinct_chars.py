def max_distinct_chars(charArr, k):
    # char_one: index, lastIndex
    charDict = {}
    
    if len(charArr) == 0:
        return 0

    maxDistinctCount = 0

    for index, char in enumerate(charArr):   #Big-o is linear to the array length
        if char not in charDict:
            charDict[char] = [index, index, 0]

            if len(charDict) > k:
                # remove key so there are only 2 chars in our window
                # remove the key that is not the one closer to our new char
                keyToDelete = ""
                for key in charDict:
                    if key != charArr[index -1] and key != char:
                        keyToDelete = key

                for key in charDict:
                    if key != keyToDelete and key != char:
                        keyToUpdate = key
                
                # update the firsItndex of the key that will remain in the charDict
                charDict[keyToUpdate][0] = charDict[keyToDelete][1] + 1
                del charDict[keyToDelete]

                listOfChars = list(charDict.values())        
                newDistantCount = 0

                for char in listOfChars:
                    if char != keyToUpdate:
                        

                if newDistantCount > maxDistinctCount:
                    maxDistinctCount = newDistantCount

        else:
            charDict[char][1] = index # update the character's last index in the window
            ++charDict[char][2]


    return maxDistinctCount


print(max_distinct_chars("araaci", 2))    