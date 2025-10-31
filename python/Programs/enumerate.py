names = ["Alice", "Bob", "Charlie"]


# without enumerate [manual index]
index = 0
for name in names:
    print(index, name)
    index += 1

for index, name in enumerate(names, start=1): # start default is 0 , can be set with start=1(any integer)
    print(f"{index} {name}")
 