import yfinance as yf
import pandas as pd
from pprint import pprint


def get_sector_info_for_stock(ticker_symbol):
    """
    Fetch sector information for a given stock ticker symbol using yfinance.

    Args:
        ticker_symbol (str): The ticker symbol of the stock.

    Returns:
        dict: A dictionary containing sector information.
    """
    try:
        stock = yf.Ticker(ticker_symbol)
        sector = yf.Sector(stock.info.get('sectorKey'))
        sector_report  = {
            'overview': sector.overview,
            'research_reports': sector.research_reports,
        }
        return sector_report
    except Exception as e:
        print(f"Error fetching sector information for {ticker_symbol}: {e}")
        return None

def get_sector_info(sector_name):
    """
    Fetch sector information using yfinance.
    The possibel values for sector_name are:
    - basic-materials 
    - communication-services
    - consumer-cyclical
    - consumer-defensive
    - energy
    - financial-services
    - healthcare
    - industrials
    - real-estate
    - technology
    - utilities

    Args:
        sector_name (str): The name of the sector.

    Returns:
        dict: A dictionary containing sector information.
    """
    try:
        sector = yf.Sector(sector_name)
        sector_report  = {
            'overview': sector.overview,
            'research_reports': sector.research_reports,
        }
        return sector_report
    except Exception as e:
        print(f"Error fetching sector information for {sector_name}: {e}")
        return None
