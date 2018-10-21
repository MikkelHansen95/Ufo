'''
    Create plots to be stored in files.
'''

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import os
import matplotlib.dates as mdates
import pandas as pd
import matplotlib.ticker as ticker
import seaborn as sns; sns.set()

def plot_evolution_of_spotters(list_of_spots):
    plot_file = f'plot0.png'
    plot_dir = 'plots'
    # If the plot directory is not already present it will be created.
    if not os.path.isdir(plot_dir):
        os.makedirs(plot_dir)

    lists = sorted(list_of_spots.items())
    x, y = zip(*lists)
    tick_spacing = 3
    fig, ax = plt.subplots(1,1)
    ax.plot(x,y)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    plt.xticks(rotation=90, fontsize=8)
    
    plt.savefig(os.path.join(plot_dir, plot_file))
    plt.show()
    plt.close()

def plot_season_most_common(seasons_number):
    plot_file = f'plot1.png'
    plot_dir = 'plots'
    # If the plot directory is not already present it will be created.
    if not os.path.isdir(plot_dir):
        os.makedirs(plot_dir)

    seasons_name = ('Winter', 'Spring', 'Summer', 'Fall')
    y_pos = np.arange(len(seasons_name))
    plt.bar(y_pos, seasons_number, align='center', alpha=0.5)
    plt.xticks(y_pos, seasons_name)
    plt.ylabel('Spots')
    plt.title('Ufo spotted each seasons')
 
    plt.savefig(os.path.join(plot_dir, plot_file))
    plt.show()
    plt.close()

def plot_weekday_spots(df):
    plot_file = f'plot2.png'
    plot_dir = 'plots'
    # If the plot directory is not already present it will be created.
    if not os.path.isdir(plot_dir):
        os.makedirs(plot_dir)
    
    
    ax = df.plot.scatter(x='weekdays', y='count')
    
    labels = [item.get_text() for item in ax.get_xticklabels()]
    labels[1] = 'Monday'
    labels[2] = 'Tuesday'
    labels[3] = 'Wednesday'
    labels[4] = 'Thursday'
    labels[5] = 'Friday'
    labels[6] = 'Saturday'
    labels[7] = 'Sunday'
    ax.set_xticklabels(labels)
    ax.yaxis.set_major_formatter(ticker.PercentFormatter())
    ax.set_ylim(0,1)

    plt.savefig(os.path.join(plot_dir, plot_file))
    plt.show()
    plt.close()
 

def plot_sentiment(list_of_sentiment):
    plot_file = f'plot3.png'
    plot_dir = 'plots'
    # If the plot directory is not already present it will be created.
    if not os.path.isdir(plot_dir):
        os.makedirs(plot_dir)

    list_of_polarity = []
    list_of_subjectivity = []
    

    for i in list_of_sentiment[:50]:
        list_of_polarity.append(i[0])
        list_of_subjectivity.append(i[1])

    x = list(range(0,len(list_of_polarity)))
    x1 = list(range(0,len(list_of_subjectivity)))
    plt.plot(x,list_of_polarity,'-ok',color='black')
    plt.plot(x1,list_of_subjectivity,'-ok',color='red')

    
    plt.savefig(os.path.join(plot_dir, plot_file))
    plt.show()
    plt.close()