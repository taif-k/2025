student = {}

student["id"] = 123 #int(input("Enter id: "))
student["name"] = "taif" #input("Enter name: ")
student["contact"] = 7827639909 #int(input("Enter contact: "))

for keys,values in student.items():
    if keys == "name":
        if values == "taif":
            print("key is matched with value")


namelist = ["taif","sumit","srishti","sheetal"]
print(namelist)

not_present = True
name_input = input("Enter name: ")

for name in namelist:
    if name == name_input:
        print(f"{name} is present")
        break
    else:
        not_present = False

if not_present == False:
    print("Entered name is present")        


