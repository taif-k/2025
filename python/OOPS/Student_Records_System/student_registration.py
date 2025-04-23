import json
datapath = r"D:\Repositories\2025\python\OOPS\Student_Records_System\studentdata.json"

class student:

    def __init__(self,datapath):
        self.recordspath = datapath
        self.studentlist = []

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
                print(json.dumps(self.read_alldata(),indent=4))
                print()
            elif ask_menu ==3:
                self.search_student()
            elif ask_menu ==0:
                break

    def ask_details(self):
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

    def search_student(self):
        search_name = input("Enter name to serach: ")
        isPresent = 0
        for data in self.read_alldata():
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
            file.write(str(json.dumps(self.studentlist,indent=3)))

    def read_alldata(self):
        try:
            with open(self.recordspath, "r") as file:
                self.studentrecords = json.load(file)
                return self.studentrecords
        except Exception as e:
            print("Student Records are blank")
            return []
    
studentdata = student(datapath)
studentdata.menu_option()

