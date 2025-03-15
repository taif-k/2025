
d1 = {1,2,3}
d2 = {9,9,9,"t"}
listdata = [d1,d2,9,9,"9"]
# print(listdata) 

# # only takes one arg, here we have removed d2, anything can be removed from anywhere in the list
print(listdata) 
listdata.pop(1) # pop takes index
print(listdata) 

# list2 = [8,9]
# set3 = {list2[1],9}  # there will be type error is we pass list in set, but we can pass list2[index] in set
# # print(set3)

# list can have duplicate data and it is in ordered(sequence), it is in sequence so we can use index 

# [{}] OK
# {[]} NO