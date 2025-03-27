listdata = []

for num in range(1,6):
    studentdata = {}
    studentdata["id"] = num
    studentdata["name"] = input("Enter name: ")
    studentdata["address"] = input("Enter address: ")
    studentdata["contact"] = int(input("Enter contact: "))
    studentdata["email"] = input("Enter email: ")
    listdata.append(studentdata)

print(listdata)    

contact_input = int(input("Enter contact to search"))


not_present = True

for dict in listdata:
    for key,value in dict.items():
        if key == "contact":
            if value == contact_input:
                print(dict)
            else:
                not_present = False

if not_present == False:
        print("Contact not present")                

