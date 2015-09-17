def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    res = []
    for key1 in aDict.keys() :
        temp = aDict[key1]
        found = False
        for key2 in aDict.keys() :
            #print key1, key2
            if key1 != key2 :
                if aDict[key2] == temp :
                    found = True
                    break
        if not found :
            res.append(key1)
    res.sort()
    return res
    
print(uniqueValues({1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}))
print(uniqueValues({1: 1, 2: 1, 3: 1}))
            
            