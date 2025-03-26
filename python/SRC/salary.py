salaries = []


salary1 = input("Enter salary 1: ")
if salary1.isdigit():
        salary1 = int(salary1)
        if salary1 >=10000:
            salaries.append(salary1) 
            
        else:
            print("Enter more than or equal to 10,000")
else:
    print("Enter salary in Digits Only")


salary2 = input("Enter salary 2: ")
if salary2.isdigit():
    salary2 = int(salary2)
    if salary2 >=10000:
        salaries.append(salary2)    
    else:
        print("Enter more than or equal to 10,000")
else:
    print("Enter salary in Digits Only")


salary3 = input("Enter salary 3: ")
if salary3.isdigit():
    salary3 = int(salary3)
    if salary3 >=10000:
            salaries.append(salary3)
    else:
        print("Enter more than or equal to 10,000")    
else:
    print("Enter salary in Digits Only")


salary4 = input("Enter salary 4: ")
if salary4.isdigit():
    salary4 = int(salary4)
    if salary4 >=10000:
        salaries.append(salary4)       
    else:
        print("Enter higher salary")       

salaries.sort()
print("Two Highest salaries are ",salaries[2:])    






