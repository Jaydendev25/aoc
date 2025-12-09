def main():
    result = 0
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

        if (current_position == 0):
            result += 1
        print(string)
    
    print("Result: " + str(result))

    
def add(current_position, val):
    new_pos = (current_position + val) % 100
    return new_pos 

def sub(current_position, val):
    new_pos = (current_position - val) % 100
    return new_pos 


if __name__ == "__main__":
    main()
