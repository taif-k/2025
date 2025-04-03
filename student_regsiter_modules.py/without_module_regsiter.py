
def student_register():
    studentlist = []
    for n in range(1,3):
        studentdict = {}
        
        studentdict["id"] = int(input("Enter id: "))
        studentdict["name"] = input("Enter name: ")
        studentdict["email"] = input("Enter email: ")
        studentdict["contact"] = int(input("Enter contact: "))
        studentlist.append(studentdict)
    return studentlist    

def student_search(output):
    search_name = input("Enter name to search: ")
    ispresent = False
    for dict in output:
        if dict["name"] == search_name:
            ispresent = True
            print(dict)

    if ispresent == False:
        print("Not found")   

def get_student(output):
    print(output)

def menu():
    print("1 - Student Registration")
    print("2 - Search Student")
    print("3 - Get details")
menu()

output = []

while True:
    task_input = int(input("Enter task no"))
    if task_input == 1:
        output = student_register()
    elif task_input == 2:
        student_search(output)
    elif task_input == 3:
        get_student(output)

