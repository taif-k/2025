import student_register
import search_data

def main():
    datalist = []
    user_input = int(input("Enter 1 to register or 2 to see details:"))
    datalist = student_register.register_user()
    search_data.get_data(datalist)


main()


