import json
datapath = r"D:\Repositories\2025\python\OOPS\Student_registration_class\studentdata.json"

class student:

    def __init__(self,datapath):
        self.recordspath = datapath
        self.menu()

    def menu(self):
        print("1 - Students Registration")
        print("2 - Display Records")
        print("3 - Search Data")
        print("0 - Exit")
        self.menu_option()

    def menu_option(self):
        while True:
            ask_menu = int(input("Enter option: "))
            if ask_menu == 1:
                self.ask_details()  
            elif ask_menu == 2:
                print(json.dumps(self.read_alldata(),indent=4))
            elif ask_menu ==3:
                self.search_student()
            elif ask_menu ==0:
                break

    def ask_details(self):
        self.studentlist = self.read_alldata()
        while True:
            self.name = input("Enter Name: ")
            self.age = int(input("Enter Age: "))
            self.grade = input("Enter Grade: ")
            studentdict = {}
            studentdict["name"] = self.name
            studentdict["age"] = self.age
            studentdict["grade"] = self.grade
            self.studentlist.append(studentdict)

            regsiter_student = input("Add More Students y/n: ")
            if regsiter_student == "y":
                continue
            else:
                self.menu_option()
                break
        self.write_data()

    def display_info(self):
        print(json.dumps(self.studentlist,indent=4))
        self.search_student()

    def search_student(self):
        search_name = input("Enter name to serach: ")
        isPresent = 0
        for data in self.studentlist:
            for key,value in data.items():
                if key == "name":
                    if value == search_name:
                        isPresent = 1
                        print(json.dumps(data,indent=3))
                        break

        if isPresent == 0:
            print("Not found")

    def write_data(self):
        with open(self.recordspath,"w") as file:
            file.write(str(json.dumps(self.studentlist,indent=3)))

    def read_alldata(self):
        try:
            with open(self.recordspath, "r") as file:
                studentrecords = json.load(file)
                return studentrecords
        except Exception as e:
            return []
    
studentdata = student(datapath)
# studentdata.menu_option()
# studentdata.read_alldata()
