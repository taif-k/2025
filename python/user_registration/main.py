import student_register
import search_data
import sys
import os
sys.path.append(os.getcwd())
from python import get_currentdate,create_log

path = r"D:\Repositories\2025\python\user_registration\all_students.json"

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
                    student_register.read_alldata()
                elif task_input == 3:
                    date = search_data.get_data()
                    print(date)
                elif task_input == 0:
                    break
                else:
                    print("Invalid option")
            else:
                print("task number should be in digit only")
                
    except Exception as e:
        print("Please check after some time")
        date = get_currentdate()
        errordict = str({"module":"main.py","function":"main_option()","error":e,"date":date})
        create_log(errordict)

main_option()


