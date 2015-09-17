balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
month = 1
Total_amount_paid = 0.0
while month <= 12 :
    min_monthly_payment = balance * monthlyPaymentRate
    balance -= min_monthly_payment
    balance += (balance * annualInterestRate)/12
    Total_amount_paid += min_monthly_payment
    print ("Month: %d"%month)
    print ("Minimum monthly payment: %0.2f"%min_monthly_payment)
    print ("Remaining balance: %0.2f"%balance)
    month += 1
    
print ("Total Paid: %0.2f"%Total_amount_paid)
print ("Remaining balance: %0.2f"%balance)
    

