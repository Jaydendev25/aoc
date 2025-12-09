def main():
    file_object = open(r"C:\random\aoc\input4.txt", "r")
    lines = file_object.readlines()
    result = 0
    # Get X and Y boundaries
    rows = 0
    cols = 0
    for line in lines:
        cols = len(line)
        rows += 1
    
    # Build 2d Array
    arr = [[0] * cols for _ in range(rows)]
    
    # Populate Array
    for row in range(rows):
        for col in range(cols-1):
            line = lines[row]
            arr[row][col] = line[col]
    
    for row in range(rows):
        for col in range(cols):
            if arr[row][col] != '@':
                continue
            tmp = 0
            if row > 0:
                if arr[row - 1][col] == '@':
                    tmp += 1
                if col > 0:
                    if arr[row - 1][col - 1] == '@':
                        tmp += 1
                if col < cols:
                    if arr[row - 1][col + 1] == '@':
                        tmp += 1
            if col > 0:
                if arr[row][col - 1] == '@':
                    tmp += 1
            if col < cols:
                if arr[row][col + 1] == '@':
                    tmp += 1
            if row < rows-1:
                if arr[row + 1][col] == '@':
                    tmp += 1   
                if col > 0:
                    if arr[row + 1][col - 1] == '@':
                        tmp += 1
                if col < cols:
                    if arr[row + 1][col + 1] == '@':
                        tmp += 1 
            if tmp < 4:
                result += 1
    print(result)

if __name__ == "__main__":
    main()