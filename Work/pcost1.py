# pcost.py
#
# Exercise 1.31
def portfolio_cost(filename):
    total_price = 0
    f = open(filename, 'rt')
    headers = next(f).split(',')
    for line in f:
        row = line.split(',')
        try:
            total_price = total_price + (int(row[1]) * float(row[2]))
        except ValueError:
            print(f'{row} has BAD INPUT')
    f.close()
    return total_price

cost = portfolio_cost('Data/missing.csv')
print(f'Total cost: {cost}')
