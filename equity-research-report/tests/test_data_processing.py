import unittest
from src.data_processing import fetch_financial_data, compute_ratios

class TestDataProcessing(unittest.TestCase):

    def test_fetch_financial_data(self):
        # Test fetching financial data for a valid company
        data = fetch_financial_data("AAPL")
        self.assertIsInstance(data, dict)
        self.assertIn("revenue", data)
        self.assertIn("net_income", data)

    def test_fetch_financial_data_invalid(self):
        # Test fetching financial data for an invalid company
        data = fetch_financial_data("INVALID")
        self.assertIsNone(data)

    def test_compute_ratios(self):
        # Test computing financial ratios
        financials = {
            "revenue": 100000,
            "net_income": 20000,
            "total_assets": 500000,
            "total_liabilities": 300000
        }
        ratios = compute_ratios(financials)
        self.assertIn("profit_margin", ratios)
        self.assertIn("debt_to_equity", ratios)
        self.assertAlmostEqual(ratios["profit_margin"], 0.2)
        self.assertAlmostEqual(ratios["debt_to_equity"], 1.0)

if __name__ == '__main__':
    unittest.main()