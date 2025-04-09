
import create_file
import json

def register_user():
    studentlist = []
    for n in range(1,3):
        studentdict = {} 
        studentdict["id"] = int(input("Enter id: "))
        studentdict["name"] = input("Enter name: ")
        studentlist.append(studentdict)
        jsondata = json.dumps(studentdict,indent=3)

        create_file.create_userfile(studentdict,jsondata)
    print(studentlist)   