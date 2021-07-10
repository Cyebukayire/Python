list = [1,2,3,5,1,2,3,4,5,4]
print(list)

# This method is not efficient
# for item in list:
#     count = list.count(item)
#     # print (str(item) +" exists "+ str(count) +" times")
#     if count>1:
#         list.remove(item)
# print(list)

# new method
unique = []
for number in list:
    if number not in unique:
        unique.append(number)
print(unique)

# muzigahono123@gmail.com
# muziga10
