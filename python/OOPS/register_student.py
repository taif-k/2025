import json

class student:
    def __init__(self):
        self.menu()

    def menu(self):
        print("1- Register")
        print("2- Display")
        print("3- Search Student")
        print("0- Exit")
        self.menu_option()

    def menu_option(self):
        while True:
            ask_option = int(input("Enter option: ")) 
            if ask_option == 1:
                self.ask_details()
            elif ask_option == 2:
                self.display_info()       
            elif ask_option == 3:
                pass
                # self.search_student()
            elif ask_option == 0:
                break

    def ask_details(self):
        self.studentlist = []
        while True:
            self.name = input("Enter Name: ")
            self.age = int(input("Enter Age: "))
            self.grade = input("Enter Grade: ")
            studentdict = {}
            studentdict["name"] = self.name
            studentdict["age"] = self.age
            studentdict["grade"] = self.grade
            self.studentlist.append(studentdict)

            regsiter_student = input("Add Student y/n: ")
            if regsiter_student == "y":
                continue
            else:
                self.menu()
                break
        
    def display_info(self):
        print(json.dumps(self.studentlist,indent=4))

    # def search_student(self):
    #     search_name = input("Enter name to serach: ")
    #     iPresent = 0
    #     for data in self.studentlist:
    #         for key,value in data:
    #             if key == "name":
    #                 if value == search_name:
    #                     print(data)

    #     if iPresent == 0:
    #         print("Not found")

studentdata = student()
