from mcp.server.fastmcp import FastMCP
from tools.sector_tools import  get_sector_info_for_stock as raw_sector_info_stock, get_sector_info as raw_sector_info

from tools.stock_tools import  get_stock_info as raw_stock_info, get_stock_news as raw_stock_news,get_ticker as raw_get_ticker, get_last_2_months_trends as raw_stock_trends
import argparse

mcp = FastMCP("Financial Analysis Server")

@mcp.tool(description="Fetch sector analysis for a stock using its ticker symbol")
def get_sector_info_for_stock(ticker_symbol: str) -> dict:
    """Fetch sector analysis for a stock using its ticker symbol"""
    return raw_sector_info_stock(ticker_symbol)

@mcp.tool(description="""Fetch comprehensive sector data, the possible vaues are energy, basic-materials, technology, 
financial-services, healthcare, industrials, real-estate, utilities, consumer-defensive, consumer-cyclical, """)
def get_sector(sector_name: str) -> dict:
    """Retrieve comprehensive sector data (basic-materials, technology, etc.)"""
    return raw_sector_info(sector_name)

@mcp.tool(description="Fetch detailed stock information using its ticker symbol")
def stock_profile(ticker_symbol: str) -> dict:
    """Get detailed profile information for a stock"""
    return raw_stock_info(ticker_symbol)

@mcp.tool(description="Fetch recent news articles related to a stock using its ticker symbol")
def stock_news(ticker_symbol: str) -> list[dict]:
    """Fetch recent news articles related to a stock"""
    return raw_stock_news(ticker_symbol)

@mcp.tool(description="Convert company name to stock ticker symbol")
def find_ticker(company_name: str) -> str:
    """Convert company name to stock ticker symbol"""
    return raw_get_ticker(company_name)

@mcp.tool(description="Retrieve 2-month price history with ticker symbol")
def price_history(ticker_symbol: str) -> list[dict]:
    """Retrieve 2-month price history with OHLC data"""
    return raw_stock_trends(ticker_symbol)


if __name__ == "__main__":
    # Start the server
    print("🚀Starting server... ")

    # Debug Mode
    #  uv run mcp dev server.py

    # Production Mode
    # uv run server.py --server_type=sse


    #args = parser.parse_args()
    mcp.run(transport="sse")