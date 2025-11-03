import pandas as pd, json
from pandas import json_normalize


# null in JSON → becomes None in Python

# dropna() doesn’t always catch None in object columns; it mainly detects np.nan or pd.NA.
# For nested JSON normalized with json_normalize, object columns often have None instead of NaN.
# Always convert None → np.nan or use notna() condition before dropping rows.


# json_normalize 
    # flattens that nested JSON, turning it into columns/ Normalize semi-structured JSON data into a flat table.
def json_normalization():
    data1 = [{'created_epoch': '1138390973000', 'enumeration_type': 'NPI-1', 'last_updated_epoch': '1698463706000', 'number': '1932170057', 'addresses': [{'country_code': 'US', 'country_name': 'United States', 'address_purpose': 'MAILING', 'address_type': 'DOM', 'address_1': 'PO BOX 5074', 'city': 'SIOUX FALLS', 'state': 'SD', 'postal_code': '571175074', 'telephone_number': '605-328-9419'}, {'country_code': 'US', 'country_name': 'United States', 'address_purpose': 'LOCATION', 'address_type': 'DOM', 'address_1': '3035 DEMERS AVE', 'city': 'GRAND FORKS', 'state': 'ND', 'postal_code': '582014040', 
'telephone_number': '701-746-7521', 'fax_number': '701-795-2553'}], 'practiceLocations': [], 'basic': {'first_name': 'DAVID', 'last_name': 'SCHALL', 'middle_name': 'M', 'credential': 'MD', 'sole_proprietor': 'NO', 'sex': 'M', 'enumeration_date': '2006-01-27', 'last_updated': '2023-10-27', 'certification_date': '2023-10-27', 'status': 'A', 'name_prefix': 'Dr.'}, 'taxonomies': [{'code': '207X00000X', 'taxonomy_group': '', 'desc': 'Orthopaedic Surgery', 'state': 'MN', 'license': '41071', 'primary': False}, {'code': '207X00000X', 'taxonomy_group': '', 'desc': 'Orthopaedic Surgery', 'state': 'ND', 'license': '9038', 'primary': True}], 'identifiers': [{'code': '01', 'desc': 'Other (non-Medicare)', 'issuer': 'NDBCBS', 'identifier': '021872', 'state': 'ND'}, {'code': '05', 'desc': 'MEDICAID', 'issuer': None, 'identifier': 
'11989', 'state': 'ND'}, {'code': '05', 'desc': 'MEDICAID', 'issuer': None, 'identifier': '200001954', 'state': 'MN'}, {'code': '01', 'desc': 'Other (non-Medicare)', 'issuer': 'RR MEDICARE', 'identifier': '200045181', 'state': None}, {'code': '01', 'desc': 'Other (non-Medicare)', 'issuer': 'BCBS MN', 'identifier': '62G05SC', 'state': 'MN'}], 'endpoints': [], 'other_names': []}]


    print("Before normalization")
    print(json.dumps(data1,indent=3)) # orient options: split, index, columns, values
    print()


    print("After normalization")
    print(json_normalize(data1).to_json(orient='records', indent=3))


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

    # # meta takes str or list of str to keep apart from record_path, record_path will flatten contacts 
    # print(json_normalize(data2,meta=['name', 'age'],record_path='contacts'))


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

    # print(df.dropna(subset='Roll no')) # after that dropping NaN value



json_normalization()

# drop_duplicates
def duplicate_drop():
    print()
    print("drop_duplicates")

    duplicate_data = {
    'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
    'style': ['cup', 'cup', 'cup', 'pack', 'pack'],
    'rating': [4, 4, 3.5, 15, 5]
    }
    df = pd.DataFrame(duplicate_data)
    print("BEFRE DROPPING DUPLICATES")
    print(df)
    print("AFTER DROPPING DUPLICATES")
    print(df.drop_duplicates(subset='brand',keep='last')) # subset is used for column, keep takes 'last'/'first(which value to keep)

# duplicate_drop()


# CONCAT
    # series is a single column Created from list, dict, array.
    # DataFrame is collection of Series Created from dict of lists or Series. 
def concat_df():
    print("DATAFRAME")
    s1 = pd.DataFrame(['a', 'b'], columns=["column_name_default_0"])
    print(f"    {s1}")
    s2 = pd.DataFrame(['c', 'd'],columns=["column_name_default_0"])
    # s2["second_col_name"] = ["x",None]
    print(f"    {s2}")

    print()
    print("SERIES")
    s3 = pd.Series(['e', 'f'])
    print(f"{s3}")
    s4 = pd.Series(['g', 'h'])
    s4["m"] = {"zyx", "123"}
    s4["m"] = ["zyx", "123"]
    s4["m"] = "next_val"
    print(f"{s4}")

    print(pd.concat([s1, s2])) 
    

# concat_df()
