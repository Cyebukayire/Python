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
    translated_str += str(numbers.get(number), "new input") +" " # the "new input" won't replace the value of number because key is already assigned
    new_num = numbers.get(234, "new NUmbre") # 234 is assigned to  "new NUmber" value because it doesn't already have a value
print(translated_str)
