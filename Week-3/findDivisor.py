def findDivisors(num1, num2) :
    divisors = ()
    for i in range(1, min(num1, num2) + 1) :
        if num1%i == 0 and num2%i == 0 :
            divisors += (i,)
    return divisors
    
divs = findDivisors(20, 100)
total = 0
for d in divs :
    total += d
print(total)
            