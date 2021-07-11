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
translated_str = ""
for item in phone:
    number = int(item)    
    translated_str += str(numbers.get(number)) +" "
print(translated_str)
