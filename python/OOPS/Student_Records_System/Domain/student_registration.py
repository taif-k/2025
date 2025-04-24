import json
import sys,os
sys.path.append(os.getcwd())
import python

class student:
    def __init__(self,datapath,errorlog_path):
        self.recordspath = datapath
        self.__studentlist = self.read_alldata()
        self.err_path = errorlog_path

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
                print(json.dumps(self.__studentlist,indent=4))
                print()
            elif ask_menu ==3:
                self.search_student()
            elif ask_menu ==0:
                break

    def ask_details(self):
        try:
            while True:
                self.name = input("Enter Name: ")
                self.age = int(input("Enter Age: "))
                self.grade = input("Enter Grade: ")
                self.joineddate = python.error_details(get_onlydate=True)
                studentdict = {}
                studentdict["name"] = self.name
                studentdict["age"] = self.age
                studentdict["grade"] = self.grade
                studentdict["joineddate"] = self.joineddate
                self.__studentlist.append(studentdict)

                regsiter_student = input("Add More Students y/n: ")
                if regsiter_student == "y":
                    continue
                else:
                    self.menu_option()
                    break
            self.write_data()

        except Exception as e:
            print("Enter valid details...")
            python.update_errorslog(python.error_details(e),self.err_path) # error_details() using traceback module
            self.ask_details()    

    def search_student(self):
        search_name = input("Enter name to serach: ")
        isPresent = 0
        for data in self.__studentlist:
            for key,value in data.items():
                if key == "name":
                    if value == search_name:
                        isPresent = 1
                        print(json.dumps(data,indent=3))
                        print()
                        break

        if isPresent == 0:
            print("\nNot found")

    def write_data(self):
        with open(self.recordspath,"w") as file:
            file.write(json.dumps(self.__studentlist,indent=3))

    def read_alldata(self):
        try:
            with open(self.recordspath, "r") as file:
                studentrecords = json.load(file)
                return studentrecords
        except Exception as e:
            print("Student Records are blank")
            python.update_errorslog(python.error_details(e),self.err_path)
            return []

