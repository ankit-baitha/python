# 1
# 12
# 123
# 1234
# 12345
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end =" ")
    print()

# 1
# 22
# 333
# 4444
# 55555
for i in range(1,6):
    for j in range(1,i+1):
        print(i, end =" ")
    print()
    
# 11111
# 2222
# 333
# 44
# 5
for a in range(1,6):
    for b in range(6,a,-1):
        print(a, end =" ")
    print()
# 65432
# 6543
# 654
# 65
# 6
print()
for a in range(1,6):
    for b in range(6,a,-1):
        print(b, end =" ")
    print()
print()

for i in range(1,6):
    for j in range(5, i, -1):
        print(" ",end=" ")
    for k in range(i):
        print("*", end="")
    print()

# 1
# 21
# 321
# 4321
# 54321
print()
for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
print()

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(5,0,-1):
    for j in range(0,i-1):
        print("*",end=" ")
    print()