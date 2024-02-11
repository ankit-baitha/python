a=["rose","rechel","monica", "joe"]
#write a program to swap first and forth element
a[0],a[3]=a[3],a[0]
# print(a)

#write a program to add a new value at second position
a.insert(1,"ankit")
# print(a)
#write a program to delete a value from 3rd position
# a.pop(2)
# print(a)

b=[13,7,12,10]
#write a program to multiply all the numbers in list
mult=1
for i in b:
    mult=mult*i
print(mult)
#write a program t get the largest number form the list
b.sort()
print("the largest value in the given list is ",b[-1])

#write a progra to get the smallest number form the 
print("the smallest value in the given list is",b[0])

