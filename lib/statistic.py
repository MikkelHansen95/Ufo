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


def count_adult_movies(data_set):
    count = 0
    for data in data_set:
        if data[0] == 'True':
            count += 1
    return f'\nThere are {count} adult movies in the set'

def count_animation_movies(data_set):
    count = 0
    for data in data_set:
        for dict in data[2]:
            if dict['name'] == 'Animation':
                count += 1
    return f'\nIn the set {count} movies are listed as "Animaton" under genres.'

def find_biggest_budget(data_set):
    max = 0
    title = ""
    for data in data_set:
        if data[1] > max:
            max = data[1]
            title = data[10] 
    return f'\nThe movie with the biggest budget is "{title}".\nAnd it is listed in the set with a {max}$ budget.'

def find_biggest_revenue(data_set, language):
    max = 0
    title = ""
    for data in data_set:
        for country in data[6]:
            if country["name"] == language and data[8] > max:
                max = data[8]
                title = data[10] 
    if max == 0:
        return f'\nNo movies found in the set from the country: {language}.'
    else:    
        return f'\n"{title}" is the movie from {language} with the biggest revenue.\nIt is listed in the set with a {max}$ revenue.'

def most_popular(data_set, language):
    max = 0
    title = ""
    for data in data_set:
        for country in data[6]:
            if country["name"] == language and data[5] > max:
                max = data[5]
                title = data[10] 
    if max == 0:
        return f'\nNo movies found in the set from the country: {language}.'
    else:  
        return f'\n"{title}" is the most popular movie from {language}.\nThe movie is rated {max} in popularity.'

#   1995-12-22

def get_all_dates_in_year():

    date1 = datetime.datetime(2050,1,1)
    date2 = datetime.datetime(2050,12,31)    
    mydates = pd.date_range(date1, date2).tolist()
    return mydates


def get_release_dates_plot(data_set, mature_rating):
    movies_rday = [];
    my_dates = get_all_dates_in_year()

    for data in data_set:
        if data[0] == mature_rating:
            movies_rday.append(data[7])
    
    no_movies_rday = np.full_like(my_dates, 0)

    for ele in movies_rday:
        i = 0
        for dato in my_dates:
            if ele.month == dato.month & ele.day == dato.day:
                    no_movies_rday[i] += 1
            i+=1

    min_serie = pd.Series(no_movies_rday, index = my_dates)
    min_serie = pd.to_numeric(min_serie)
    return min_serie;


def get_runtime_plot(data_set):
    runtime_list = []
    realease_date_list = []

    for d in data_set:
        realease_date_list.append(d[7])

    for data in data_set:
        runtime_list.append(data[9])

    df = pd.DataFrame(
        {'release_date': realease_date_list,
         'runtime': runtime_list
         }
    )
    df['Month'] = df['release_date'].dt.month
    
    ax1 = df.plot.scatter(x='Month', y='runtime')
    #ax1.plot()
    return ax1


    
    

