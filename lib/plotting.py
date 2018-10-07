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


def plot(serie):

    plot_file = f''
    plot_dir = 'plots'
    # If the plot directory is not already present it will be created.
    if not os.path.isdir(plot_dir):
        os.makedirs(plot_dir)

    serie.plot()
    
    plt.show()

    print("\nPlot saved in plots folder as '"  "'.")

def plot2(df):
    plot_file = f''
    plot_dir = 'plots'
    # If the plot directory is not already present it will be created.
    if not os.path.isdir(plot_dir):
        os.makedirs(plot_dir)
    df.plot(x='release_date', y='runtime', marker='.', linewidth=0)
    plt.show()