import json

listdata = []
for num in range(1,4):
    studentdata = {}
    qualificationlist = []
    studentdata["id"] = num + 100
    studentdata["name"] = input("Enter name: ")
    studentdata["qualification"] = qualificationlist
    for q in range(1,3):
        qualificationdict = {}
        qualificationdict["qname"] = input("Enter qualification: ")
        qualificationdict["passingyear"] = int(input("Enter passing year: "))
        qualificationlist.append(qualificationdict)
        ask_qualification = input("Add More qualification - y or n: ")
        if ask_qualification.lower() == "y":
            continue
        else:
            break 

    listdata.append(studentdata)

print(json.dumps(listdata,indent=4))
for x in range(1,10000000):
    qualification_search = input("Enter qualification to search: ")
    if qualification_search.isalpha():
        for d in listdata:
            for keys in d.keys():
                if keys == "qualification":
                    for n in qualificationlist:
                        for value in n.values():
                            if value == qualification_search:
                                print(d["name"])
        break
    else:
        print("Enter valid Qualification")

                


            
            
        
                       
              

