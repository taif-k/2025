path = r"C:\Users\DELL\Desktop\pandastest.xlsx"
import pandas as pd

exceldata = pd.read_excel(path,sheet_name="Sheet1")
print(pd.DataFrame(exceldata))
