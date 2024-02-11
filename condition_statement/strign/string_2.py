#endswith () - return true if the string ends with the specified value
a ="harry potter"
print(a.endswith("r"))
print(a.endswith("t",6,9))
print(a.endswith("potter"))
print()

#startswith() - return true if the string starts with the specified value
print(a.startswith("h"))
print(a.startswith("p" ,6,9))
print()
#swapcase() - swaps cases ,lower case becomes upper case and vice versa
a="ankit kumar"
print(a.swapcase())

#strip()- return a trimmed version of the string
print()
a ="   ankit potter"
print(a)
print(a.strip())
b="       ******ankit......"
print(b)
print(a.strip("*,., "))
#split()- splits the string at the specified separator ,and return a list

a= "#grr#fjfg#ihn#oih#oh"
print(a.split("#"))

#LJUST()- return a left justified version of the string
a="harry potter"
x=a.ljust(20,"*")
print(x,"is my favorite movie")


#rjust()-return a right justified version of the string
a="harry potter"
x=a.rjust(20)
print(x, "is my fovarite movie")

#replace()- return a string where a specified value is replaced with a specified value
a="my name is john"
print(a)
print(a.replace("john","lisa"))

#rindex()- searches the string for a specified value and returns the last position of where it was found

a="harry potter and the prisoner of azkaban"
print(a.rindex("harry"))
print(a.rindex("prisoner"))

#rfind()
a="harry potter and the prisoner of azkaban"
print(a.rfind("harry"))
print(a.rfind("prisoner"))

