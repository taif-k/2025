import Domain
import json
import Report

def menu():
    print("1 - Student Registration")
    print("2 - Display All Records")
    print("3 - Get Report")
    print("0 - Exit")

def menu_option():
    print("\n----STUDENT RECORDS MANAGEMENT SYSTEM----\n")
    while True:
        menu()
        task_input = input("Enter Task number: ")
        if task_input.isdigit():
            task_input = int(task_input)
            if task_input == 1: 
                Domain.register_user()
            elif task_input == 2:
                data = Domain.read_allrecords()
                print(json.dumps(data,indent=4))
            elif task_input == 3:
                Report.get_data()
            elif task_input == 0:
                break
            else:
                print("Invalid option\n")
        else:
            print("Task number should be in digit only\n")     

 
            
