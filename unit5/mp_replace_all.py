original=[1,2,1,4,5,1,6,7,1]
to_replace=1
replace_with=3

def replace_all(original, to_replace, replace_with):
    for item in original:
        if item == 1:
            original.remove(item)
            original.insert(replace_with,item)
    print(original)
replace_all(original,to_replace,replace_with)