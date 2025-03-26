# filepath: equity-research-report/equity-research-report/src/main.py

def main():
    print("Welcome to the Equity Research Report Generator!")
    
    # Step 1: User input for company selection
    asx_code = input("Please enter the ASX code of the company you want to research: ")
    
    # Step 2: Company selection logic
    from company_selection import select_company
    company_data = select_company(asx_code)
    
    if company_data is None:
        print("Company not found. Please check the ASX code and try again.")
        return
    
    # Step 3: Fetch financial data
    from data_processing import fetch_financial_data
    financial_data = fetch_financial_data(company_data)
    
    # Step 4: Generate the report
    from report_generator import ReportGenerator
    report_generator = ReportGenerator()
    report = report_generator.generate_report(company_data, financial_data)
    
    # Step 5: Save the report as a PDF
    report_generator.save_report(report)
    
    print("The equity research report has been generated successfully!")

if __name__ == "__main__":
    main()