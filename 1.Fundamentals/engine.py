command = " "
car_started = False
while True:
    command = raw_input("Enter command: ").lower()

    if command == "help":
        print("""

Available Commands:

start - Start Engine
print("stop - Stop Engine
print("quit - exit

        """)

    elif command == "start":
        if car_started:
            print("car is already started.\n")
        else:
            car_started = True
            print("car engine started .......\n")

    elif command == "stop":
        if car_started:
            car_started = False
            print("car engine stopped......\n")
        else:
            print("car is already stopped.\n")

    elif command == "quit":
        print("End!\n")
        break

    else:
        print("I don't understand that...\n")

    
    