# Assumptions:
#   - There is only 5 lines
#   - Each line has the same amount of characters
def main():
    file_object = open(r"C:\random\aoc\input6.txt", "r")
    lines = file_object.readlines()
    result = 0
    matrix = []

    tmpArray = [""] * 5
    for x in range(len(lines[0])):
        split = True
        for y in range(len(lines)):
            tmpArray[y] = str(tmpArray[y]) + lines[y][x]
            if lines[y][x].strip():
                split = False

        if split:
            matrix.append(tmpArray)
            tmpArray = [""] * 5

    for x in range(len(matrix)):
        numOfDigits = len(matrix[x][0])
        tmpArray = [""] * numOfDigits
        for y in range(len(matrix[x]) - 1):
            tmp = 0
            for z in range(numOfDigits - 1, -1, -1):
                if matrix[x][y][z].strip():
                    tmpArray[tmp] = tmpArray[tmp] + matrix[x][y][z]
                tmp += 1

        tmpResult = 0
        firstRec = True
        for i in range(len(tmpArray)):
            if len(tmpArray[i]) == 0:
                continue

            if firstRec:
                tmpResult = int(tmpArray[i])
                firstRec = False
            else:
                opp = matrix[x][len(matrix[x]) - 1].replace(" ", "")
                opp = opp.replace("\n", "")
                if opp == '*':
                    tmpResult *= int(tmpArray[i])
                elif opp == '+':
                    tmpResult += int(tmpArray[i])
                elif opp == '/':
                    tmpResult /= int(tmpArray[i])
                elif opp == '-':
                    tmpResult -= int(tmpArray[i])  
                else:
                    print("Unknown Opp")

        result += tmpResult   
    print(result)

if __name__ == "__main__":
    main()