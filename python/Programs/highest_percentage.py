import json

listdata = []
percentagelist = []

for num in range(1,3):
    studentdata = {}
    markslist = []
    marksdict = {}
    
    while True:
        studentdata["id"] = input("Enter id: ")
        if studentdata["id"].isdigit():
            break
        else:
            print("Enter id in digits only")
    while True:
            studentdata["name"] = input(f"Enter name {num}: ")
            if studentdata["name"].isalpha():
                
                studentdata["marks"] = markslist
                for m in range(0,4):
                    subject = ["hindi","english","math","science"]
                    m = subject[m]
                    while True:
                        marksdict[m] = input(f"Enter {m} marks: ")
                        if marksdict[m].isdigit():
                            marksdict[m] = int(marksdict[m])
                            if marksdict[m] >=0 and marksdict[m] <=100:
                                break
                            else:
                                print("Marks range should be 0 - 100")
                        else:
                            print("Marks should be in digits")
                            
                markslist.append(marksdict)
                break
            else:
                print("Enter valid name")
        

    percentage = (marksdict["hindi"] + marksdict["english"] + marksdict["math"] + marksdict["science"])/400 * 100
    percentagelist.append(percentage)
    listdata.append(studentdata)   
                
print(json.dumps(listdata,indent=3))
percentagelist.sort()
print(percentagelist)
print("Highest: ",percentagelist[-1])



            
            
        
                       
              

