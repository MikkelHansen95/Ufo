'''
Usage: 
    python main.py [<url>]
Example:
   python main.py https://raw.githubusercontent.com/planetsig/ufo-reports/master/csv-data/ufo-scrubbed-geocoded-time-standardized.csv
'''

import os
import sys
import csv
from lib.converter import convert
from lib.download import download
import lib.statistic as stat
import lib.plotting as plotter

if __name__ == '__main__':
    print("\nPlain Product Ufo Analyzer:")

    file_dir = 'csv'
    # If the csv directory doesn't already exits it will be created.
    if not os.path.isdir(file_dir):
        os.makedirs(file_dir)
    try:
        _, url = sys.argv
        file_name = os.path.join(file_dir, os.path.basename(url))
        print(f'\nDownloading file : {os.path.basename(url)} ...')
        download(url, file_name)  
        print('Download completed succesfully!')
    except Exception as e:
        print(__doc__)
        sys.exit(1)  

    # After downloading the csv file we use our own converter to read the file and clean it up. 
    # We filter some data away in order to represent our data in away we find more easy to work with
    data_set = []

    with open('csv/ufo-scrubbed-geocoded-time-standardized.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        csv_array = []
        list_with_dates = []
        for line in csv_reader:
          csv_array.append(line)

        for i in csv_array:
            if '24:00' in i[0]:
                replaced = i[0].replace('24:00','00:00')
                temp = i
                temp[0] = replaced
                data_set.append(temp)
            else:
                data_set.append(i)

    print(stat.count_ufo_spotted(data_set))
    ufo_spots_evolution = stat.ufo_spotted_over_time(data_set)
    plotter.plot_evolution_of_spotters(ufo_spots_evolution)
    seasons = stat.which_season_is_most_common(data_set)
    plotter.plot_season_most_common(seasons)
    print(stat.how_does_an_ufo_look(data_set))
    #print(stat.how_long_was_ufo_spotted(data_set))
    df = stat.which_weekday_ufo_spotted(data_set)
    plotter.plot_weekday_spots(df)
    sentiment = stat.sentiment(data_set)
    plotter.plot_sentiment(sentiment)