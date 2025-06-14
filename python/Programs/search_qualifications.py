import json
listdata = []
for num in range(1,4):
    studentdata = {}
    qualificationlist = []
    studentdata["id"] =  num
    studentdata["name"] = input("Enter name: ")
    studentdata["qualification"] = qualificationlist

    while True:
        qualificationdict = {}
        qualificationdict["qname"] =  input("Enter qualification: ")
        qualificationdict["passingyear"] = input("Enter passing year")
        qualificationlist.append(qualificationdict)

        ask_qualification = input("Add More qualification - y or n: ")
        
        if ask_qualification.lower() != "y":
            break

    listdata.append(studentdata)
    
print(json.dumps(listdata,indent=4))

while True:
    qualification_search = input("Enter qualification to search: ")
    if qualification_search.isalnum():
        ispresent = False
        for d in listdata:
            for qualification in d["qualification"]:
                if qualification_search.lower() == qualification["qname"].lower():
                    print(f"""Student Name: {d["name"]}""")
                    ispresent = True
        if ispresent == False:
            print("qualification not found")
        break
    else:
        print("Enter valid qualification: ")

        


   

                


            
            
        
                       
              

