data = {"id":132, "name": "taif"} 
set3 = {tuple(data.values())} 
print("dictionary is printed inside set using tuple: ",set3)

setdata1 = {1,2,3,4}
setdata2 = {4,5,6}
setdata1.add(7)
setdata1.discard("string") # discard will not throw an error unlike remove, if the element is not present in set 
setdata1.remove(2) 
setdata1.pop() # when using pop in set it does not take any arg(index was passed as arg in list) but set is unordered so no index, pop in set will remove randomly
print(setdata1)