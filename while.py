i=1
while i <= 5:
    print("*" * i)
    i = i+1
print("done")



secret_num = 9
guess_limit = 3
guess_count = 0

while guess_count > guess_limit:
    guess=int(input("Guess: "))
    guess_count +=1
    if guess == secret_num:
        print("You Won")
        break
else:
    print("Loss")
    