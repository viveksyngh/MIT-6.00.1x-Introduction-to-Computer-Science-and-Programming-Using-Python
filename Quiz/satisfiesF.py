def f(s) :
    return 'a' in s
    
def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    L_start = L [:]
    for string in L_start :
        if not f(string) :
            L.remove(string)
    return len(L)

L = ['a', 'b', 'a']
print satisfiesF(L)
print L

#run_satisfiesF(L, satisfiesF)