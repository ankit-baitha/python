#tuple
#Tuples are the collection of ordered and un-mutable data.
#for tuples no brackets are mandatory. by choice one can use parenthese.
#The value inside a tuple is separted by coma(,)
# Once created tuples cannot be changed.
#Multiple datatypes can be written inside a tuples.


a="apple","mango", "banana",5,7,73,1.4 
print(type(a))
#single items are not  tupel
b="ankit"
print(type(b))
c="ankit",
print(type(c))



#slicing and Iteration in tuples
a=(" onePlus","vivo","redmi", "sumsung","nokia")
print(a[1::])
print(a[:3])
print(a[::2])
#reverse
print(a[::-1])



#iteration
#with for loop
b=(" onePlus","vivo","redmi", "sumsung","nokia")
for i in b:
    print(i)

#along with range; and length in for loop
for i in range(len(b)):
    print(b[i])

#along with while loop
i=0
while i<len(b):
    print(b[i])
    i+=1