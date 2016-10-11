equation = input("Enter an equation")
first_term = equation[0]
operation= equation[1]
second_term = equation[2]
f= int(first_term)
s= int(second_term)
x= 0
if operation== "+":
    x= f  + s 
if operation == "-":
    x= f - s 
if operation == "*":
    x= f * s 
if operation == "/":
    x= f / s 
if operation == "%":
    x= f % s 
else:
    print ("operation is invalid")
print("Your answer is {}" .format(x))
