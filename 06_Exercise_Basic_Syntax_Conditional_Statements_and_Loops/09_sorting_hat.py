student_name = input()

while student_name != 'Welcome!':
    if student_name == "Voldemort":
        print("You must not speak of that name!")
        break
    name_lenght = len(student_name)
    if name_lenght < 5:
        print(f"{student_name} goes to Gryffindor.")
    elif name_lenght == 5:
        print(f"{student_name} goes to Slytherin.")
    elif name_lenght == 6:
        print(f"{student_name} goes to Ravenclaw.")
    elif name_lenght > 6:
        print(f"{student_name} goes to Hufflepuff.")
    student_name = input()

if student_name != "Voldemort":
    print("Welcome to Hogwarts.")