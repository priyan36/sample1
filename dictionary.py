phone=input("Phone: ")
digit ={
    "1": "one",
    "2": "two",
    "3": "three"
}
output = ""
for ch in phone:
    output+= digit.get(ch, "!!") + " "
print(output)