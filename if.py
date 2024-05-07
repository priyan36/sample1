name = "S"

if len(name) < 2:
    print("Invalid")
elif len(name) > 13:
    print("invalid2")
else:
    print("Good")


weight=int(input("your weight: "))
unit = input("K-kilo and G- grams: ")

if unit.upper() == "K":
    convert = 1000 * weight
    print(f"your weight in gram is {convert}")
elif unit.upper() == "G":
    convert = weight / 1000
    print(f"weight in kg is {convert}")
else:
    print("invalid")