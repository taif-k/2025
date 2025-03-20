# data = {"id":132, "name": "taif"} 
# flag = "9" 

# setdata = {str(9),flag,9,data["name"],data["name"],tuple(data)} #we cannot directly use data dictionary in setdata set because it is unhashable, use tuple to aviod error
# print(setdata)


# # Set is collection of unique unordered data 

# # [{}] OK
# # {[]} NO


# # s1 = {1,2,3}
# # s2 = {2,4,5}
# # s3 = {s1,s2}
# # print(s3) # {{}} NO


setdata1 = {1,2,3,4}
# setdata1.add(6-1)
# setdata1.discard("string") # discard will not throw an error unlike remove, if the element is not present in set 
# setdata1.remove(2)
setdata1.pop() # when using pop in set it does not take any arg(index was passed as arg in list) but set is unordered so no index, pop in set will remove randomly

print(setdata1)