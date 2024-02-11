# Functions are a set of code,  which once created, they can be used throughout the program
# function help break our program into smaller parts and helps it look more organized and manageable.
def hello():
    print("hello world")

hello()

# parameters
# parameterds are the variables written inside the parenthese with the name of function
# Arguments
# arguments are the values passed to the parameters while calling the function

def add(x,y):#parameters
    print(x+y)
add(5,7)#arguments


#Ruturn

# Return keyword in python is used to exit a function and return the value of the function

def ans():
    return("hello world")
print(ans())

def add(a,b):
    return(a+b)
print(add(12,5))


# Recursion in python
# Recursion in most commonly used mathematical and programming concept.
# In simple words, recursion means a function can call itself , giving us a benefit of looping through data in order to get a result
# Advantages:
#they make the code look clean and organized
# By the use of recursive functions ,a complex task can be broken down into small sub-parts.
#sequence generation becomes easier.

#Disadcantages:
#recursive functions take up a lot of memory.
#sometimes the logic becomes hard to follow.




def fact(n):
    if n==1:
        return 1
    else:
        return (n*fact(n-1))
print(fact(5))


#lambda function in python
# It is used when an anonymous function is required for a short period of time.
# it can take numerous arguments
# it can only have one expression

a =lambda b: b*5
print(a(4))



x=lambda a,b,c: (a+b)*c
print(x(2,4,6))
    
    
#local and global variables
# local variables are restricted to only one block of code and cannot be changed throughout the program
# x=24
# print("first variables x ",x)
# def hello():
#     x=25
#     return x
# print(hello())
# print(x)


#Global variables are not restricted to one block of code and throu be changed throughout the program
x=24
print("first variables x ",x)
def hello():
    global x
    x=25
    return x
print(hello())
print(x)
