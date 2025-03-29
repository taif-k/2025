import json

listdata = []

for num in range(1,4):
    studentdata = {}
    qualificationlist = []
    studentdata["id"] = input("Enter id: ")
    studentdata["name"] = input("Enter name: ")
    studentdata["qualification"] = qualificationlist

    while True:
        qualificationdict = {}
        qualificationdict["qname"] =  input("Enter qualification: ")
        qualificationdict["passingyear"] = int(input("Enter passing year: "))
        qualificationlist.append(qualificationdict)

        ask_qualification = input("Add More qualification - y or n: ")
        
        if ask_qualification.lower() != "y":
            break


    listdata.append(studentdata)
    
print(json.dumps(listdata,indent=4))





import json

# listdata = []
# for num in range(1, 4):
#     studentdata = {}
    
#     qualificationlist = []
#     studentdata["id"] = input("Enter id")
#     studentdata["name"] = input("Enter name: ")
#     studentdata["qualification"] = qualificationlist
    
#     while True:
#         qualificationdict = {}
#         qualificationdict["qname"] = input("Enter qualification: ")
#         qualificationdict["passingyear"] = int(input("Enter passing year: "))
#         qualificationlist.append(qualificationdict)
        
#         ask_qualification = input("Add more qualifications (y/n): ")
#         if ask_qualification.lower() != 'y':
#             break

#     listdata.append(studentdata)
    

# print(json.dumps(listdata, indent=4))

   

                


            
            
        
                       
              

