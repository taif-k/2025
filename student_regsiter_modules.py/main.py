import studentregister
import studentdetails
import studentsearch

def menu():
    print("1 - Registration")
    print("2 - Get details")
    print("3 - Search")
    print("0 - Exit")
 
def userinput():
    data = []
    while True:
        task_input = input("Enter task number: ")
        if task_input.isdigit():
            task_input = int(task_input)
            if task_input == 1:
                data = studentregister.student_register()
            elif task_input == 2:
                studentdetails.get_student(data)
            elif task_input == 3:
                studentsearch.student_search(data)
            elif task_input == 0:
                break
            else:
                print("Choose Valid option")
        else:
            print("Task number should be in digit")
    
menu()
userinput()