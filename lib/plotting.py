'''
    Create plots to be stored in files 
'''

import matplotlib.pyplot as plt
import numpy as np
import os

# This functions take the data_set, a state, a cause, start year and end year and plots the annual increase in death.
def plot():
  
    plot_file = f''
    plot_dir = 'plots'
    # If the plot directory is not already present it will be created.
    if not os.path.isdir(plot_dir):
        os.makedirs(plot_dir)

    
    print("\nPlot saved in plots folder as '" + plot_file + "'.")
