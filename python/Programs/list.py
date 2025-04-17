
d1 = {1,2,3}
d2 = {9,9,9,"t"}
listdata = [4,5,6,7,8]
listdata2 = [1,2,3,4,5,6,7]
list = [d1,d2,listdata,listdata2]
print(list) 

list.pop() # pop takes index, or last element(default) without index
print(list) 
print("Length of list is",len(list))

city = ["mumbai","delhi","gugurgram"]
city.reverse() # descending
print(city)

city = ["mumbai","delhi","gugurgram"]
city.sort() # ascending
print(city)
# list can have duplicate data and it is in ordered(sequence), it is in sequence so we can use index 

# [{}] OK
# {[]} NO
