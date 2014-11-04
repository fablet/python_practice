from operator import itemgetter

stock_data = [
    ["2014-06-01", "APPL", 100.11],
    ["2014-06-02", "APPL", 110.61],
    ["2014-06-01", "MSFT", 20.46],
    ["2014-06-03", "APPL", 120.22],
    ["2014-06-04", "APPL", 100.54],
    ["2014-06-02", "MSFT", 21.25],
    ["2014-06-03", "MSFT", 32.53],
    ["2014-06-04", "MSFT", 40.71],
]

def stock_keys(stock_list):
  unique = []
  for stock in stock_list:
    if stock[1] not in unique:
      unique.append(stock[1])
  return unique

def stock_groups(stock_list):
  sorted_stock = sorted(stock_list, key=itemgetter(1))
  stock_dict = {}
  stocks_per_key = []
  key_list = stock_keys(stock_list)
  for key in key_list:
    start = 0
    end = len(sorted_stock)
    for i in range(start,end):
      if sorted_stock[i][1] == key:
        stocks_per_key.append(sorted_stock[i])
    stock_dict[key] = stocks_per_key
    stocks_per_key = []
  return stock_dict
    
def print_stocks(stock_dict):
  for key, value in stock_dict.items():
    print('{}:'.format(key))
    for item in value:
      print('\t{}'.format(item))
    
my_stocks = stock_groups(stock_data)
print_stocks(my_stocks)  
      