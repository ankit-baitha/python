# Function 
#1 get
# 2 item to value get in tuples
# 3 keys
# 4 values
# 5 copy
# 7 update
# 8 pop 
# 9 popitem
# 10 clear


#get
student={"name":"ankit","class":"12th","roll_no":11222840}
x=student.get("name")
print(x)


# item 
# a = student.items()
# print(a)

# keys
# b=student.keys()
# print(b)

#values
# c=student.values()
# print(c)

#copy
# d=student.copy()
# print(d)

# 1st update second rull  variable["key_name"]=value 
# student.update({'roll_no':1229})
# print(student)
# student['roll_no']=11222999
# print(student)


#pop 
print(student)
# student.pop("name")
# print(student)


#popitems  in defoult last  items delete
student.popitem()
print(student)
