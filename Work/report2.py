import csv

def read_prices(filename):
    """ read prices from file """
    price = {}
    with open(filename, 'rt') as f:
        line = csv.reader(f)
        try:
            for line in f:
                row = line.split(',')
                price[row[0].replace('"', '')] = float(row[1])
        except IndexError:
            pass
    return price

