# mortgage.py
#
# Exercise 1.8
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000
extra_month = 12
month = 0

while principal > 0:
    while extra_month > 0:
        principal = principal * (1+rate/12) - (payment+extra_payment)
        total_paid = total_paid + payment + extra_payment
        extra_month = extra_month - 1
        month = month + 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment 
    month = month + 1

print('Tatal paid', total_paid)
print('Tatal month', month)
