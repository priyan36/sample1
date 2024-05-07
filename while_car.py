command=""
started= False
while True:
    command=input("> ").lower()
    if command=="start":
        if started:
            print("car already started")
        else:
            started= True
            print("Car Started")
    elif command=="stop":
        if not started:
            print("car is already stopped")
        else:
            started = False 
            print("Car Stoped")
    elif command=="help":
        print("""
Start - to start
Stop  - to stop
Quit - to quit""")
    elif command=="quit":
        break
    else:
        print("dont understand")