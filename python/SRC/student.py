import json
students = {} 
qualificationdict = {}
listdata = []

students["id"] = int(input("Enter id: "))
students["name"] = input("Enter name: ")
students["address"] = input("Enter address: ")
students["contact"] = int(input("Enter contact: "))


qualificationdict["qulaificationname"] = "12th"
qualificationdict["passingyear"] = "2016"
listdata.append(qualificationdict)

qualificationdict["qulaificationname"] = "bca"
qualificationdict["passingyear"] = "2020"
listdata.append(qualificationdict)

qualificationdict["qulaificationname"] = "mca"
qualificationdict["passingyear"] = "2024"
listdata.append(qualificationdict)

students["qualifications"] = listdata




# # studentstr = f"""id: {studentdetails["id"]} \nname: {studentdetails["name"]} \naddress: {studentdetails["address"]} \ncontact: {studentdetails["contact"] } \nqualification: {studentdetails["qualification"]}"""   
# print(json.dumps(studentdetails,indent=4))
print(students)
# print(json.dumps(students,indent=4))
 






