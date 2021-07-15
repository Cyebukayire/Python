def maximum(list):
    maxi = list[0]
    for number in list:
        if maxi < number:
            maxi = number
    return  maxi

def minimum(list):
    min = list[0]
    for number in list:
        if min > number:
            min = number
    return min


# imibare = [23,43,-5,2,454,1,0,100]
# maxi = maximum(imibare)
# mini = minimum(imibare)

# print("The maximum is: " + str(maxi))
# print("The minimum is: " + str(mini))

        

        
    