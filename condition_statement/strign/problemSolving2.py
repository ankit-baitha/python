#take an input from a user as a string then ,reverse it
a = input("enter anything here: ")
print(a[::-1])


#Write a program to check if a string contains only digits.

a = input("enter anything here: ")
print(a.isdigit())



#Write a program to check if a string is palindrome.
a=input("enter anything here: ")
rev=a[::-1]
if a==rev:
    print("it is palindrome")
else:
    print("it is not palindrome ")


#write a program to find number of vovels in a string 

a=input("enter anything here: ")
vowels = 0
for i in a :
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
        vowels+=1
print("the number of vowels in the following string are ",vowels)


#Write a program to check if every word in string beging with a capital letter.
b=input("enter anything here: ")
print(b.istitle())
