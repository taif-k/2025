from python.student_qualification.src.Domain.register_students import student_registration
from python.student_qualification.src.Domain.search import student_search


class Homepage: 
    def __init__(self):
        pass

    def menu_option(self):
        print("1 - Register Student")
        print("2 - Search Student by Qualification")

    def main_menu(self):
        self.menu_option()
        ask_menu = int(input("Enter Mmenu options: "))
        if ask_menu == 1:
            student_registration()
        elif ask_menu == 2:
            student_search()
        else:
            print("Choose valid option")

homepage_obj = Homepage()

