original=[0,2,1,4,5,1,6,7,1]
to_replace=2
replace_with=1

def replace_all(original, to_replace, replace_with):
    for index in range(len(original)):
        if original[index]==to_replace:
            original[index]=replace_with
    # alist[3] = "hi"
    print(original)
replace_all(original,to_replace,replace_with)