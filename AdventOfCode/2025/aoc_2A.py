def main():
    file_object = open(r"C:\random\aoc\input2.txt", "r")
    ranges = file_object.readlines()[0].split(",")
    result = 0
    for rangeItm in ranges:
        lowerLim = int(rangeItm.split("-")[0])
        upperLim = int(rangeItm.split("-")[1])
        for val in range(lowerLim, upperLim + 1):
            stringLength = len(str(val))
            if stringLength % 2 != 0:
                continue
            patternlength = int(stringLength / 2)
            pattern = str(val)[0:patternlength]
            secondHalf = str(val)[patternlength:]
            if pattern == secondHalf:
                result += val
    
    print(str(result))


        



if __name__ == "__main__":
    main()