import json
import python

class Student:
    def __init__(self,datapath,errorlog_path):
        self.recordspath = datapath
        self.studentlist = self.read_alldata()
        self.err_path = errorlog_path

    def write_data(self):
        with open(self.recordspath,"w") as file:
            file.write(json.dumps(self.studentlist,indent=3))

    def read_alldata(self):
        try:
            with open(self.recordspath, "r") as file:
                studentrecords = json.load(file)
                return studentrecords
        except Exception as e:
            print("Student Records are blank")
            python.update_errorslog(python.error_details(e),self.err_path)
            return []   

    def ask_details(self):
        
            while True:
                try:
                    self.name = input("Enter Name: ")
                    self.age = int(input("Enter Age: "))
                    self.grade = input("Enter Grade: ")
                    self.joineddate = python.error_details(get_onlydate=True)
                    studentdict = {}
                    studentdict["name"] = self.name
                    studentdict["age"] = self.age
                    studentdict["grade"] = self.grade
                    studentdict["joineddate"] = self.joineddate
                    self.studentlist.append(studentdict)

                    if input("Add More Students y/n: ").lower() != "y":
                        break

                except Exception as e:
                    print("Enter valid details...")
                    python.update_errorslog(python.error_details(e),self.err_path) # error_details() using traceback module
            self.write_data()            

        
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
                print(json.dumps(self.studentlist,indent=4))
                print()
            elif ask_menu ==3:
                searchobj = python.StudentSearch(self.recordspath, self.err_path)
                searchobj.search_student()
            elif ask_menu ==0:
                break 

