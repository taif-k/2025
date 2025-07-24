from python.student_qualification.src.Domain.register_students import student_obj
from python.student_qualification.src.Domain.search import search_obj
from python.student_qualification.src.Domain.paths import diff_path_obj
from python.Utils.file_io import file_io_obj


class Homepage:
    def __init__(self):
        pass

    def menu_option(self):
        print("1 - Register Student")
        print("2 - Search Student by Qualification")
        print("0 - Exit")

    def main_menu(self):
        try:
            while True:
                self.menu_option()
                ask_menu = int(input("Enter Menu option: "))
                if ask_menu == 1:
                    student_obj.student_registration()
                elif ask_menu == 2:
                    search_obj.student_search()
                elif ask_menu == 0:
                    break
                else:
                    print("Choose valid option")
        except Exception as e:
            file_io_obj.update_errorslog(file_io_obj.get_errdetails(e),diff_path_obj.errorlog_path)

homepage_obj = Homepage()
