import pandas as pd

data = {
    'Name': ['John', 'Riya', 'Amit', 'Sara', 'Leo'],
    'Age': [25, 19, 30, 22, 17],
    'Marks': [85, 90, 70, 95, 60]
}

df = pd.DataFrame(data)
print(df)

filter_logic1 = ('(Age > 20 & Marks >= 80)  | Name == "Leo"')

filter_logic2 = df[df['Name'].isin(['Riya', 'Leo'])]

filter_logic3 = df[df['Age'].between(18,25)]

filter_logic4 = df[df['Name'].str.startswith('J')]

filter_logic5 = df.loc[df['Age'].between(18,25), ['Name', 'Age']]

filter_logic6 = df.loc[ [0,1], ['Name', 'Age']]

def calculate_amount(x, n, z):
    return x['Age'] * n + z
filter_logc7 = df.apply(calculate_amount, args=(2, 5), axis=1)

print("-------------------  Filter Logic 1 -------------------")
print(filter_logc7)

#print(df[(df['Age'] >20) & (df['Marks'] >= 80)])

