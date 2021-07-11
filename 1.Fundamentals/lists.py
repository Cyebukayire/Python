names = ['Mary','John', 'Kelly', 'Musa', 'Cedro']
print (names[2:4])
# maximum number in a list
numbers = [12,0,5,3,1,9,6]
max = numbers[0]
for number in numbers:
    if max<number:
        max=number
print ("The maximum number is : " + str(max))
