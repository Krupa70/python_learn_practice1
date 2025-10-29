import pandas as pd

# Read specific columns and set index
df = pd.read_excel('employees.xlsx', sheet_name='Data', 
                   usecols=['ID', 'Name', 'Salary'], index_col='ID')
print(df.head())