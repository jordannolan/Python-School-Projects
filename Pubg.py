# I have to run this program threw the terminal for pycharm can not import sklearn package
import numpy
import matplotlib.pyplot as pyplot
import pandas
from sklearn import linear_model, metrics
from sklearn.model_selection import KFold

data = pandas.read_csv('./PubgData.csv')

training_data_size = 10000
training_data = data.iloc[0:training_data_size, [3, 14]].as_matrix()

training_array = numpy.array(training_data)
training_x = training_array[:,0].reshape(training_data_size, 1)
training_y = training_array[:,1].reshape(training_data_size, 1)

regression = linear_model.LinearRegression()

regression.fit(training_x, training_y)
prediction_y = regression.predict(training_x)

pyplot.scatter(training_x, training_y, color='green')
pyplot.plot(training_x, prediction_y, color='black', linewidth=3)

print("Mean squared error: %.2f" % metrics.mean_squared_error(prediction_y,
training_y))

pyplot.show()

average = 0.0
#KFold training testing #7
kf = KFold(n_splits=5)
for train_index, test_index in kf.split(training_x):
    print("TRAIN:", train_index, "TEST:", test_index)
    x_train, X_test = training_x[train_index], training_x[test_index]
    y_train, y_test = training_y[train_index], training_y[test_index]

    prediction_y = regression.predict(x_train)
    average += metrics.mean_squared_error(prediction_y, y_train)

average = average / kf.get_n_splits(x_train)
print(" KFold Average error: " + str(average))


