import yfinance as yf
import pandas as pd 
from pprint import pprint
def get_stock_info(ticker_symbol):
    """
    Fetch stock information using yfinance.

    Args:
        ticker_symbol (str): The ticker symbol of the stock.

    Returns:
        dict: A dictionary containing stock information.
    """
    try:
        stock = yf.Ticker(ticker_symbol)
        info = stock.info
        return info
    except Exception as e:
        print(f"Error fetching stock information for {ticker_symbol}: {e}")
        return None

def get_stock_news(ticker_symbol):
    """
    Fetch stock news using yfinance.

    Args:
        ticker_symbol (str): The ticker symbol of the stock.

    Returns:
        list: A list of news articles related to the stock.
    """
    try:
        stock = yf.Ticker(ticker_symbol)
        news = stock.news
        news = [{
            'title': article['content']['title'],
            'summary': article['content']['summary'],
            'published_at': article['content']['pubDate']
        } for article in news]
        return news
    except Exception as e:
        print(f"Error fetching stock news for {ticker_symbol}: {e}")
        return None

def get_ticker(company_name: str):
    """
    Fetch ticker symbol for a given company name

    Args:
        company_name (str): The search term for the stock.

    Returns:
        str: The ticker symbol of the stock.
    """
    try :
        stock = yf.Search(company_name).quotes[0]['symbol']
        return stock
    except Exception as e:
        raise ValueError(f"Error fetching ticker symbol for {company_name}: {e}")

def get_last_2_months_trends(ticker_symbol):
    """
    Fetch the last 3 months of stock data.

    Args:
        ticker_symbol (str): The ticker symbol of the stock.

    Returns:
        pd.DataFrame: A DataFrame containing the last 3 months of stock data.
    """
    try:
        stock = yf.Ticker(ticker_symbol)
        data = stock.history(period='2mo')
        data = data.to_dict(orient='records')
        return data
    except Exception as e:
        print(f"Error fetching last 3 months of stock data for {ticker_symbol}: {e}")
        return None
    

if __name__ == '__main__':
    ticker = get_ticker("Apple Inc")
    stock_info = get_stock_info(ticker)
    if stock_info:
        pprint(stock_info)
    stock_news = get_stock_news(ticker)
    if stock_news:
        pprint(stock_news)
    else:
        print("No news found.")