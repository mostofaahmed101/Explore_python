                                        #  MNIST


#  source link : https://www.codewithharry.com/videos/ml-tutorials-in-hindi-21/




import matplotlib.pyplot as mpl_pp
from sklearn import datasets, linear_model, model_selection
import numpy as np 
import matplotlib as mpl

data1 = datasets.fetch_openml("mnist_784")
x,y = data1['data'], data1['target']

# digit = x.to_numpy()[101]
# digit_img = digit.reshape(28,28)
# mpl_pp.imshow(digit_img, cmap=mpl.cm.binary, interpolation='nearest')
# mpl_pp.show()

x_train, x_test = x[:6000],x[6000:6500]
y_train, y_test = y[:6000],y[6000:6500]

# shuffle_index = np.random.permutation(60000)      
# x_train, y_train = x_train.[shuffle_index], y_train.[shuffle_index]     # something wrong is here

y_train, y_test = y_train.astype(np.int8), y_test.astype(np.int8)
y_train, y_test = (y_train=='2'), (y_test==2)

reg = linear_model.LogisticRegression()
reg.fit(x_train, y_train)
pred = reg.predict([[101]])
print(pred)