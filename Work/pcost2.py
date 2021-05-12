# pcost.py
#
# Exercise 1.32
import csv
import sys

def portfolio_cost(filename):
    total_price = 0
    f = open(filename, 'rt')
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        total_price = total_price + (int(row[1]) * float(row[2]))
    f.close()
    return total_price

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost('Data/portfolio.csv')
print(f'Total cost: {cost}')
