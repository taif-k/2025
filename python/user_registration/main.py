import student_register
import search_data

def main():
    datalist = []
    datalist = student_register.register_user()
    search_data.get_data(datalist)


main()


