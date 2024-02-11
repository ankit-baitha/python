print('''
 + ADD     
- SUBTRACT 
 * MULTIPLE  
 / DIVIDED
  % MODULSE
  
      ''')
number1 = int(input("Enter the frist number "))
number2 = int(input("Enter the second number "))
opr=input("choese the oprator + - * / %")
if opr=="+":
    print(number1+number2)
elif opr=="-":
    print(number1-number2)
elif opr=="*":
    print(number1*number2)
elif opr=="/":
    print(number1/number2)
    
elif opr=="%":
    print(number1%number2)
else:
    print("don't match the oprator")
