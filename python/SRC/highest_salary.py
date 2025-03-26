salaries = [10000,10000,10000,10000]


if salaries[0] >= 10000:
        salaries[0] = int(input("Enter salary 1: "))
else:
    print("salary should be more than or equal to 10,000 ")

if salaries[1] >= 10000:
    salaries[1] = int(input("Enter salary 2: "))
else:
    print("salary should be more than or equal to 10,000 ") 

if salaries[2] >= 10000:
    salaries[2] = int(input("Enter salary 3: "))
else:
    print("salary should be more than or equal to 10,000 ") 

if salaries[3] >= 10000:
    salaries[3] = salaries.append(int(input("Enter salary 4: ")))
else:
    print("salary should be more than or equal to 10,000 ")          
    
print(salaries)
