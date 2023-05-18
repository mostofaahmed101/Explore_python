import matplotlib.pyplot as mpl_pp
import numpy as np 
from sklearn import linear_model, datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_squared_error
import pandas as pd 




# doc = datasets.load_diabetes()
# doc_data = doc.data

# doc_train_x = doc_data[:-20]
# doc_test_x = doc_data[-20:]

# doc_train_y = doc.target[:-20]
# doc_test_y = doc.target[-20:]



# doc = pd.read_csv("basic python\my_data.csv")

# doc_train_x = doc["year"][:15, np.newaxis]
# doc_train_y = doc["rate"][:15]

# doc_test_x = doc["year"][15:, np.newaxis]
# doc_test_y = doc["rate"][15:]


# reg = linear_model.LinearRegression()
# reg.fit(doc_train_x, doc_train_y)

# print("Result :", reg.predict(doc_test_x))
# print("slope :", reg.coef_)
# print("intercept :", reg.intercept_)

# mpl_pp.scatter(doc_train_x, doc_train_y)
# mpl_pp.plot(doc_train_x,)
# mpl_pp.show()





                    # k nearest / classification

# docI = datasets.load_iris()
# features = docI.data
# label = docI.target
# Classifier = KNeighborsClassifier()
# Classifier.fit(features, label)
# print("Classifier predict is" , Classifier.predict([[6.8, 8.8, 3.5, 0.9]]))
# # print(docI.DESCR)





                #  Logistic Regression classifer

# file101=datasets.load_iris()
# x101= file101.data[:, 3:]
# y101= (file101.target == 2).astype(np.int)

# l_c101= linear_model.LogisticRegression()
# l_c101.fit(x101, y101)
# print(l_c101.predict([[0.9]]))
# # print(y101)

# x101New = np.linspace(0,4,1000).reshape(-1,1)
# y101New = l_c101.predict_proba(x101New)
# mpl_pp.plot(x101New,y101New[:,1], "-")
# mpl_pp.show()














                            # next level ML

























