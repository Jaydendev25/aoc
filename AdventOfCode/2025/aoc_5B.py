def main():
    file_object = open(r"C:\random\aoc\input5.txt", "r")
    lines = file_object.readlines()
    rangesToTest  = []
    addNumbers = False
    resultRanges = []
    # Build list of ranges
    for line in lines:
        if (line == "\n"):
            addNumbers = True
        elif (addNumbers != True):
            rangesToTest.append(line.replace("\n", ""))

    # Sort Ranges in ascending order
    sortedList = []
    lowestVal = rangesToTest[0].split('-')[0]
    lowestValFullStr = rangesToTest[0]
    lenRange = len(rangesToTest)
    for x in range(lenRange):
        for rge in rangesToTest:
            if (int(rge.split('-')[0]) < int(lowestVal)):
                lowestVal = rge.split('-')[0]
                lowestValFullStr = rge
            elif (int(rge.split('-')[0]) == int(lowestVal)):
                if (int(rge.split('-')[1]) < int(lowestValFullStr.split('-')[1])):
                    lowestVal = rge.split('-')[0]
                    lowestValFullStr = rge  

        sortedList.append(lowestValFullStr)
        rangesToTest.remove(lowestValFullStr)
        if (len(rangesToTest) == 0):
            break
        lowestVal = rangesToTest[0].split('-')[0]
        lowestValFullStr = rangesToTest[0]

    # Loop through sorted list and combine ranges to get rid of overlaps 
    i = 1
    saveRange = sortedList[0]
    while i < len(sortedList):
        currMinVal = sortedList[i].split('-')[0]
        prevMaxVal = sortedList[i-1].split('-')[1]
        currMaxVal = sortedList[i].split('-')[1]
        if (int(currMinVal) <= int(prevMaxVal)):
            if (int(currMaxVal) > int(prevMaxVal)):
                saveRange = saveRange.split('-')[0] + "-" + currMaxVal
        else:
            resultRanges.append(saveRange)
            saveRange = sortedList[i]
        
        i += 1
        if (i >= len(sortedList)):
            resultRanges.append(saveRange)

    #Find result by taking maxVal - minVal + 1 for each range
    result = 0
    for rge in resultRanges:
        minVal = rge.split('-')[0]
        maxVal = rge.split('-')[1]

        result += (int(maxVal) - int(minVal) + 1)

    print(result)
    
if __name__ == "__main__":
    main()