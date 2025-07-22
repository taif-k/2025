from python.student_qualification.src.Domain.register_students import student_obj
from python.student_qualification.src.Domain.search import search_obj
from python.student_qualification.src.Domain.paths import diff_path_obj
from python.Programs.error_source import error_details,update_errorslog

class Homepage:
    def __init__(self):
        pass

    def menu_option(self):
        print("1 - Register Student")
        print("2 - Search Student by Qualification")

    def main_menu(self):
        try:
            self.menu_option()
            ask_menu = int(input("Enter Menu option: "))
            if ask_menu == 1:
                student_obj.student_registration()
            elif ask_menu == 2:
                search_obj.student_search()
            else:
                print("Choose valid option")
        except Exception as e:
            update_errorslog(error_details(e),diff_path_obj)

homepage_obj = Homepage()
