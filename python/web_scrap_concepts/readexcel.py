import pandas as pd
path = r"D:\Repositories\2025\python\web_scrap_concepts\npi_data.xlsx"

exceldata = pd.read_excel(path,sheet_name="Sheet1")
print(pd.DataFrame(exceldata))
