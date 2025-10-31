import pandas as pd

# dropna()
# dropna() removes row which has (NaN / None) from a pandas DataFrame or Series.


# args of dropna()
    # 1 axis = 0(row direction drop)(default) / 1(column direction drop)
    # 2 how = "all" (All value should be None)/ "any" (if any None is there)(default)
    # 3 thresh = n (n is atleast n non None value) Ex: thresh = 2


# THRESH
print("*************THRESH*************")
thresh_data = { # when making df with dict no need to manually assign col key becomes column names 
    "Name": ["Alice", "Bob", "Cristy", "David"],
    "Age": [None, 20, 18, 22],
    "City": [None, "LA", "TX", "FL"]
}
# Atleast 2(n) Non None values in a row
print(pd.DataFrame(thresh_data).dropna(thresh=2))  






# AXIS
print("*************AXIS*************")
axis_data = { 
    "Name": ["Alice", "Bob", "Cristy", "David"],
    "Age": [None, 20, 18, 22],
    "City": [None, "LA", "TX", "FL"]
}
# axis=0 (row, also default) and axis = 1(column)
print(pd.DataFrame(axis_data).dropna(axis=1)) 






# HOW 
print("*************HOW**************")
how_data = { 
    "Name": ["Alice", "Bob", "Cristy", "David"],
    "Age": [None, 20, 18, 22],
    "City": [None, "LA", "TX", "FL"]
}
# how takes 'any' (default) and all. if any None is present it will work, when using all all has to be None to be dropped. 
print(pd.DataFrame(how_data).dropna(how='any')) 






# SUBSET
print(f"*************SUBSET*************")
subset_data = { 
    "Name": ["Alice", "Bob", "Cristy", "David"],
    "Age": [None, 20, 18, 22],
    "City": [None, "LA", "TX", "FL"]
}
# criteria for drop is Age here if for any Age is None that will be dropped
print(pd.DataFrame(subset_data).dropna(subset='Age')) 








data = [ # when making df with list, need to manually assign col key
    ["Alice", 25, "NY"],
        # ["Alice", 25], # it will not cause error unlike when using dict
    ["Bob", None, "LA"],
    [None, 30, "SF"],
    ["David", 22, None]
]

print(pd.DataFrame(data,columns=["Name", "Age", "City"]))
print(pd.DataFrame(data).dropna())