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


#create a list of unique stocks to later be used as the keys
#for the dictionary of stock tickers per stock
def stock_keys(stock_list):
    unique = []
    for stock in stock_list:
        if stock[1] not in unique:
            unique.append(stock[1])
    return unique


#compile the list of stocks into a dictionary with a list of relevant
#stock information associated with each stock key
def stock_groups(stock_list):
    stock_dict = {}
    stocks_per_key = []
    key_list = stock_keys(stock_list)  # get the list of individual stocks
    for key in key_list:
        for i in range(0, len(stock_list)):
            if stock_list[i][1] == key:
                stock_value = [stock_list[i][0], stock_list[i][2]]
                stocks_per_key.append(stock_value)
        stock_dict[key] = stocks_per_key
        stocks_per_key = []
    return stock_dict


#formatting for the print out of stock data
def print_stocks(stock_dict):
    for key, value in stock_dict.items():
        print('{}:'.format(key))
        for item in value:
            print('\t{} - {}'.format(item[0], str(item[1])))


#main program calls
my_stocks = stock_groups(stock_data)
print_stocks(my_stocks)
