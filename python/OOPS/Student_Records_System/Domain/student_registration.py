import json
import python as py_lang

class Student:
    def __init__(self,datapath,errorlog_path):
        self.recordspath = datapath
        self.err_path = errorlog_path

    def ask_details(self):        
            while True:
                try:
                    studentdict = {}
                    studentdict["name"] = input("Enter Name: ")
                    studentdict["age"] = int(input("Enter Age: "))
                    studentdict["grade"] = input("Enter Grade: ")
                    studentdict["joineddate"] = py_lang.error_details(get_onlydate=True)
                    self.listobj = py_lang.DataOperations(self.recordspath,self.err_path)
                    self.listobj.studentlist.append(studentdict)

                    if input("Add More Students y/n: ").lower() != "y":
                        break

                except Exception as e:
                    print("Enter valid details...")
                    py_lang.update_errorslog(py_lang.error_details(e),self.err_path) # error_details() using traceback module
            self.listobj.write_data()            

        
class StudentMenu(Student):
    def menu(self):
            print("1 - Students Registration")
            print("2 - Display Records")
            print("3 - Search Data")
            print("0 - Exit")

    def menu_option(self):
        while True:
            self.menu()
            ask_menu = int(input("Enter option: "))
            if ask_menu == 1:
                self.ask_details()  
            elif ask_menu == 2:
                listobj = py_lang.DataOperations(self.recordspath,self.err_path)
                print(json.dumps(listobj.studentlist,indent=4))
                print()
            elif ask_menu ==3:
                searchobj = py_lang.StudentSearch(self.recordspath, self.err_path)
                searchobj.search_student()
            elif ask_menu ==0:
                break 

