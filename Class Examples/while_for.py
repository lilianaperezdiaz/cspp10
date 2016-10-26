for n in range(1,6):
    print(n)
    
m = 1
while (m <=5):
    print(m)
    m = m +1 #increase n by 1
#program will take a bunch of numbers
#until the user types "exit" and then
#print out all of the numbers together
final=""
inp = input("Enter a number or exit")
while(inp != "exit"):
    inp=input("Enter a number")
    final=final+ inp +" "
    
print(final)