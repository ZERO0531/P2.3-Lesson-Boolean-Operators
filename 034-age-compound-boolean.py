name = input("Your name: ")
age = int(input("Your age: "))
if age < 16: 
    print(f"You can't drive, {name}")
if age == 16 and 17: 
    print(f"You can drive but not vote, {name}")
if age <= 18 and <= 14: 
    print(f"You can vote but not rent a car, {name}. ")
if age >= 25: 
    print(f"You can do pretty much anything, {name}.")
