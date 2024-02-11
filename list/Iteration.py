#Iteration using for loop

a=["hulk", "thor", "Ironman" , "caption america"]
for i in a:
    print(i)
    
    
#Iteration using for loop with Range and lenght function
for i in range(len(a)):
    print(a[i])
    
    
#Interation using white loop
i=0
while i<(len(a)):
    print(a[i])
    i +=1

#Using short-hand for loop
[print(i) for i in a]
