import student_register
import search_data

def task_option():
    print("1- Register")
    print("2- See all Students")
    print("3 - Search Email")

def main():
    task_option()
    task_input = int(input("Enter Task number: "))
    if task_input == 1: 
        student_register.register_user()
    elif task_input == 2:
        student_register.read_allfiles()
    elif task_input == 3:
        search_data.get_data()


main()


