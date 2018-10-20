'''
    Converts the CSV file into a more useful representation of the data for our exercise.
'''
import csv
import dateutil.parser
import ast
import datetime

def convert(file_name):
    '''
        This function cleans the data in the given CSV file.
    '''
    print('\nReading data from file to memory ...')
    with open(file_name, encoding='utf-8') as fp:
        reader = csv.reader(fp)
        next(reader)
        data_set = []
        # data_set = [line for line in reader]
        print('Cleaning up data ...')
        for line in reader:
            try:
                datetime,city,state,country,shape,duration,comments,date_posted,latitude,longitude = line
                # Converting strings to int, float or date:
                datetime,duration= dateutil.parser.parse(datetime), int(duration)   
                # Appending cleaned data to array:
                data_set.append([datetime,city,state,country,shape,duration,comments,date_posted,latitude,longitude])
            except:
                # Some data in the data set is not in standard format..!
                pass
    print('Finished reading and cleaning data!')
    return data_set