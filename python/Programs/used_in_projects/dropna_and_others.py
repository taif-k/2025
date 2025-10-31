# dropna
# dropna() removes row which has (NaN / None) from a pandas DataFrame or Series.

import pandas as pd


# when making df with dict no need to manually assign col key becomes column names
data = {
    "Name": ["Alice", "Bob", None, "David"],
    # "Name": ["Alice", "Bob", None], # this will cause error because all ararys ,ust be of same length but it not same with list
    "Age": [25, None, 30, 22],
    "City": ["NY", "LA", "SF", None]
}

print(pd.DataFrame(data))
print(pd.DataFrame(data).dropna())

# when making df with list, need to manually assign col key 
data = [
    ["Alice", 25, "NY"],
        # ["Alice", 25], # it will not cause error unlike when using dict
    ["Bob", None, "LA"],
    [None, 30, "SF"],
    ["David", 22, None]
]

print(pd.DataFrame(data,columns=["Name", "Age", "City"]))
print(pd.DataFrame(data).dropna())