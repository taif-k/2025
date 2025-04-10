import json

path =  r"D:\student_details\all_students.json" # update path accordingly to avoid error

def search_menu():
    print("1- Search Email")
    print("2- Search name")
    print("3- Search contact")
    print("4- Search address")

def get_data():
    search_menu()
    search_option = int(input("Enter search option"))
    if search_option == 1:
        search_email = input("Enter email to search: ")
        with open(path, 'r') as file: 
            data = json.load(file)
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
    elif search_option == 2:
        search_name = input("Enter name to search: ")
        with open(path, 'r') as file: 
            data = json.load(file)
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
    elif search_option == 3:
        search_contact = int(input("Enter contact to search: "))
        with open(path, 'r') as file: 
            data = json.load(file)
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
    elif search_option == 4:
        search_address = input("Enter address to search: ")
        with open(path, 'r') as file: 
            data = json.load(file)
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


