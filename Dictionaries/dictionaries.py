#Dictionary
# dictionary allows user to write the data in the form of keys and values.
# dictionaries are enclosed inside curly brackets{}.
# keys and values are seperated by colon.
# every key value pair is seperated by a coma(,).

employee_data={"name":"ankit", "age":23, "gender":"male"}
print(type(employee_data))
print(employee_data)

print(employee_data["age"])
print(employee_data["name"])
print()

#iteration in dictionares

student={"name":"ankit","class":"12th","roll_no":11222840}
#printing all key neames one by one
print("all key names are ")
for i in student:
    print(i)
#printing all the value names one by one
print("the value names are")
for x in student:
    print( student[x])
print()
    
#using value fucntion 
print("using value function")
for x in student.values():
    print(x)

#using items function
for x,y in student.items():
    print(x,y)
    


    

