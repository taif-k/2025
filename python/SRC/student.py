print("Enter student details")
id = int(input("Enter id: "))
name = input("Enter name: ")
address = input("Enter address: ")
contact = int(input("Enter contact: "))


studentdetails = {"id":id,"name":name,"address":address,"contact":contact}
studentstr = f""" Student is is: {studentdetails["id"]} \n Student name is: {studentdetails["name"]} \n student address is: {studentdetails["address"]} \n student contact is: {studentdetails["contact"]}"""
print(studentstr)
