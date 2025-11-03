import pandas as pd, numpy as np

print("astype()")
data = [
    {"id": 123},
    {"id":456}
]

df = pd.DataFrame(data)
print(f"1st print: {df.dtypes}") # 1
df["id"] = df["id"].astype("string") # new version when using "string" it doesnt store str as object
# df["id"] = df["id"].astype(str) 
print(f"2nd print: {df.dtypes}") # 2



print()
print("isin()")
not_done = [123,456]

data2 = [{
    "num": 123
},{
    "num": 456
},{
    "num": 789
}]

check_isin = pd.DataFrame(data2)
do_now = check_isin[check_isin["num"].isin(not_done)] # return boolean
print(do_now)


# array_split numpy
spliting_arr =  np.array_split(do_now,2)
print(spliting_arr[0])
print(spliting_arr[1])
print(type(spliting_arr[1]))

