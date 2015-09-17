def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    mid = (len(aStr)-1)//2
    if aStr[mid] == char :
        return True
    elif char > aStr[mid ] :
        return isIn(char, aStr[mid + 1: ])
    else :
        return isIn(char, aStr[:mid - 1])
        
print(isIn('c', 'abcd'))