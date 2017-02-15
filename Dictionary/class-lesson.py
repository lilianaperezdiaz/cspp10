from pprint import pprint
#from the pprint module, import the pprint function
#dictionarie contain key-value pairs
d = {
#key : value
    "name": "Lily",
    "birthmonth" : "July",
    "grade" : "10"
}
print(d)

schedule={
    "A":"Trig",
    "B":"Living Enviornment",
    "C":"English",
    "D":"Global",
    "E":"Global"
    
}
schedule["E"]="Trig"
print(schedule['E'])
#only checks if it exsit inas a KEY not a value
if "E" in schedule:
    print("E is in the schedule")
else:
    print("E is not in schedule")
        
#how to check if a value exist
for key in schedule:
    if (schedule[key]) == "Trig":
        print("Exist as value!")
        break
else:#this only happen if for loop dosn't break
    print("Does not exist as value!")