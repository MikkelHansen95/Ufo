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

if __name__ == '__main__':
    file_dir = 'csv'
    # If the csv directory already exits it will be created
    if not os.path.isdir(file_dir):
        os.makedirs(file_dir)
    try:
        _, url = sys.argv
        file_name = os.path.join(file_dir, os.path.basename(url))
        download(url, file_name)   
    except Exception as e:
        print(__doc__)
        sys.exit(1)  

    # After downloading the csv file we use our own converter to read the file and clean it up. 
    # We filter some data away in order to represent our data in away we find more easy to work with
    # data_set = convert(file_name)


    