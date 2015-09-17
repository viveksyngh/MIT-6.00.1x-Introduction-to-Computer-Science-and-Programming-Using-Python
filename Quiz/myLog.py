def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    assert not (x <= 0 and b < 2 )
    logValue = 0 
    value = 1
    while value < x :
        value = value * b
        logValue = logValue + 1
    if value == x :
        return logValue
    else :
        return logValue - 1
        
print(myLog(15, 3))
        