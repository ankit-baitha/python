# add pop remove discard copy
a={"ankit","deepak","aryan","vikash"}
a.add("ansh")
print(a)
a.pop()
print(a)
a.remove("ankit")
print(a)
a.copy()
print(a)

#isdisjoint issubset issuperset, update, clear ,union, difference update, intersection, intersection update, symmetric difference, symmetric difference update
b={"ironman","hulk",'thor','captain america'}
c={"superman","batman","wonder-woman"}
d={"hulk" ,"thor"}
print(b.isdisjoint(c))#true
print(b.isdisjoint(d))#false

print(b.issubset(d))#false
print(d.issubset(b))#true


print(b.issuperset(d))#true

a.update(b)
print(a)
a.clear()
print(a)