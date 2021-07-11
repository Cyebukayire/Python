# Loop through a string
string = " "
for item in "Python":
    string = string + item
print(string)

#  Loop through a list
print ("\nlist 1")
for item in [2,3,5,2]:
    print(item)

print ("\nlist 2")
for item in range(10):
    print (item)

print ("\nlist 3")
# 5: range from 5
# 10: range up to 9
# 2: move 2 steps forward
for item in range(5, 10, 2):
    print(item)

#Print the sum
price = [10, 20, 30]
sum = 0
for item in price:
    sum += item
print("The sum is: ")
print(sum)