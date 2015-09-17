def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    oddTup = ( )
    for i in range(0, len(aTup), 2) :
        oddTup += (aTup[i],)
    return oddTup

print(oddTuples(('I', 'am', 'a', 'test', 'tuple'))) 
        