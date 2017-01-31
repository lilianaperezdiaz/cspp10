#working with Ethan
original=[0,3,6,8,0,0,0,7,4]
target=0
def remove_all(original,target):
    while target in original:
        original.remove(target)
    
    
remove_all(original,target)
print(original)



