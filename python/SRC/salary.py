salaries = []


salary = input("Enter salary 1: ")
if salary.isdigit():
        salary = int(salary)
        if salary >=10000:
            salaries.append(salary) 
            
        else:
            print("Enter more than or equal to 10,000")
else:
    print("Enter salary in Digits Only")


salary = input("Enter salary 2: ")
if salary.isdigit():
    salary = int(salary)
    if salary >=10000:
        salaries.append(salary)    
    else:
        print("Enter more than or equal to 10,000")
else:
    print("Enter salary in Digits Only")


salary = input("Enter salary 3: ")
if salary.isdigit():
    salary = int(salary)
    if salary >=10000:
            salaries.append(salary)
    else:
        print("Enter more than or equal to 10,000")    
else:
    print("Enter salary in Digits Only")


salary = input("Enter salary 4: ")
if salary.isdigit():
    salary = int(salary)
    if salary >=10000:
        salaries.append(salary)       
    else:
        print("Enter higher salary")       

salaries.sort(reverse=True)
print("Two Highest salaries are ",salaries[:2])    






