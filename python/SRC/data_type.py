# doc string
name = "taif"
country = "India"
info = f"""Hi {name}, I am using doc string for practise """
print(info)
print("{name}") # cant use {name} in double qoutes except f"{name}"

# dictionary
location = {"city":"New Delhi"}
print(f"My location is {location["city"]}",country)