ticker_file = 'tickers'

def read_lines(file):
    """
    reads the document. Places each line as an element in a list.
    """
    with open(file) as infile:
        lines_list = infile.readlines()
    return lines_list


def tickers_to_dict(file):
    """
    Takes a file with companies and their ticker symbol as input. Returns a dict with the same information. Company name
    is the key, ticker the value.
    """
    lines_list = read_lines(file)
    ticker_dict = {}
    for line in lines_list:
        company, ticker = line.split(sep=':')
        ticker_dict[company] = ticker
    return ticker_dict


def name_to_symbol(name_company, ticker_dict):
    """
    takes a company name and a dictionaty with ticker symbools as input. Finds the tickersymbol of the company and
    returns it.
    """
    return ticker_dict[name_company]


def symbol_to_name(symbol, ticker_dict):
    """
    takes a ticker symbol and a dictionaty with ticker symbools as input. Finds the company name associated with the
    ticker symbol and returns it.
    """
    for name_company, ticker in ticker_dict.items():
        if ticker[-1:] == '\n':
            ticker = ticker[:-1]
        if ticker == symbol:
            return name_company

if __name__ == '__main__':
    tickers = tickers_to_dict(ticker_file)

    name = input('Enter Company name: ')
    print("Ticker symbol: {}".format(name_to_symbol(name, tickers)))

    symbol = input('Enter Ticker symbol: ')
    print("Company name: {}".format(symbol_to_name(symbol, tickers)))
