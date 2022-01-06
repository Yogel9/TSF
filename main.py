# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from math import sqrt
from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from sklearn.metrics import mean_squared_error
from pandas import DataFrame
from pandas import concat

def make_rmse(test,predictions):
    rmse = sqrt(mean_squared_error(test, predictions))
    print('RMSE: %.3f' % rmse)

def parser(x):
    return datetime.strptime('190' + x, '%Y-%m')

# frame a sequence as a supervised learning problem
def timeseries_to_supervised(data, lag=1):
	df = DataFrame(data)
	columns = [df.shift(i) for i in range(1, lag+1)]
	columns.append(df)
	df = concat(columns, axis=1)
	df.fillna(0, inplace=True)
	return df

def persistence_foracasting(X):
    # split data into train and test
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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # load dataset
    series = read_csv('shampoo-sales.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
    # split data into train and test
    X = series.values
    supervised = timeseries_to_supervised(X, 1)
    print(supervised.head())

