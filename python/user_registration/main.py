import student_register
import search_data
import datetime

path = r"D:\Repositories\2025\python\user_registration\all_students.json"
log_path = r"D:\Repositories\2025\python\user_registration\studenterror_log.txt"

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
                    search_data.get_data()
                elif task_input == 0:
                    break
                else:
                    print("Invalid option")
            else:
                print("task number should be in digit only")
                
    except Exception as e:
        print("Please check after some time")
        date = datetime.datetime.now()
        errordict = str({"module":"main.py","function":"main_option()","error":e,"date":date})
        student_register.create_userfile(errordict,log_path)

main_option()


