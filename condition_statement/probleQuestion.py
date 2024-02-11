# write a progarm to get fibonaaci series up to 10 nuber
a=0
b=1
print(a)
print(b)
for i in range(2,11):
    c=a+b
    a=b
    b=c
    print(c)

# write a program to check if a number is prime or not.
num=int(input("enter a number  : "))
if num <=1:
    print("it is not a prime number")
else:
    for i in range(2,num): 
        if num%i==0:
            print("numner is not a prime number")
            break
    else:
        print("it is a prime number")
    

# write a program to find a palindrome of integers.

num =int(input("enter a number here: "))
temp=num
rev= 0 
while num>0:
    dig =num%10
    rev=rev * 10 + dig
    num = num//10
if rev ==temp:
    print("it is palindrome")
else:
    print("it is not palindrome")
    
# writr a progarm to create  an area calculator
