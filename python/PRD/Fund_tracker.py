import pandas as pd
fund_excel_path = r"python/PRD/fund.xlsx"
fund_data = []

while True:
    print("\nEnter expense details:")
    category = input("Expense Category: ")
    estimated = float(input("Estimated Cost: "))
    actual = float(input("Actual Cost: "))
  
    diff = actual - estimated
    
    
    fund_data.append({"Expense Category": category,"Estimated Cost": estimated,"Actual Cost": actual,"diiference": diff})
    
    another_entry = input("Add another category y/n: ")
    if another_entry != "y":
        break

df = pd.DataFrame(fund_data)
df.to_excel(fund_excel_path, index=False)

