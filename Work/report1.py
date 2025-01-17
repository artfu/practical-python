# report1.py
#
# Exercise 2.5

import csv

def read_portfolio(filename):
    """ read portfolio from {filename} """
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {'name': row[0], 'shares': int(row[1]), 'price':
            float(row[2])}
            portfolio.append(holding)
    return portfolio

