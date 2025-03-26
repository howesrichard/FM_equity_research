import unittest
from src.company_selection import select_company

class TestCompanySelection(unittest.TestCase):

    def test_select_company_valid(self):
        # Assuming 'AAPL' is a valid ASX code for testing
        company_data = select_company('AAPL')
        self.assertIsNotNone(company_data)
        self.assertEqual(company_data['code'], 'AAPL')

    def test_select_company_invalid(self):
        # Test with an invalid ASX code
        company_data = select_company('INVALID_CODE')
        self.assertIsNone(company_data)

    def test_select_company_empty_input(self):
        # Test with empty input
        company_data = select_company('')
        self.assertIsNone(company_data)

if __name__ == '__main__':
    unittest.main()