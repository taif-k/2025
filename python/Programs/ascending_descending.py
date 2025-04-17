# ascending order
ascending_numbers =list(range(1,11))  
print("Ascending Numbers: ",ascending_numbers)     

# descending order
descending_numbers = set(range(10,0,-1))  
print("Descending order, not maintained because set is used,which is unordered): ",descending_numbers)

descending_numbers = list(range(10,0,-2))
print("Descending order is maintained because list is used, which is ordered",descending_numbers)

