import numpy as np 
import scipy.stats as sp_st
import matplotlib.pyplot as mpl_pp
import pandas as pd 
import sklearn.tree as slt
from sklearn.tree import DecisionTreeClassifier as sltD
from sklearn import linear_model, datasets
from sklearn.metrics import mean_squared_error




x1 = [12,55,64,77,45,76,88,99,45,66,12,56,76,89,23,45,66]
print(len(x1))
print(np.mean(x1))
print(np.median(x1))
print(sp_st.mode(x1))

print(np.percentile(x1, 80))



x2 = [43,57,86,97,12,45,56,29]
print(np.std(x2))
print(np.var(x2))



                            # Linear Reggration

x3 = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y3 = [99,86,87,88,111,86,103,87,94,78,77,85,86]
slope, intercept, r, p, std_err = sp_st.linregress(x3, y3)    # this code give us the 5 value for 5 variable
linre = [slope, intercept, r, p, std_err]
print("linregress : ", linre)
Linear_reg = []
for XXI in x3:
    abcX3 = XXI * slope + intercept
    Linear_reg.append(abcX3)
# mpl_pp.scatter(x3, y3)
# mpl_pp.plot(x3, Linear_reg)
# mpl_pp.show()

               # future predict by Linear Reggration

# x4 = int(input("your future VAlue: "))
# print(x4 * slope + intercept)



                    #  Linear Reggration  2.0

doc = pd.read_csv("basic python\my_data.csv")

doc_train_x = doc["year"][:15, np.newaxis]
doc_train_y = doc["rate"][:15]

doc_test_x = doc["year"][15:, np.newaxis]
doc_test_y = doc["rate"][15:]

reg = linear_model.LinearRegression()
reg.fit(doc_train_x, doc_train_y)

print("Result :", reg.predict(doc_test_x))
print("slope :", reg.coef_)
print("intercept :", reg.intercept_)





                        # polynomial Regression by Train/Test

x5 = np.random.normal(3,1,150)
y5 = np.random.normal(200,50,150)

trainX = x5[:80]
trainY = y5[:80]

testX = x5[80:]
testY = y5[80:]

ttpr_func = np.poly1d(np.polyfit(trainX, trainY, 4))
ttpr_line = np.linspace(0,7,150)
# mpl_pp.scatter(trainX, trainY)
# mpl_pp.plot(ttpr_line, ttpr_func(ttpr_line))

# mpl_pp.show()






                    #  Decision  Tree
file1 = pd.read_csv("basic python\my_data_2.csv")
# print(file1)

PN_change = {"Bangladesh":101, "india":102, "canada":103, "korea":104}
PS_change = {"YES":1, "NO":0}
file1["produce Name"] = file1["produce Name"].map(PN_change)
file1["profit states"] = file1["profit states"].map(PS_change)
# print(file1)

Dfeature = ["year", "rate", "produce Name"]
x6 = file1[Dfeature]
y6 = file1["profit states"]

Dtree = sltD().fit(x6, y6)
slt.plot_tree(Dtree, feature_names=Dfeature)
print("Predict by Decision tree: ", Dtree.predict([[2021,550,101]]))



