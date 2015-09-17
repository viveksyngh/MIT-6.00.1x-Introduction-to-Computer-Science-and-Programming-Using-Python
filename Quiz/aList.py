def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    sublist = []
    for string in aList :
        if len(string) < 4 :
            sublist.appen(string)
    return sublist