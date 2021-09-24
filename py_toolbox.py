

def sorting(keys,values,rev=0):
    if rev==0:
        sortedval=[]
        for i, j in enumerate(sorted(keys)):
            if j in keys:
                sortedval.insert(i,values[keys.index(j)])
    else:
        sortedval=[]
        for i, j in enumerate(reversed(sorted(keys))):
            if j in keys:
                sortedval.insert(i,values[keys.index(j)])
    
    return (sortedval,sorted(keys))

def listrotate(mylist,amount=0):
    return [mylist[(i + amount) % len(mylist)] for i, x in enumerate(mylist)]


