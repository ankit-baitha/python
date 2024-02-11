# lists are the collection  of ordered and mutable DeprecationWarning
# list are written inside the squared brackets.
# The value inside a list a separeted by coma(,).
# mutable means once created ,they can be changed.
# multiple datatypes can be written inside a list.

li=[22, 4, 55, 4, 52, 3, 6, 63]
print(li," As a print the list")
li.sort()
print(li ," sorting the list")#sort the list
li.reverse()
print(li,"reverse the  list")
li.append(34,"add to end list")#adds 34 at the end of the list
print(li)
li.insert(1, 345,"insert a list of indexing number")
print(li)

li.pop(2)#delete the indez 2
print(li)

li.remove(55)#remove 55 form the list
print(li)
