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
    count = 0
    while count == 0:
        marks = int(input("Enter Hindi marks (0 - 100): "))
        if marks >=0 and marks <=100:
            marksdict["hindi"] = marks
            while count == 0:
                marks = int(input("Enter English marks (0 - 100): "))
                if marks >=0 and marks <=100:
                    marksdict["english"] = marks
                    while count == 0:
                        marks = int(input("Enter Math marks (0 - 100): "))
                        if marks >=0 and marks <=100:
                            marksdict["math"] = marks
                            while count == 0:
                                marks = int(input("Enter Science marks (0 - 100): "))
                                if marks >=0 and marks <=100:
                                    marksdict["science"] = marks
                                    count = 1
    markslist.append(marksdict)
    listdata.append(studentdata)    
    percentagelist.append((marksdict["hindi"] + marksdict["english"] + marksdict["math"] + marksdict["science"])/400 * 100)
    
print(markslist)
print(json.dumps(listdata,indent=3))
percentagelist.sort()
print(percentagelist)
print("Highest percentage is: ",percentagelist[-1])    


                


            
            
        
                       
              

