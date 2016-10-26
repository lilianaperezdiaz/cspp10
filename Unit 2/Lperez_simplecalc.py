equation = input("Enter an equation")
first_term = equation[0]
#first_term is looking at the first number of equation
operation= equation[1]
#operation is looking at the second number of equation
second_term = equation[2]
#second_term is looking at the third number of equation
f= int(first_term)
#variable f is made to make first_term an int
s= int(second_term)
#variable s is made to make second_term an int
x= 0
#x is given the value zero it can not effect the outcome
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
