numbers = [2,4,5,0,9,-67,1,0]
# print (numbers)
# print("\nAPPEND METHOD")
# newNumber = input("Enter number to Append: ")
# numbers.append(newNumber)
# print(numbers)

# # insert at the beginning
# print("\nINSERT METHOD")
# newNum = input("Enter number to insert: ")
# index = input("Enter index number: ")
# numbers.insert(index, newNum)
# print(numbers)

# # remove item
# print("\nDELETE METHOD")
# delete = input("Enter number to remove: ")
# numbers.remove(delete)
# print(numbers)

# # clear the list
# # numbers.clear() #not workin

# # delete at the end
# print("\nPOP METHOD")
# numbers.pop()
# print (numbers)

# # Check for Location of item in list
# print("\nINDEX METHOD")
# numbers.index(9)

# # Check for existance of item in list
# print("\nEXISTANCE OF AN ITEM")
# num = input("Enter any number to check: ")
# print("Item exists: " + str(num in numbers))

# Count existance of a number
print("\nCOUNT EXISTANCE OF AN ITEM")
num = input("Enter any item from list: ")
count = numbers.count(num)
print("The item exists " + str(count) + " times")

# Sorting
print("\nSORT METHOD")
numbers.sort()
print(numbers)

# REVERSING
print("\nREVERSE METHOD")
numbers.reverse()
print(numbers)

