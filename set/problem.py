# 1 write a progarm to find max and min in a set.
a ={12,6,7,9,23,20,10}
maximum=max(a)
minimum=min(a)
print("The minimum value in the set is ", minimum)
print("The maximum valuen in the given set is ",maximum)


# # 2 Write a progam to find common elements in three lists using sets
b=[1,5,6,8,2]
c=[4,5,6,7]
d=[1,9,6,2,5]
print(" the common elements in the given three list are ", set(b) & set(c) & set(d))

# 3 write a program to find difference between two sets.

b={1,5,6,8,2}
c={1,5,6,7}
print(b.difference(c))


# 4 write a python program to remove an item from a set  if is present in the set.
b={1,5,6,8,2}
b.discard(8)
print(b)

# 5 Write a python program to check if a set a subset of another set.
a={1,2,3,4,5,6}
b={2,3,4}
print(b.issubset(a))
