numbers = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine"
}
phone = raw_input("Phone: ")
for item in phone:
    number = int(item)
    print(numbers[number])
# print(numbers[1], numbers[2], numbers[3])