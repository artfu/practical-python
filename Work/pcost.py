# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    total_price = 0
    f = open(filename, 'rt')
    headers = next(f).split(',')
    for line in f:
        row = line.split(',')
        total_price = total_price + (int(row[1]) * float(row[2]))
    f.close()
    return total_price

cost = portfolio_cost('Data/portfolio.csv')
print(f'Total cost: {cost}')
