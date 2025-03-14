
# tupledata[0] = 5 'tuple' object does not support item assignment, we generally keep that data here which is not changed
setdata = {1,2,3}
tupledata = (1,setdata)
# tupledata = (5,5,"five") # but we can completely update the tuple but not the particularly indexing
print(tupledata)



# [{}] OK
# {[]} NO 