'''
    Functions to be used in order to analyze csv file. 
'''

from collections import Counter
import lib.plotting as plotting

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
