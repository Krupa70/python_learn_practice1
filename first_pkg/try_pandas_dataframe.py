
import pandas as pd
#data 
my_data =  {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
                            'Age': [24, 27, 22, 32, 29],
                            'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
                            'Score': [85.5, 90.0, 78.5, 88.0, 92.5]}
#data frame
my_frame = pd.DataFrame(my_data)
print (my_frame)

def display_series_info(series):
    print("Series Name:", series.name)
    print("Series Index:", series.index.tolist())
    print("Series Values:", series.values.tolist())
    print("Series Description:\n", series.describe())

if __name__ == "__main__":
  #  print(f" print records where Age > 25 \n {my_frame[my_frame['Age'] > 25]}") 
    print("Age", my_frame.loc[0,'Age'] )
    print("Age", my_frame.iloc[0, 1] )