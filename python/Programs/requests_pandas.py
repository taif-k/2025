# import requests
# import json
import pandas
path = r"D:\filetereddata\data.json"

# response = requests.get("https://api.sampleapis.com/coffee/hot")
# data = response.json()
# # print(json.dumps(data,indent=4))

# print(pd.__version__)


data = {
    "Plan": ["A", "B", "C"],
    "Premium": [3000, 7000, 4500]
}

matrix_data = pandas.DataFrame(data)
# matrix_data.head()  first 5 rows
output = matrix_data[matrix_data["Premium"] < 5000]
output.to_json(path, orient="records", indent=3)


print(matrix_data["Premium"])
