isActive = 1  # using a flag to check if else stats
id = int(input("Enter student id: "))
name = input("Enter student name: ")
dictionarydata = {"id":id,"name":name,"isActive":isActive}

if isActive == 1:
    print(f""" Id is: { dictionarydata["id"] } \n Name is: { dictionarydata["name"] } \n isActive value is: {dictionarydata["isActive"]}""")
   
else:
    print("\nvalue is false")