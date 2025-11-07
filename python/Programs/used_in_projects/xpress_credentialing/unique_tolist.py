import pandas as pd

data = [{'name': 'abc'},{'name': 'abc'}]
a = pd.DataFrame(data)

# unique() in pandas is similar to set() in python - unique keeps appearance order unlike set 
print(a['name'].unique(), type(a['name'].unique()), a['name'].dtype)
print(a['name'].unique().tolist(), type(a['name'].unique().tolist()))
# print(a['name'].unique().tolist().dtype) # now series has become list so dtype wont work on it  