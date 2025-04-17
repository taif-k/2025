
# tupledata[0] = 5 'tuple' object does not support item assignment, we generally keep that data here which is not changed
setdata = {1,2}
setdata2 = (91,20)
list = [2,"list"]
tuple1 = (1,setdata,setdata2,list)
print(tuple1)

tuple2 = ((9,8))
print(tuple2[0])
print(tuple2[1])

data3, data4 = (10,"20")
print(type(data3),data3)
print(type(data4),data4)


# [{}] OK
# ({}, [], ) Ok

# {[]} NO 