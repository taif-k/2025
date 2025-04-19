import student_register
import search_data
import json
import sys
import os
sys.path.append(os.getcwd())
from python import error_details,update_errorslog

path = r"D:\Repositories\2025\python\user_registration\all_students.json"
err_log = r"D:\Repositories\2025\python\user_registration\studenterror_log.txt"

def task_option():
    print("1 - Register")
    print("2 - See all Students")
    print("3 - Search data")
    print("0 - Exit")

def main_option():
    try:
        while True:
            print()
            task_option()
            task_input = input("Enter Task number: ")
            if task_input.isdigit():
                task_input = int(task_input)
                if task_input == 1: 
                    student_register.register_user()
                elif task_input == 2:
                    print(json.dumps(student_register.read_alldata(),indent=4))
                elif task_input == 3:
                    search_data.get_data()
                elif task_input == 0:
                    break
                else:
                    print("Invalid option")
            else:
                print("task number should be in digit only")
                
    except Exception as e:
        print("Please check after some time")
        update_errorslog(error_details(e),err_log)

if __name__ == "__main__":
    main_option()
    


