mydict={
    "fast":  "in a quick manner",
    "ankit":"A coder",
    "marks":[1,2,3,4],
    "anotherdict":{'harry':"player"}
    
}
print(mydict['fast'])
print(mydict['ankit'])
print(mydict['marks'])
print(mydict['anotherdict']['harry'])

#print(list(mydict.keys()))
print(mydict.keys())
#print(list(mydict.values()))
print(mydict.items())#print the (key, value) for all contents of  the dictionary
print(mydict)
updatedict ={
    "lovish":"friend"
}
mydict.update(updatedict)#update th dictionary by adding key-value pairs from updatedict
# print(mydict)
# print(mydict.get["ankit"])