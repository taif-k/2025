import json
import pandas

path = r"D:\Repositories\2025\python\Students_Record_System\Src\Database\all_students.json"

with open(path,"r") as f:
    data = json.load(f)

matrix_data = pandas.DataFrame(data)

print(matrix_data)

