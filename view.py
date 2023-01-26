def get_op():
    op = int(input(
        " 1 - добавить нового студента \n 2 - добавить предмет \n 3 - добавить оценки ученику по предмету \n 4 - показ списка учеников \n 5 - показ листа оценок конкретного ученика \n 6 - выход \n"))
    return op

def add_student():
    name = input("Введите имя: ")
    lastname = input("Введите фамилию: ")
    line = f"{name} {lastname}\n"
    with open("student_list.txt","a") as file:
        file.write(line)
    print("сохранено!")
    print(line)

def add_subject():
    name = input("Введите название предмета: ")
    line = f"{name}\n"
    with open("subject_list.txt","a") as file:
        file.write(line)
    print("сохранено!")
    print(line)
#
# def print_only_name():
#     with open("worker_list.txt","r") as file:
#         lst = file.readlines()
#         for line in lst:
#             a = line.split(",")
#             print(f"Имя - {a[1]}, Фамилия - {a[2]}")
#
def add_marks():
    if ""
    print("Выберите предмет: ")
    print("Выберите ученика: ")
    mark = input("Введите оценку: ")
    line = f"{mark}\n"
    with open("student_list.txt","a") as file:
        file.write(line)
    print("сохранено!")
    print(line)

def print_table():
    with open("student_list.txt","r") as file:
        for line in file.readlines():
            print(line,end="")
