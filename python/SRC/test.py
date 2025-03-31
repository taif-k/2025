import json

listdata = []
percentagelist = []

for num in range(1,3):
    studentdata = {}
    markslist = []
    marksdict = {}
    count = 0

    studentdata["id"] = num + 100
    while True:
        studentdata["name"] = input(f"Enter name {num}: ")
        if studentdata["name"].isalpha():

            studentdata["marks"] = markslist
            for m in range(0,4):
                sub = ["hindi","english","math","science"]
                m = sub[m]
                marksdict[m] = int(input(f"Enter {m} marks"))
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

  


                


            
            
        
                       
              

