
# tupledata[0] = 5 'tuple' object does not support item assignment, we generally keep that data here which is not changed
setdata = {1,2}
setdata2 = {1,2}
list = [2,"list"]
tupledata1 = (1,setdata,setdata2,list)
print(tupledata1)

tuple2 = ((9,8))
print(tuple2[0])
print(tuple2[1])



# [{}] OK
# ({}, [], ) Ok

# {[]} NO 