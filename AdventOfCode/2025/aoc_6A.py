def main():
    file_object = open(r"C:\random\aoc\input6.txt", "r")
    lines = file_object.readlines()
    result = 0
    matrix = [[0 for x in range(len(lines))] for y in range(len(lines[0].split(" ")))]

    for x in range(len(lines)):
        for y in range(len(lines[0].split())):
            matrix[y][x] = lines[x].split()[y]
            y += 1
        x += 1


    for y in range(len(lines[0].split())):   
        tmpResult = 0
        for x in range(len(lines)):
            if x == 0:
                tmpResult = int(matrix[y][x])
            else:
                if x != len(matrix[y]) - 1:
                    if matrix[y][len(matrix[x]) - 1] == '*':
                        tmpResult *= int(matrix[y][x])
                    elif matrix[y][len(matrix[x]) - 1] == '+':
                        tmpResult += int(matrix[y][x])
                    elif matrix[y][len(matrix[x]) - 1] == '/':
                        tmpResult /= int(matrix[y][x])
                    elif matrix[y][len(matrix[x]) - 1] == '-':
                        tmpResult -= int(matrix[y][x])
            x += 1
        
        result += tmpResult
        y += 1
    print (result)
            




if __name__ == "__main__":
    main()
