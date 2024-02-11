# Write a program to find a um of all the even numbers up to 50
# TotalSum=0
# for n in range(0, 51):
#     if n%2==0:
#          TotalSum=TotalSum+n
#          print(TotalSum)


    #Write a progra  to write first 20 number and their square number
# for i in range(1,21):
#    print("number ",i ,i**2)

#write a program to find sum of first 10 odd number using while loop

# n=0
# sum=0
# while n<=20:
#     if n%2!=0:
#         sum=sum+n
#     n+=1
# print(sum)


while True:
    name = input("enter customer's name: ")
    total=0
    
    while True:
        print("enter the amount and quantity :")
        amount=float(input("enter amount: "))
        quantity = float(input("enter quantity : "))
        total =total+(amount*quantity)
        repeat=input("do you want ot add more items?(yes \ no): ")
        if repeat =="no" or repeat =="No":
            break
    print("-"*40)
    print("name:", name)
    print("Amount to be paid: ",total)
    print("-"*40)
    print("************Happy shopping*************")
    
    repeat1=input("do you want to go to next customer :(yes \no)")
    if repeat1=="no" or repeat1=="No":
        break
    
