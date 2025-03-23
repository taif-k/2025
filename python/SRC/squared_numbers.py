numbers =list(range(1,11))  
numbers = numbers[:5]      

squared_numbers = {num ** 2 for num in numbers }  # using for loop to iterate over each num from 1 - 5 and squaring it using ( ** 2)
                                                   
print(squared_numbers)
