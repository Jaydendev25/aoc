def main():
    file_object = open(r"C:\random\aoc\input3.txt", "r")
    banks = file_object.readlines()
    result = 0
    for bank in banks:
        biggestNum = 0
        bankLength = len(bank)
        x = 0
        while x < bankLength:
            y = x + 1
            while y < bankLength:
                val = int(bank[x] + bank[y])
                if (val > biggestNum):
                    biggestNum = val
                y += 1
            x += 1
        result += biggestNum
    
    print(result)




if __name__ == "__main__":
    main()