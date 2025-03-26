import unittest
from src.report_generator import ReportGenerator

class TestReportGenerator(unittest.TestCase):

    def setUp(self):
        self.report_generator = ReportGenerator()

    def test_generate_report(self):
        # Assuming generate_report returns a boolean indicating success
        result = self.report_generator.generate_report("Sample Company", "Sample Data")
        self.assertTrue(result)

    def test_format_report(self):
        # Assuming format_report returns a formatted string
        formatted_report = self.report_generator.format_report("Sample Data")
        self.assertIsInstance(formatted_report, str)
        self.assertIn("<html>", formatted_report)
        self.assertIn("</html>", formatted_report)

if __name__ == '__main__':
    unittest.main()