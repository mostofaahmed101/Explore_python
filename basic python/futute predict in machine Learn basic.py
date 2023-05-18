import pandas as pd
import sklearn.linear_model as skllm


file1 = pd.read_csv('basic python\my_data.csv')

x = file1[['year']]
y = file1['rate']

Reg = skllm.LinearRegression()
Reg.fit(x, y)
inp_pre = int(input("which year you want to predict: "))
print(Reg.predict([[inp_pre]]))




