
def input_marks(studentdata):
    markslist = []
    marksdict = {}    
    percentagelist = []

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
                
    percentage = (marksdict["hindi"] + marksdict["english"] + marksdict["math"] + marksdict["science"])/400 * 100
    percentagelist.append(percentage)                   
    markslist.append(marksdict)
    return markslist,percentagelist