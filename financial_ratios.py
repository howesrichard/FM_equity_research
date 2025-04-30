import yfinance as yf

class Stock:
    def __init__(self, ticker: str):
        """
        Initializes the Stock object with a given ticker symbol.

        Args:
            ticker (str): The stock ticker symbol.
        """
        self.ticker = ticker
        self.stock = yf.Ticker(ticker)
        self.info = self.stock.info

    def get_forward_pe(self):
        """
        Retrieves the forward P/E ratio.

        Returns:
            float: The forward P/E ratio.
        """
        return self.info.get("forwardPE")

    def get_debt_to_equity(self):
        """
        Retrieves the debt-to-equity ratio.

        Returns:
            float: The debt-to-equity ratio.
        """
        return self.info.get("debtToEquity")

    def get_return_on_equity(self):
        """
        Retrieves the return on equity ratio.

        Returns:
            float: The return on equity ratio.
        """
        return self.info.get("returnOnEquity")*100

    def get_operating_margin(self):
        """
        Retrieves the operating margin.

        Returns:
            float: The operating margin.
        """
        return self.info.get("operatingMargins")*100

    def get_dividend_yield(self):
        """
        Retrieves the dividend yield.

        Returns:
            float: The dividend yield.
        """
        return self.info.get("dividendYield")