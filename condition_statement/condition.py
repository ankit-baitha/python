age=int(input("enter th number : "))
if(age>18):
   print("adult")
else:
   print("not adult")
if(age>24 & age<56):
    print("you can work with us")
else:
    print("you cannot work with us")


num1=int(input("Enter the number 1: "))
num2=int(input("enter number 2: "))
num3=int(input("enter number 3: "))
num4=int(input("enter number 4: "))
if(num1>num4):
    f1=num1
else:
    f1=num4
if(num2>num3):
    f2=num3
else:
    f2=num3
if(f1>f2):
    print(str(f1)+"is greatest")
else:
    print(str(f2)+"is greatest")