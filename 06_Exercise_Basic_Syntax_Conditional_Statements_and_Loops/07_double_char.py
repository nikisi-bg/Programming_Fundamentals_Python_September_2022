input_string = input()

while input_string != "End":
    if input_string == "SoftUni":
        input_string = input()
        continue
    else:
        for i in range(len(input_string)):
            character = input_string[i]
            print(character * 2, end='')
        print('')
    input_string = input()


