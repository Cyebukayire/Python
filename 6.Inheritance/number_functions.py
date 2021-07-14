class Numbers():
    def __init__(self, list):
        self.list = list

    def maximum(self):
        maxi = list[0]
        for number in list:
            if maxi < number:
                maxi = number
        return  maxi
    
    def minimum(self):
        min = list[0]
        for number in list:
            if min > number:
                min = number
        return min

list = [2,34,0,3,1,44]
obj = Numbers(list)
maxi = obj.maximum()
mini = obj.minimum()

print("The maximum is: " + str(maxi))
print("The minimum is: " + str(mini))

# maxi = maximum(list)
# mini = minimum(list)
# print(maxi)
        

        
    