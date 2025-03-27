salaries = []

for salary in range(0,4):
    sal = (input("Enter salary: "))
    if sal.isdigit():
        sal = int(sal)
        if sal >=10000: 
            salaries.append(sal)
        else:
            print("Salary should be minimum 10,000")
    else:
        print("Salary should be in digits")        

salaries.sort(reverse=True)    
print("salary in descending order",salaries)
    

