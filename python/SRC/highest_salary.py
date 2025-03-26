salaries = []

salary1 = int(input("Enter salary 1: "))
if salary1 >=10000:
    salaries.append(salary1)  
   

salary2 = int(input("Enter salary 2: "))
if salary2 >=10000:
    salaries.append(salary2)

salary3 = int(input("Enter salary 3: "))
if salary3 >=10000:
    salaries.append(salary3)  

salary4 = int(input("Enter salary 4: "))
if salary4 >=10000:
    salaries.append(salary4)      


salaries.sort()
print(salaries[1:])    






