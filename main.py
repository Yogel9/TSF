# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # load dataset
    def parser(x):
        return datetime.strptime('190' + x, '%Y-%m')
    series = read_csv('shampoo-sales.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
    # summarize first few rows
    print(series.head())
    # line plot
    series.plot()
    pyplot.show()


