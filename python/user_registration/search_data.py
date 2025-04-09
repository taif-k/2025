import json

def search_type():
    print("1 - search from email")
    print("2 - search from name")
    print("3 - search from contact")
    print("4 - search from adress")

def get_data(datalist):
    print(json.dumps(datalist,indent=3))
    while True:
        search_type()
        search_option = int(input("Enter search option number: "))
        if search_option == 1:
            ispresent = False
            search_email = input("\nEnter email to search: ")
            for list in datalist:
                for key,value in list.items():
                    if value == search_email:
                        ispresent = True
                        # print(list)
            if ispresent == True:
                print(list)     
            else:
                print("email not present")
        elif search_option == 2:
            ispresent = False
            search_name = input("\nEnter name to search: ")
            for list in datalist:
                for key,value in list.items():
                    if value == search_name:
                        ispresent = True
                        # print(list)
            if ispresent == True:
                print(list)     
            else:
                print("name not present")
        elif search_option == 3:
            ispresent = False
            search_contact = input("\nEnter contact to search: ")
            for list in datalist:
                for key,value in list.items():
                    if value == search_contact:
                        ispresent = True
                        # print(list)
            if ispresent == True:
                print(list)     
            else:
                print("contact not present")
        elif search_option == 4:
            ispresent = False
            search_address = input("\nEnter Address to search: ")
            for list in datalist:
                for key,value in list.items():
                    if value == search_address:
                        ispresent = True
                        # print(list)
            if ispresent == True:
                print(list)     
            else:
                print("Address not present")

       


                

