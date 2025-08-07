from python.Utils.file_io import file_io_obj
from python.OOPS.Student_Records_System.Report.search_student import StudentSearch
from python.OOPS.Student_Records_System.Utils.read_writedata import file_obj
from python.OOPS.Student_Records_System.Domain.all_paths import paths_obj
import json


class Student:
    def __init__(self, datapath):
        self.recordspath = datapath
        
    def ask_details(self):
        while True:
            try:
                studentdict = {}
                studentdict["name"] = input("Enter Name: ")
                studentdict["age"] = int(input("Enter Age: "))
                studentdict["grade"] = input("Enter Grade: ")
                studentdict["joineddate"] = file_io_obj.get_errdetails(get_date=True)
                file_obj.studentlist.append(studentdict)

                if input("Add More Students y/n: ").lower() != "y":
                    break

            except Exception as e:
                print("Enter valid details...")
                file_io_obj.update_errorslog(file_io_obj.get_errdetails(e),paths_obj.err_log_path) # traceback module to get dyn. err details
        file_io_obj.write_data(data=file_obj.studentlist,path=self.recordspath)


class StudentMenu(Student):
    def __init__(self, datapath):
        super().__init__(datapath)

    def menu(self):
        print("1 - Students Registration")
        print("2 - Display Records")
        print("3 - Search Data")
        print("0 - Exit")

    def menu_option(self):
        try:
            while True:
                self.menu()
                ask_menu = int(input("Enter option: "))
                if ask_menu == 1:
                    self.ask_details()
                elif ask_menu == 2:
                    print(json.dumps(file_obj.studentlist, indent=4))
                    print()
                elif ask_menu == 3:
                    searchobj = StudentSearch(self.recordspath)
                    searchobj.search_student()
                elif ask_menu == 0:
                    break
        except Exception as e:
            file_io_obj.update_errorslog(file_io_obj.get_errdetails(e),paths_obj.err_log_path)
