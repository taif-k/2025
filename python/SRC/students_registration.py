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
studentqualification2 = {}
qualificationlist2 = []

studentskills2 = []

studentdict2["studentid"] = int(input("Enter id: "))
studentdict2["studentname"] = input("Enter name: ")
studentdict2["experience"] = input("Enter experience: ")
studentdict2["skills"] = studentskills2
studentdict2["Qualification"] = qualificationlist2

studentskills2.append(input("Enter 1st skill: "))
studentskills2.append(input("Enter 2nd skill: "))
studentskills2.append(input("Enter 3rd skill: "))

studentqualification2["name"] = input("Enter qualification: ")
studentqualification2["passingyear"] = input("Enter passing year: ")
qualificationlist2.append(studentqualification2) #

mainlist = [studentdict,studentdict2]
print(json.dumps(mainlist,indent=4))

