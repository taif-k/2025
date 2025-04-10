import json
import student_register

path =  r"D:\student_details\all_students.json" # update path accordingly to avoid error

def search_menu():
    print("1- Search Email")
    print("2- Search name")
    print("3- Search contact")
    print("4- Search address")
    print("0 - Go Back")

def get_file():
    with open(path,"r") as file:
        jsondata = json.load(file)
        return jsondata
         
def get_data():
    while True:
        print()
        search_menu()
        search_option = input("Enter search option: ")
        if search_option.isdigit():
            search_option = int(search_option)
            if search_option == 1:
                try:
                    search_email = input("Enter email to search: ")
                    data = get_file()
                    ispresent = False
                    for studentdict in data:
                        for key,value in studentdict.items():
                            if key == "email":
                                if value == search_email.lower():
                                    ispresent = True
                                    print(studentdict)
                                    break

                    if ispresent == False:
                        print("Email not found")
                except:
                    print("Students not registered yet") 
                    student_register.register_user() 

            elif search_option == 2:
                try:
                    search_name = input("Enter name to search: ")
                    data = get_file()
                    ispresent = False
                    for studentdict in data:
                        for key,value in studentdict.items():
                            if key == "name":
                                if value == search_name.lower():
                                    ispresent = True
                                    print(studentdict)
                                    break

                    if ispresent == False:
                        print("name not found")
                except:
                    print("Students not registered yet") 
                    student_register.register_user()       

            elif search_option == 3:
                try:
                    search_contact = int(input("Enter contact to search: "))
                    data = get_file()
                    ispresent = False
                    for studentdict in data:
                        for key,value in studentdict.items():
                            if key == "contact":
                                if value == search_contact:
                                    ispresent = True
                                    print(studentdict)
                                    break

                    if ispresent == False:
                        print("contact not found")
                except:
                    print("Students not registered yet") 
                    student_register.register_user()                     

            elif search_option == 4:
                try:
                    search_address = input("Enter address to search: ")
                    data = get_file()
                    ispresent = False
                    for studentdict in data:
                        for key,value in studentdict.items():
                            if key == "address":
                                if value == search_address.lower():
                                    ispresent = True
                                    print(studentdict)
                                    break

                    if ispresent == False:
                        print("Address not found")
                except:
                    print("Students not registered yet") 
                    student_register.register_user() 

            elif search_option == 0:
                break
            else:
                print("Invalid option")
        else:
            print("Task number should be in digits")


