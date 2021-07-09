list = [1,2,3,5,1,2,3,4,5,4]
print(list)
for item in list:
    count = list.count(item)
    # print (str(item) +" exists "+ str(count) +" times")
    if count>1:
        list.remove(item)
print(list)