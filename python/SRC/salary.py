salaries = []


salary = input("Enter salary 1: ")
if salary.isdigit():
        salary = int(salary)
        if salary >=10000 and salary <=100000:
            salaries.append(salary) 
            
        else:
            print("Enter salary between 10,000 and 1,00,000")
else:
    print("Enter salary in Positive numbers Only")


salary = input("Enter salary 2: ")
if salary.isdigit():
    salary = int(salary)
    if salary >=10000 and salary <=100000:
        salaries.append(salary)    
    else:
        print("Enter salary between 10,000 and 1,00,000")
else:
    print("Enter salary in Positive numbers Only")


salary = input("Enter salary 3: ")
if salary.isdigit():
    salary = int(salary)
    if salary >=10000 and salary <=100000:
            salaries.append(salary)
    else:
        print("Enter salary between 10,000 and 1,00,000")    
else:
    print("Enter salary in Positive numbers Only")


salary = input("Enter salary 4: ")
if salary.isdigit():
    salary = int(salary)
    if salary >=10000 and salary <=100000:
        salaries.append(salary)       
    else:
        print("Enter higher salary")       

salaries.sort(reverse=True)
print("Two Highest salaries are ",salaries[:2])    






