def my_all (sequence):
    for unit in sequence:
        if unit:
            continue
        else:
            return(False)
    return(True)    
            

def my_any (sequence):
    for unit in sequence:
        if unit :
            return(True)
    return(False)        


print(my_all([43,45,0,21,23]))
print(my_any([0,0,0,0,10]))