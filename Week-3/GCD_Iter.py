def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    while b > 0:
        if a%b == 0 :
            return b
        a,b = b, a%b        
    return b

    
print(gcdIter(8,12))