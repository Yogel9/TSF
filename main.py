# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from math import sqrt
from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from sklearn.metrics import mean_squared_error

def make_rmse(test,predictions):
    rmse = sqrt(mean_squared_error(test, predictions))
    print('RMSE: %.3f' % rmse)

def parser(x):
    return datetime.strptime('190' + x, '%Y-%m')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # load dataset
    series = read_csv('shampoo-sales.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
    # split data into train and test
    X = series.values
    train, test = X[0:-12], X[-12:]
    # walk-forward validation
    history = [x for x in train]
    predictions = list()
    for i in range(len(test)):
        # make prediction...
        predictions.append(history[-1])
        # observation
        history.append(test[i])
    # report performance
    rmse = sqrt(mean_squared_error(test, predictions))
    print('RMSE: %.3f' % rmse)
    # line plot of observed vs predicted
    pyplot.plot(test)
    pyplot.plot(predictions)
    pyplot.show()

