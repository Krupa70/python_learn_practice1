import pandas as pd
import numpy as np


d1 = pd.DataFrame({'Name':['John','Riya'], 'Age':[18,19]})
print(d1)
print("-------------------------------------")

d2 = pd.DataFrame([[1,2,3],[4,5,6]])
print(d2)
print("-------------------------------------")

s1 = pd.Series([10,20], index=['a','b'])
s2 = pd.Series([30,40], index=['a','b'])
d3 = pd.DataFrame({'Age':s1, 'Salary':s2})
print(d3)
print("-------------------------------------")

d4 = pd.DataFrame(np.array([[1,2],[3,4]]))
print(d4)
print("-------------------------------------")

d5 = pd.DataFrame([{'a':1,'b':2}, {'a':3,'b':4}])
print(d5)
print("-------------------------------------")