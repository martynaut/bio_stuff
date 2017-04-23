"""Module for simple plotting."""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def import_data_file(name):
    """Importing data."""
    if name[-3:] == 'csv':
        df = pd.read_csv(name)
    if name[-3:] == 'xls' or name[-4:] == 'xlsx':
        df = pd.read_excel(name)
    # print(df.head())
    return df


def plot_draw(name, type='line', color=0, title='title', xlabel='xlabel',
              ylabel='ylabel', xscale='default', yscale='default'):
    """Main plotting function."""
    df = import_data_file(name)
    xvalues = np.arange(1, len(df.index)+1)
    for column in df.columns:
        # print(column)
        plt.plot(xvalues, df[column])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    return 'success'

# simple import test
import_data_file('asd.csv')
import_data_file('asd.xls')
import_data_file('asd.xlsx')

# simple plot test
print(plot_draw('asd.csv'))
