student = {}

while True:
    student_id = input("Enter id: ")
    if student_id.isdigit():
      student["id"] = student_id

      while True:
          student_name = input("Enter name: ")
          if student_name.isalpha():
               student["name"] = student_name

               while True:
                   student_contact = input("Enter contact: ")
                   if student_contact.isdigit():
                       student["contact"] = student_contact
                       break
                   else:
                       print("Enter only numbers") 
               break                 
          else:
              print("Enter only alphabets")  
      break                    
    else:
      print("Enter only digits")
    

for keys,values in student.items():  # items is used here for both keys and values, for only keys or values use student.keys or student.values respectively.  
    print(f"""{keys} is {values}""")

# for keys in student.items(): 
    # print(f"""{keys}""") # iterating over car.items(), but unpacking the key-value tuple, means key will hold the entire tuple (key, value).  
                         # use student.keys to het values of keys