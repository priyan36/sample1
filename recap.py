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


a=[]
for i in range (5):
    num=int(input())
    a.append(num)
print(a)
sum=0
for i in a:
    sum = sum+i
print(sum)

#nested_for
for i in range(1,5):
    print()
    for j in range(1,i+1):
     print(j,end="")




#while loop
i=10
print()
while i>0:
    print(i)
    i-=1


#factorial
a=int(input("Enter a num for fact: "))
fact = 1
while a>0:
    fact=fact*a
    a=a-1
print(fact)

