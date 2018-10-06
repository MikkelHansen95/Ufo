'''
    Create plots to be stored in files 
'''

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import os
import matplotlib.dates as mdates
import pandas as pd
import matplotlib.ticker as ticker

# This functions take the data_set, a state, a cause, start year and end year and plots the annual increase in death.


def plot(x, y, y2):

    plot_file = f''
    plot_dir = 'plots'
    # If the plot directory is not already present it will be created.
    if not os.path.isdir(plot_dir):
        os.makedirs(plot_dir)

    #bins = [0, 30, 60, 90 ,120, 150, 180, 210, 240, 270, 300, 365]
    #plt.hist(no_movies_rday, bins, histtype='bar')
    '''
    plt.bar(x,y)
    plt.xlabel('Days')
    plt.xticks()
    plt.ylabel('Number of releases')
    plt.show()
    '''

    ax = plt.subplot()
    ax.plot(x, y)
    plt.show()

print("\nPlot saved in plots folder as '"  "'.")
