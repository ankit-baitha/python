l1=[35,75,47,30,64,37]
#simple format
l2=[]
for i in l1:
    l2.append(i)
print(l2)

print()
#by comprehension
l3=[i for i in l1]
print(l3) 