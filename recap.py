result=input("Will RCB Win ? ")
if result == "yes":
    print("Ee Saala Cup Namde")
elif result == "no":
    print("Nothing new")
else:
    print("Invalid")



num = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
fun = input("Add, Sub, Multi, Div : ").lower()
res = " "
if fun == "add":
    res = num+num2
    print(res)
elif fun == "sub":
    res = num-num2
    print(res)
elif fun == "multi":
    res = num*num2
    print(res)
elif fun == "div":
    res = num/num2
    print(res)
else:
    print("Invalid Funtion")



    