def fibMetered(x) :
    global numCalls
    numCalls += 1
    if x == 0 or x == 1 :
        return 1
    else :
        return fibMetered(x-1) + fibMetered(x-2)

def test(n) :
    global numCalls
    for i in range(0, n + 1) :
        numCalls = 0
        print("Fibonnaci is " + str(fibMetered(i)))
        print("Fib called " + str(numCalls) + " times")
test(15)
        