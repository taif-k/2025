import student_register
import search_data

def main():
    task_input = int(input("1-register 2-see data 3 -search: "))
    if task_input == 1: 
        student_register.register_user()
    elif task_input == 2:
        student_register.read_allfiles()
    elif task_input == 3:
        search_data.get_data()

main()


