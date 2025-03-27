# student = {}

# student["id"] = int(input("Enter id: "))
# student["name"] = input("Enter name: ")
# student["contact"] = int(input("Enter contact: "))

# for keys,values in student.items():  # items is used here for both keys and values, for only keys or values use student.keys or student.values respectively.  
#     print(f"""{keys}:{values}""")

# for keys in student.items(): 
#     print(f"""{keys}""") # iterating over car.items(), but unpacking the key-value tuple, means key will hold the entire tuple (key, value).  
#                          # use student.keys to het values of keys


namelist = ["taif","sumit","srishti","sheetal"]

not_present = True

for name in namelist:
    if name == "fi":
        print(f"{name} is present")
        break
    else:
        not_present = False

if not_present == False:
    print("Not present")        


