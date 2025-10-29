import pandas as pd
my_data = [['Krupa', 42, 210.0], 
           ['Riya', 25, 103.25], 
           ['Ram', 36, 150.50]]

my_index = ['row1', 'row2', 'row3']
my_column_index = ['Name', 'Age', 'Score']

d1 = pd.DataFrame(my_data, index=my_index,columns=my_column_index)



print(d1)
empty_line = "\n-------------------------------------"

def print_loc_examples():
    print( d1.loc['row2', 'Age'], empty_line)  # access by label
    print(d1.loc['row2'], empty_line)        # access entire row by label
    print( d1.loc[:, 'Age'], empty_line)     # access entire column by label

def print_iloc_examples():
    empty_line = "\n*************************************"
    print(empty_line)
    print( d1.iloc[1, 1], empty_line)         # access by position
    print( d1.iloc[1], empty_line)         # access entire row by position
    print( d1.iloc[:, 1], empty_line)         # access entire column by position

def print_at_examples():
    empty_line = "\n#####################################"
    print( d1.at['row2', 'Age'], empty_line)  # access by label
    print( d1.at['row3', 'Score'], empty_line)  # access by label

def print_iat_examples():
    empty_line = "\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
    print( d1.iat[1, 1], empty_line)         # access by position
    print( d1.iat[2, 2], empty_line)         # access by position


d2 = pd.DataFrame(my_data)


if __name__ == "__main__":
   print(d2, empty_line)
   print( d2.loc[1, 1], empty_line)  # access by label
