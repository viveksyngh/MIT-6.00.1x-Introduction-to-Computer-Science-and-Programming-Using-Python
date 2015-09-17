balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = (annualInterestRate)/12.0
start = balance/12
end = (balance * (( 1 + monthlyInterestRate) ** 12) ) / 12.0
min_monthly_payment = 0.0
found = False
while not found :
    month = 1
    min_monthly_payment = (start + end)/2.0
    new_balance = balance
    while month <= 12 :
        new_balance -= min_monthly_payment
        new_balance += (new_balance * annualInterestRate) / 12
        month += 1
    if  new_balance <= 0.001 and new_balance >= -0.001 :
        found = True
    elif new_balance > 0.001:
        start = min_monthly_payment
    elif new_balance < -0.001 :
        end = min_monthly_payment
        
print ("Lowest Payment: %0.2f" %min_monthly_payment)