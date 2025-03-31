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
                marksdict = {}
                marksdict[m] = int(input(f"Enter {m} marks"))
                markslist.append(marksdict)

            listdata.append(studentdata)   
            # percentage = (marksdict[1] + marksdict[2] + marksdict[3] + marksdict[4])/400 * 100
            # percentagelist.append(percentage)
            # break
        else:
            print("Enter valid name ") 
        
            # while count == 0:
            #     marks = int(input("Enter Hindi marks (0 - 100): "))
            #     if marks >=0 and marks <=100:
            #         marksdict["hindi"] = marks
            #         while count == 0:
            #             marks = int(input("Enter English marks (0 - 100): "))
            #             if marks >=0 and marks <=100:
            #                 marksdict["english"] = marks
            #                 while count == 0:
            #                     marks = int(input("Enter Math marks (0 - 100): "))
            #                     if marks >=0 and marks <=100:
            #                         marksdict["math"] = marks
            #                         while count == 0:
            #                             marks = int(input("Enter Science marks (0 - 100): "))
            #                             if marks >=0 and marks <=100:
            #                                 marksdict["science"] = marks
            #                                 count = 1
          

    
        print(studentdata)
# print(json.dumps(listdata,indent=3))
# percentagelist.sort()
# print(percentagelist)
# print("Highest percentage is: ",percentagelist[-1])    


                


            
            
        
                       
              

