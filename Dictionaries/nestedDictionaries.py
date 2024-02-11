coure={
    "python":{"duration":"3 month", "fees":1500},
    "java":{"duration": "2 month", "fees":1000},
    "php":{"duration":"4 month", "fees":2000}

}
print(coure)
print(coure["python"]["duration"])

#loop method
for k, v in coure.items():
    print(k,v)
   
#update
coure['java']['fees']=7000
print(coure['java']['fees'])