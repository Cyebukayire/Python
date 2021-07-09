numbers = [2,4,5,0,9,1,0]
print (numbers)
print("\nAPPEND METHOD")
newNumber = input("Enter number to Append: ")
numbers.append(newNumber)
print(numbers)

# insert at the beginning
print("\nINSERT METHOD")
newNum = input("Enter number to insert: ")
index = input("Enter index number: ")
numbers.insert(index, newNum)
print(numbers)

# remove item
print("\nDELETE METHOD")
delete = input("Enter number to remove: ")
numbers.remove(delete)
print(numbers)

# clear the list
numbers.clear()
