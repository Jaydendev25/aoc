result = 0
def main():
    global result
    current_position = 50
    file_object = open(r"C:\random\aoc\input1.txt", "r")
    all_lines = file_object.readlines()

    for line in all_lines:
        string = "Current Pos: " + str(current_position)
        val = int(line[1:len(line)])
        
        if (line[0] == 'L'):
            string += " Val to Sub: " + str(val)
            current_position = sub(current_position, val)
            string += " New Pos: " + str(current_position)
        else:
            string += " Val to add: " + str(val)
            current_position = add(current_position, val)
            string += " New Pos: " + str(current_position)
        string += " New Result:" + str(result)
        print(string)
    
    print("Result: " + str(result))

    
def add(current_position, val):
    global result
    result += int((current_position + val) / 100)
    new_pos = (current_position + val) % 100

    return new_pos 

def sub(current_position, val):
    global result
    result += int((((100 - current_position) % 100) + val) / 100)
    new_pos = (current_position - val) % 100

    return new_pos 


if __name__ == "__main__":
    main()
