import pandas as pd, json
from pandas import json_normalize
                                   # iterrows
data = [{'created_epoch': '1138390973000', 'enumeration_type': 'NPI-1', 'last_updated_epoch': '1698463706000', 'number': 123, 'addresses': [{'country_code': 'US', 'country_name': 'United States', 'address_purpose': 'MAILING', 'address_type': 'DOM', 'address_1': 'PO BOX 5074', 'city': 'SIOUX FALLS', 'state': 'SD', 'postal_code': '571175074', 'telephone_number': '605-328-9419'}, {'country_code': 'US', 'country_name': 'United States', 'address_purpose': 'LOCATION', 'address_type': 'DOM', 'address_1': '3035 DEMERS AVE', 'city': 'GRAND FORKS', 'state': 'ND', 'postal_code': '582014040', 
'telephone_number': '701-746-7521', 'fax_number': '701-795-2553'}], 'practiceLocations': [], 'basic': {'first_name': 'DAVID', 'last_name': 'SCHALL', 'middle_name': 'M', 'credential': 'MD', 'sole_proprietor': 'NO', 'sex': 'M', 'enumeration_date': '2006-01-27', 'last_updated': '2023-10-27', 'certification_date': '2023-10-27', 'status': 'A', 'name_prefix': 'Dr.'}, 'taxonomies': [{'code': '207X00000X', 'taxonomy_group': '', 'desc': 'Orthopaedic Surgery', 'state': 'MN', 'license': '41071', 'primary': False}, {'code': '207X00000X', 'taxonomy_group': '', 'desc': 'Orthopaedic Surgery', 'state': 'ND', 'license': '9038', 'primary': True}], 'identifiers': [{'code': '01', 'desc': 'Other (non-Medicare)', 'issuer': 'NDBCBS', 'identifier': '021872', 'state': 'ND'}, {'code': '05', 'desc': 'MEDICAID', 'issuer': None, 'identifier': 
'11989', 'state': 'ND'}, {'code': '05', 'desc': 'MEDICAID', 'issuer': None, 'identifier': '200001954', 'state': 'MN'}, {'code': '01', 'desc': 'Other (non-Medicare)', 'issuer': 'RR MEDICARE', 'identifier': '200045181', 'state': None}, {'code': '01', 'desc': 'Other (non-Medicare)', 'issuer': 'BCBS MN', 'identifier': '62G05SC', 'state': 'MN'}], 'endpoints': [], 'other_names': []
},{'created_epoch': '1138390973000', 'enumeration_type': 'NPI-1', 'last_updated_epoch': '1698463706000', 'number': '456', 'addresses': [{'country_code': 'US', 'country_name': 'United States', 'address_purpose': 'MAILING', 'address_type': 'DOM', 'address_1': 'PO BOX 5074', 'city': 'SIOUX FALLS', 'state': 'SD', 'postal_code': '571175074', 'telephone_number': '605-328-9419'}, {'country_code': 'US', 'country_name': 'United States', 'address_purpose': 'LOCATION', 'address_type': 'DOM', 'address_1': '3035 DEMERS AVE', 'city': 'GRAND FORKS', 'state': 'ND', 'postal_code': '582014040', 
'telephone_number': '701-746-7521', 'fax_number': '701-795-2553'}], 'practiceLocations': [], 'basic': {'first_name': 'JOE', 'last_name': 'M', 'middle_name': 'M', 'credential': 'MD', 'sole_proprietor': 'NO', 'sex': 'M', 'enumeration_date': '2006-01-27', 'last_updated': '2023-10-27', 'certification_date': '2023-10-27', 'status': 'A', 'name_prefix': 'Dr.'}, 'taxonomies': [{'code': '207X00000X', 'taxonomy_group': '', 'desc': 'Orthopaedic Surgery', 'state': 'MN', 'license': '41071', 'primary': False}, {'code': '207X00000X', 'taxonomy_group': '', 'desc': 'Orthopaedic Surgery', 'state': 'ND', 'license': '9038', 'primary': True}], 'identifiers': [{'code': '01', 'desc': 'Other (non-Medicare)', 'issuer': 'NDBCBS', 'identifier': '021872', 'state': 'ND'}, {'code': '05', 'desc': 'MEDICAID', 'issuer': None, 'identifier': 
'11989', 'state': 'ND'}, {'code': '05', 'desc': 'MEDICAID', 'issuer': None, 'identifier': '200001954', 'state': 'MN'}, {'code': '01', 'desc': 'Other (non-Medicare)', 'issuer': 'RR MEDICARE', 'identifier': '200045181', 'state': None}, {'code': '01', 'desc': 'Other (non-Medicare)', 'issuer': 'BCBS MN', 'identifier': '62G05SC', 'state': 'MN'}], 'endpoints': [], 'other_names': []
}]


df =  pd.DataFrame(data)
# print(df.to_json(indent=3))

df_flatten = json_normalize(data)
# print(df_flatten.to_json(indent=3))

df_flatten["number"] = df_flatten["number"].astype("string") # converting npi(number as string) before loop(after that it iterates on copy and not ref.) 
# iterrows() returns a copy of each row, not a reference to the DataFrame. 

# for _, record in df.iterrows():
for _, record in df_flatten.iterrows(): # flatten nested json first
    # df_flatten["number"] = df_flatten["number"].astype("string") # this is wrong 
    npi_number = record["number"]
    first_name = record.get("basic.first_name", None)
    last_name = record.get("basic.last_name", None)
    # print(f"Npi: {npi_number} TYPENPI: {type(npi_number)} Fname: {first_name} Lname: {last_name}")
    print(record.get("basic.first_name"))

    
for record in df_flatten.itertuples(): 
    # pass
    print(record)
 
    
                                      # isinstance
py_list = []
list_as_str = "[]"
print(isinstance(py_list,list))
print(isinstance(list_as_str,str))

                                    # ast.literal_eval()
import ast
anything_but_string = "[]"
# print(eval(anything_but_string), type(eval(anything_but_string))) # eval() can run arbitary code also

# safer version 
print(type(ast.literal_eval(anything_but_string)))


s = "{'a': 1, 'b': 2}"  
# d = json.loads(s) # when using loads json prperty should be in double qoutes otherwise its an err but literal_eval() can handle this
d = ast.literal_eval(s)
print(d)  

