def main():
    file_object = open(r"C:\random\aoc\input2.txt", "r")
    ranges = file_object.readlines()[0].split(",")
    result = 0
    for rangeItm in ranges:
        lowerLim = int(rangeItm.split("-")[0])
        upperLim = int(rangeItm.split("-")[1])
        for val in range(lowerLim, upperLim + 1):
            stringLength = len(str(val))
            divisable_arr = getDivisArr(stringLength)
            for itm in divisable_arr:
                res = int(getResult(str(val), itm))
                result += res
                if (res != 0):
                    break    
        print(result)
    print(str(result))

def getResult(val, divide_amt):
    result_arr = []
    idx = 0
    result = val
    while idx < len(val):
        result_arr.append(val[idx: idx + divide_amt])
        idx += divide_amt
    
    cnt = 1
    while cnt < len(result_arr):
        if result_arr[cnt - 1] != result_arr[cnt]:
            result = 0
            break
        cnt += 1
    return result


def getDivisArr(stringLength):
    result_arr = []
    for val in range(1,stringLength + 1):
        if stringLength % val == 0 and stringLength != val:
            result_arr.append(val)
    return result_arr
if __name__ == "__main__":
    main()