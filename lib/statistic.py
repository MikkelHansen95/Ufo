'''
    Functions to be used in order to analyze csv file. 
'''

from collections import Counter
import matplotlib.pyplot as plt
import lib.plotting as plotting
import datetime
import pandas as pd
import numpy as np
from pandas import DataFrame
import csv
from datetime import datetime
import dateutil
import pandas as pd

def count_ufo_spotted(data_set):
    place_ufo_spotted = []
    for data in data_set:
        place_ufo_spotted.append(data[1])

    most_common_place_spotted = Counter(place_ufo_spotted).most_common(1)
    
    return f'\nMost spotted place is {most_common_place_spotted[0][0]} and was spotted {most_common_place_spotted[0][1]} '

def ufo_spotted_over_time(data_set):
    year_spotted = []
    datetime_list = []
    datetime_year = []
    datetime_list = [datetime.strptime(x[0], '%m/%d/%Y %H:%M') for x in data_set]
    
    for i in datetime_list:
        datetime_year.append(i.year)
 
    year_spotted = Counter(datetime_year)
    return year_spotted
    
def which_season_is_most_common(data_set):
    season_count = []
    datetime_list = [datetime.strptime(x[0], '%m/%d/%Y %H:%M') for x in data_set]
    season_one = 0
    season_two = 0
    season_three = 0
    season_four = 0
    for i in datetime_list:
        if i.month == 1 or i.month == 2 or i.month == 12:
            season_one += 1
        elif i.month == 3 or i.month == 4 or i.month == 5:
            season_two += 1
        elif i.month == 6 or i.month == 6 or i.month == 8:
            season_three += 1
        elif i.month == 9 or i.month == 10 or i.month == 11:
            season_four += 1
    season_count.append(season_one)
    season_count.append(season_two)
    season_count.append(season_three)
    season_count.append(season_four)
    return season_count

def how_does_an_ufo_look(data_set):
    ufo_shape_list = []

    for i in data_set:
        ufo_shape_list.append(i[4])
    
    count_shapes = Counter(ufo_shape_list).most_common(5)
    return f'\nTop 5 shapes of ufo {count_shapes}'

def how_long_was_ufo_spotted(data_set):
    ufo_spot_duration = []
    my_count = 0
    for i in data_set:
        ufo_spot_duration.append(i[6])
        my_count += 1
    
    duration_spotted = Counter(ufo_spot_duration)

    return duration_spotted

def which_weekday_ufo_spotted(data_set):
    weekdays = []
    datetime_list = [datetime.strptime(x[0], '%m/%d/%Y %H:%M') for x in data_set]
    allsights = 0
    newlist = []
    for i in datetime_list:
        weekdays.append(i.weekday())
        allsights +=1
    
    counted_weekdays = Counter(weekdays)
    count = sorted(counted_weekdays.items())
    x, y = zip(*count)
    for l in y:
        newlist.append(l/allsights)

    df = pd.DataFrame(
        {'weekdays': x,
         'count': newlist
         })

    return df
