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


qualification_search = input("Enter qualification to search")
not_present = True

for dict in listdata:
    for key,value in dict.items():
        if key == "qualification":
             for d in qualificationlist:
                  for keys,values in d.items():
                       if keys == "qname":
                            print(dict["name"])
                       
              
            

if not_present == False:
        print("qualification not present")                

