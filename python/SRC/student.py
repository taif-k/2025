id = int(input("Enter id: "))
name = input("Enter name: ")
address = input("Enter address: ")
contact = int(input("Enter contact: "))
qualification = input("Enter qualification: ")


studentdetails = {"id":id,"name":name,"address":address,"contact":contact,"qualification":qualification}
studentstr = f"""id: {studentdetails["id"]} \nname: {studentdetails["name"]} \naddress: {studentdetails["address"]} \ncontact: {studentdetails["contact"] } \nqualification: {studentdetails["qualification"]}"""
print("\n---student details---")
print(studentstr)
