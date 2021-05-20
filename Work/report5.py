# Exercise 2.10
# report.py

import csv

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {'name': row[0], 'shares': int(row[1]), 'price':
            float(row[2])}
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    price = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        try:
            for rows in f:
                row = rows.split(',')
                price[row[0].replace('"', '')] = float(row[1])
        except IndexError:
                pass
    return price

def make_report(portfolio, prices):
    report = []
    for holding in portfolio:
        current_price = prices[holding['name']]
        change_price = prices[holding['name']] - holding['price']
        report_row = (holding['name'], holding['shares'], current_price, change_price)
        report.append(report_row)
    return report


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

total_cost = 0.0
for s in portfolio:
    total_cost += s['shares']*s['price']
    
print('total_cost: ' + f'{total_cost:0.2f}')

total_value = 0.0
for s in portfolio:
    total_value += s['shares']*prices[s['name']]

print('Current value: ', f'{total_value:0.2f}')
print('Gain/Loss: ', f'{(total_value - total_cost):0.2f}')

report = make_report(portfolio, prices)
for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
