command = ""
started = False
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started")
        else:
            started =True
            print("Car started")
    elif command == "stop":
        if not started:
            print("Car alresy stopped")
        else:
            started = False
            print("Car stopped")
    elif command == "help":
        print ("""
start- on the car
stop - off the car
quit - to quit""")
    elif command == "quit":
        break
else:
        print("Invalid")
