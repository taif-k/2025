import json

listdata = []
percentagelist = []

for num in range(1,3):
    studentdata = {}
    markslist = []
    

    studentdata["id"] = num + 100
    studentdata["name"] = input("Enter name: ")
    studentdata["marks"] = markslist
    
    marksdict = {}
    marksdict["hindi"] = int(input("Enter Hindi marks: "))
    marksdict["english"] = int(input("Enter English marks: "))
    marksdict["math"] = int(input("Enter Math marks: "))
    marksdict["science"] = int(input("Enter science marks: "))
    markslist.append(marksdict)
    listdata.append(studentdata)
    
    percentagelist.append((marksdict["hindi"] + marksdict["english"] + marksdict["math"] + marksdict["science"])/400 * 100)
    

# print(json.dumps(listdata,indent=3))
percentagelist.sort()
print(percentagelist)
print("Highest percentage is: ",percentagelist[-1])    

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


                


            
            
        
                       
              

