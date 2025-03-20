import json

studentdict = {}
studentqualification = {}
qualificationlist = []

studentskills = []

studentdict["studentid"] = int(input("Enter id: "))
studentdict["studentname"] = input("Enter name: ")
studentdict["experience"] = input("Enter experience: ")
studentdict["skills"] = studentskills
studentdict["Qualification"] = qualificationlist

studentskills.append(input("Enter 1st skill: "))
studentskills.append(input("Enter 2nd skill: "))
studentskills.append(input("Enter 3rd skill: "))

studentqualification["name"] = input("Enter qualification: ")
studentqualification["passingyear"] = input("Enter passing year: ")
qualificationlist.append(studentqualification)
studentqualification = {}
studentqualification["name"] = input("Enter qualification: ")
studentqualification["passingyear"] = int(input("Enter passing year: "))
qualificationlist.append(studentqualification)
studentqualification = {}
studentqualification["name"] = input("Enter qualification: ")
studentqualification["passingyear"] = int(input("Enter passing year: "))
qualificationlist.append(studentqualification)
#//////////////////////////////////////////////////////////////////////////////
studentdict2 = {}
studentqualification = {}
qualificationlist = []

studentskills = []

studentdict2["studentid"] = int(input("Enter id: "))
studentdict2["studentname"] = input("Enter name: ")
studentdict2["experience"] = input("Enter experience: ")
studentdict2["skills"] = studentskills
studentdict2["Qualification"] = qualificationlist

studentskills.append(input("Enter 1st skill: "))
studentskills.append(input("Enter 2nd skill: "))
studentskills.append(input("Enter 3rd skill: "))

studentqualification["name"] = input("Enter qualification: ")
studentqualification["passingyear"] = input("Enter passing year: ")
qualificationlist.append(studentqualification) #

mainlist = [studentdict,studentdict]
print(json.dumps(mainlist,indent=4))

