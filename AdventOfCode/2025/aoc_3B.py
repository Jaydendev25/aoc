def main():
    file_object = open(r"C:\random\aoc\input3.txt", "r")
    banks = file_object.readlines()
    result = 0
    for bank in banks:
        bankLength = (len(bank)-1)
        if bankLength <= 12:
            result += int(bank)
            break
        
        bankNum = ""
        currNum = 0
        currIdx = 0
        x = 0
        while x < 12:
            y = currIdx
            currNum = 0
            while y < bankLength:
                if int(bank[y]) > currNum:
                    currNum = int(bank[y])
                    currIdx = y + 1
                    if currNum == 9:
                        break

                if (bankLength - y <= (12 - len(bankNum))):
                    break
                y += 1
            bankNum += str(currNum)
            x += 1
        result += int(bankNum)
        print(result)
    


 



if __name__ == "__main__":
    main()