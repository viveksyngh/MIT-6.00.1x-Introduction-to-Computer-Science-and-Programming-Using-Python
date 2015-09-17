def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    count = 0
    for ch in aStr :
        count = count + 1
    return count

print(lenIter("Hi"))
        