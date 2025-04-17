data = {"id":132, "name": "taif"} 
setdata1 = {tuple(data.values())} 
print("dictionary is printed inside set 1 using tuple: ",setdata1)

setdata2 = {1,2,3,4}
setdata2.add(7)
setdata2.discard("string") # discard will not throw an error unlike remove, if the element is not present in set 
setdata2.remove(2) 
setdata2.pop() # when using pop in set it does not take any arg(index was passed as arg in list) but set is unordered so no index, pop in set will remove randomly
print("Printing set 2 after using add,dicard,remove and pop: ",setdata2)


setdata3 = {1,2,3,4}
setdata4 = {4,5,6,7}

print("set 3: ",setdata3)
print("set 4: ",setdata4)
print("Difference method used on set 3 and set 4",setdata3.difference(setdata4))

colors = {"blue","green","black","red","white"}
for color in colors:
    print(color)