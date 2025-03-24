student = {}

student["id"] = int(input("Enter id: "))
student["name"] = input("Enter name: ")
student["contact"] = int(input("Enter contact: "))

for keys,values in student.items():  # items is used here for both keys and values, for only keys or values use student.keys or student.values respectively.  
    print(f"""{keys}:{values}""")

for keys in student.items(): 
    print(f"""{keys}""") # output will be both keys and values in a tuple because items is unpacking keys and values in each key [key = (key,value)]
                         # use student.keys to het values of keys