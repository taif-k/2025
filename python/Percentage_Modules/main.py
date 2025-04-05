import studentid
import studentname
import studentmarks
import json

def percentage():
    listdata = []
    percentagelist = []
    for num in range (1,3):
        studentdict = {}
        studentdict["id"] = studentid.student_id(studentdict)
        studentdict["name"] = studentname.student_name(studentdict)
        marks, percentages = studentmarks.student_marks(studentdict)    
        studentdict["marks"] = marks  
        listdata.append(studentdict)

        percentagelist.append(percentages[0])

    print(json.dumps(listdata, indent=3))
    
    percentagelist.sort()
    print(f"Sorted Percentages: {percentagelist}")
    
    if percentagelist:
        print("Highest Percentage: ", percentagelist[-1])
    
    return listdata  

percentage()
