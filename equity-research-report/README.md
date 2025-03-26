# Equity Research Report Program

This project is designed to generate comprehensive equity research reports in PDF format. The reports include various financial metrics, recommendations, commentary, charts, and functionality for selecting companies based on ASX codes.

## Features

- **Financial Metrics**: Fetch and compute key financial ratios and metrics from an API.
- **Company Selection**: Select companies using their ASX codes and retrieve relevant data.
- **Report Generation**: Generate well-structured and visually appealing PDF reports.
- **Charting**: Create visual representations of stock price history and market performance.
- **Commentary**: Import and include commentary in the reports.

## Project Structure

```
equity-research-report
├── src
│   ├── main.py                # Entry point for the application
│   ├── report_generator.py     # Handles report generation
│   ├── data_processing.py      # Fetches and processes financial data
│   ├── charting.py            # Creates charts for the report
│   ├── company_selection.py     # Manages company selection logic
│   └── utils
│       └── helpers.py         # Utility functions
├── templates
│   └── report_template.html    # HTML template for the PDF report
├── tests
│   ├── test_report_generator.py # Unit tests for report generation
│   ├── test_data_processing.py  # Unit tests for data processing
│   ├── test_charting.py        # Unit tests for charting functions
│   └── test_company_selection.py # Unit tests for company selection
├── requirements.txt            # Project dependencies
├── .gitignore                  # Files to ignore in version control
└── README.md                   # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd equity-research-report
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/main.py
   ```

## Usage Guidelines

- Follow the prompts in the application to select a company and generate a report.
- Ensure that the necessary API keys and configurations are set up in the environment.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.