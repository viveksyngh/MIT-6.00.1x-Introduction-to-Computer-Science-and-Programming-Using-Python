def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    keys_list = []
    for key in aDict.keys() :
        if aDict[key] == target :
            keys_list.append(key)
    keys_list.sort()
    return keys_list
    
print(keysWithValue({1 : 8, 8 : 3, 2 :3, 4 : 3 }, 3))