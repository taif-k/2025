import json

listdata = []
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
    
    percentage = (marksdict["hindi"] + marksdict["english"] + marksdict["math"] + marksdict["science"])/400 * 100
    print(percentage)
    
print(json.dumps(listdata,indent=3))


                


            
            
        
                       
              

