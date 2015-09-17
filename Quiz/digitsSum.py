def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    assert not N < 0  
    if N < 10 :
        return N 
    else :
        return (N%10) + sumDigits(N/10) 
print(sumDigits(0))