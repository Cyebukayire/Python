class NumberFunctions():
    def __init__(self, list):
        self.list = list

    def maximum(self):
        max=list[0]
        for number in list:
            if max < number:
                max = number
        
        return  max

# list = [2,34,0,3,1,44]
# maxi = maximum(list)
# print(maxi)
        

        
    