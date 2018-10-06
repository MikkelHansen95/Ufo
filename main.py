'''
Usage: 
    python main.py [<url>]
Example:
   python main.py https://raw.githubusercontent.com/MikkelHansen95/dataset/master/movies_metadata.csv
'''

import os
import sys
from lib.converter import convert
from lib.download import download
import lib.statistic as stat
import lib.plotting as plotter

if __name__ == '__main__':
    print("\nPlain Product Movie Analyzer:")
    file_dir = 'csv'
    # If the csv directory already exits it will be created
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
    data_set = convert(file_name)

    # print(data_set[0][2][0])
    print(stat.count_adult_movies(data_set))
    print(stat.count_animation_movies(data_set))
    print(stat.find_biggest_budget(data_set))
    print(stat.most_popular(data_set,'Denmark'))
    print(stat.find_biggest_revenue(data_set,'United Kingdom'))


    #plot 1
    dates = stat.get_all_dates_in_year()
    non_adult_rd = stat.get_release_dates(data_set,'False')
    adult_rd = stat.get_release_dates(data_set,'True')
    plotter.plot(dates, non_adult_rd, adult_rd)
    # print(stat.most_popular(data_set,'Greenland'))
    # print(stat.find_biggest_revenue(data_set,'Burundi'))
    