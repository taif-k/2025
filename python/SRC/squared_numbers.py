numbers =list(range(1,11))  # generating numbers 1 t0 10 in a list using range
numbers = numbers[:5]       #  using slice to get first 5 numbers

squared_numbers = {num ** 2 for num in numbers }  # using for loop to iterate over each num from 1 - 5 and squaring it using ( ** 2)
                                                  # also keeping squared numbers in a set  
print(squared_numbers)
