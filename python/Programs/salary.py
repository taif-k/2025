salaries = []

for salary in range(0,4):
    sal = (input("Enter salary: "))
    if sal.isdigit():
        sal = int(sal)
        if sal >=10000:
            dict = {}
            dict["id"] = int(input("Enter id: "))
            salaries.append(dict) 
            salaries.append(sal)
        else:
            print("Salary should be minimum 10,000")
    else:
        print("Salary should be in digits")        


print(salaries)
    

