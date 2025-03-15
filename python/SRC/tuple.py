
# tupledata[0] = 5 'tuple' object does not support item assignment, we generally keep that data here which is not changed
setdata = {"set",1,2}
list = [3,"list"]
tupledata = (1,setdata,list)
# tupledata = (5,5,"five") # but we can completely update the tuple but not the particularly indexing
print(tupledata)



# [{}] OK
# ({}, [], ) Ok

# {[]} NO 