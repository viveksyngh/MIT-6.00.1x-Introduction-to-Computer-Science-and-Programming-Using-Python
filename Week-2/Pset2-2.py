balance = 320000
annualInterestRate = 0.2
min_monthly_payment = 10
found = False
while not found :
    month = 1
    new_balance = balance
    while month <= 12 :
        new_balance -= min_monthly_payment
        new_balance += (new_balance * annualInterestRate) / 12
        month += 1
    if  new_balance <= 0 :
        found = True
    else :
        min_monthly_payment += 10
print "Lowest Payment: " + str(min_monthly_payment)