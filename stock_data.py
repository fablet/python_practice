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
INDEX_DATE = 0
INDEX_SYMBOL = 1
INDEX_AMOUNT = 2


#create a list of unique stocks to later be used as the keys
#for the dictionary of stock tickers per stock
def unique_keys(data_list, index):
    unique = []
    for data in data_list:
        if data[index] not in unique:
            unique.append(data[index])
    return unique


#compile the list of stocks into a dictionary with a list of relevant
#stock information associated with each stock key
def stock_groups(stock_list, sorting_key, value1, value2):
    sorted_stock = sorted(stock_list, key=itemgetter(sorting_key))
    stock_dict = {}
    stocks_per_key = []
    key_list = unique_keys(sorted_stock, sorting_key)  # get the list of individual stocks
    start = 0
    for key in key_list:
        for i in range(start, len(sorted_stock)):
            if sorted_stock[i][sorting_key] == key:
                stock_value = [sorted_stock[i][value1], sorted_stock[i][value2]]
                stocks_per_key.append(stock_value)
            else:
                break
        stock_dict[key] = stocks_per_key
        start += len(stocks_per_key)
        stocks_per_key = []
    return stock_dict


#formatting for the print out of stock data
def print_stocks(stock_dict):
    for key, value in stock_dict.items():
        print('{}:'.format(key))
        for item in value:
            print('\t{} - {}'.format(item[0], str(item[1])))


#main program calls
stocks_by_symbol = stock_groups(stock_data, INDEX_SYMBOL, INDEX_DATE, INDEX_AMOUNT)
stocks_by_date = stock_groups(stock_data, INDEX_DATE, INDEX_SYMBOL, INDEX_AMOUNT)
print("Stocks by Ticker:")
print_stocks(stocks_by_symbol)
print("stocks by Date:")
print_stocks(stocks_by_date)
