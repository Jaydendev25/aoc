def main():
    result = 0
    file_object = open(r"C:\random\aoc\input5.txt", "r")
    lines = file_object.readlines()
    numbersToTest = []
    rangesToTest  = []
    addNumbers = False
    
    for line in lines:
        if (line == "\n"):
            addNumbers = True
        elif (addNumbers != True):
            rangesToTest.append(line.replace("\n", ""))
        elif (addNumbers):
            numbersToTest.append(line.replace("\n", ""))
    
    for num in numbersToTest:        
        for rge in rangesToTest:
            lineSplit = rge.split('-')
            minVal = lineSplit[0]
            maxVal = lineSplit[1]
            if (int(num) >= int(minVal) and int(num) <= int(maxVal)):
                result += 1
                break
    
    print(result)







if __name__ == "__main__":
    main()