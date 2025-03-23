numbers = list(range(10,0,-1))
print("Numbers: ",numbers)
numbers = numbers[:6]
print("First 5 numbers: ",numbers)

squared_numbers = [num ** 2 for num in numbers]
print("Square of first 5 descending numbers: ",squared_numbers)