# pcost.py
#
# Exercise 1.27
total_price = 0

f = open('Data/portfolio.csv', 'rt')
headers = next(f).split(',')
for line in f:
    row = line.split(',')
    total_price = total_price + (int(row[1]) * float(row[2]))
print(f'total cost {total_price}')
f.close()
