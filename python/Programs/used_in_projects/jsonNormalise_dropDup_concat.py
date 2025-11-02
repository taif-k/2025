import pandas as pd
from pandas import json_normalize

# json_normalize 
    # flattens that nested JSON, turning it into columns/ Normalize semi-structured JSON data into a flat table.
data1 = [
    {
    "name": "Alice",
    "age": 25,
    "address": {"city": "New York", "zip": "10001"}
}
]

print("Before normalization")
print(pd.DataFrame(data1))
print()


print("After normalization")
print(json_normalize(data1))

print()
data2 = [
    {
        "name": "Alice",
        "age": 25,
        "contacts": [
            {"type": "email", "value": "alice@email.com"},
            {"type": "phone", "value": "111-222"}
        ]
    },
    {
        "name": "Bob",
        "age": 30,
        "contacts": [
            {"type": "email", "value": "bob@email.com"}
        ]
    }
]

# meta takes str or list of str to keep apart from record_path, record_path will flatten contacts 
print(json_normalize(data2,meta=['name', 'age'],record_path='contacts'))


data3 = [
    {"Roll no": 1,
     "student": {"first_name": "Ram", "last_name": "kumar"}
     },
    {"student": {"English": "95", "Math": "88"}
     },
    {"Roll no": 2,
     "student": {"first_name": "Joseph", "English": "90", "Science": "82"}
     },
    {"Roll no": 3,
     "student": {"first_name": "abinaya", "last_name": "devi"},
     "student": {"English": "91", "Math": "98"}
     },
]
df = json_normalize(data3) # normalizing

print(df.dropna(subset='Roll no')) # after that dropping NaN value