# Print coordinates
for x in range(4):
    print("coordinate")
    for y in range(4):
        print (x,y)

# F challenge
numbers = [5, 2, 5, 2, 2]
string = ""
for item in numbers:
    x = item
    while x>0:
        string = string + "x"
        x = x-1
    print (string)
    string = ""