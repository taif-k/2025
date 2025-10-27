import name_as_main


# if name_as_main was running directly as script name was "__main__"
# but here name is name_as_main because it is imported and then used 
print(name_as_main.__name__) 