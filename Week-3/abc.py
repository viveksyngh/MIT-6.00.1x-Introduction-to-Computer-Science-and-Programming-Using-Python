def performOps(A):
    m = len(A)
    n = len(A[0])
    B = []
    for i in xrange(len(A)):
        B.append([0] * n)
        for j in xrange(len(A[i])):
            B[i][n - 1 - j] = A[i][j]
    return B

A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
B = performOps(A)
for i in xrange(len(B)):
    for j in xrange(len(B[i])):
        print B[i][j],
        
def rotateArray(A, B):
        ret = []
        B = B%(len(A))
        for i in xrange(len(A)-B):
            ret.append(A[i + B])
        for j in range(B):
            ret.append(A[j])
        return ret
        
print(rotateArray([ 14, 5, 14, 34, 42, 63, 17, 25, 39, 61, 97, 55, 33, 96, 62, 32, 98, 77, 35 ],56))

def performOps(A):
    blen = 2 * len(A)
    B = [0]*blen
    for i in xrange(len(A)):
        B[i] = A[i]
        B[i + len(A)] = A[(len(A) - i) % len(A)]
    return B
A = [5, 10, 2, 1]
B = performOps(A)
for i in xrange(len(B)):
    print B[i],
    