# mortgage.py
#
# Exercise 10
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000
month = 0

while principal > 0:
    while month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal * (1+rate/12) - (payment+extra_payment)
        total_paid = total_paid + payment + extra_payment
        remain = principal - total_paid
        month = month + 1
        if remain >= 0:
            print(month, " ", round(total_paid, 2), " ", round(remain, 2))
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment 
    remain = principal - total_paid
    month = month + 1
    if remain >= 0:
        print(month, " ", round(total_paid, 2), " ", round(remain, 2))
print('Tatal paid', round(total_paid, 2))
print('Tatal month', month)
