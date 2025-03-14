data = {"id":132, "name": "taif"} 
flag = "9" 

setdata = {str(9),flag,9,data["name"],data["name"],tuple(data)} #we cannot directly use data dictionary in setdata set because it is unhashable, use tuple to aviod error
print(setdata)


# Set is collection of unique unordered data 