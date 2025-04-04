import studentregister
import studentdetails
import studentsearch

def menu():
    print("1 - Registration")
    print("2 - Get details")
    print("3 - Search")

def userinput():
    data = []
    task_input = int(input("Enter task number: "))
    if task_input == 1:
        data = studentregister.student_register()
    elif task_input == 2:
        studentdetails.get_student(data)
    elif task_input == 3:
        studentsearch.student_search(data)
    else:
        print("Choose Valid option")
        

menu()
userinput()