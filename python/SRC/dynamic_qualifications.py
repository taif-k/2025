import json

listdata = [] # {studentdata (k,v)}, {studentdata (k,v)}, {studentdata (k,v)}
qualificationlist = [] # qualificationdict

for num in range(1,3):
    studentdata = {}

    studentdata["id"] = num
    studentdata["name"] = input("Enter name: ")
    studentdata["qualification"] = qualificationlist
    for q in range(1,3):
        qualificationdict = {}
        qualificationdict["qname"] = input("Enter qualification: ")
        qualificationdict["passingyear"] = int(input("Enter passing year: "))
        ask_qualification = input("Add More qualification - y or n: ")
        if ask_qualification.lower() == "y":
            continue
        else:
            break 
    qualificationlist.append(qualificationdict)
    listdata.append(studentdata)

print(json.dumps(listdata,indent=4))    


qualification_search = input("Enter qualification to search: ")
not_present = True

for dict in listdata: # {}, {}
    for key in dict.keys(): # id: name: qualification:
        if key == "qualification":
             for d in qualificationlist: # qualificationdict qualificationdict
                  for value in d.values(): # qname: passingyear:
                       if value == qualification_search:
                            print("Names: ",dict["name"])
                       else:
                            not_present = False
                       
if not_present == True:
        print("qualification not present")                

