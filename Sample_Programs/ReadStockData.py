"""Utility functions"""

import os
import pandas as pd

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        # TODO: Read and join data for each symbol
        df1 = pd.read_csv(symbol_to_path(symbol),na_filter=True,parse_dates=True, index_col='Date',usecols=['Date','Adj Close'])
        
        df1.rename(columns={'Adj Close':symbol})
        df= df.join(df1)
        if symbol == "SPY"
            df=df.dropna(subset=["SPY"]);
        print( df1)
        #df = df.join(df1,how='inner') 
    return df


def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-22', '2010-01-26')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']
    
    # Get stock data
    df = get_data(symbols, dates)
    print( df)


if __name__ == "__main__":
    test_run()
