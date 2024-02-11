# letter =input("enter a letter here : ")
# if (letter in "aeiou") or (letter in "AEIOU"):
#     print("it is a vowel")
# else:
#     print("it is not a vowel")
#
print()
number=int(input("enter a number : "))
if(number>=0 and number<=9):
    print("single digit number")
elif(number>=10 and number<=99):
    print("double digit number")
elif(number>=100 and number<=999):
    print("three digit number")
elif(number>=1000 and number<=9999):
    print("four digit number")
else:
    print("no found any number")


    