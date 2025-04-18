import pandas as pd

# URL of the webpage containing the dividend table
url = "https://www.bendigoadelaide.com.au/investor-centre/dividends/fully-paid-ordinary-shares/"

# Read all tables from the webpage
tables = pd.read_html(url)

# Assuming the first table is the dividend history table
df = tables[0]

# Display the DataFrame
print(df.head())
