'''
    Converts the CSV file into a more useful representation of the data for our exercise.
'''
import csv

def convert(file_name):
    '''
        This function cleans the data in the given CSV file
    '''
    with open(file_name) as fp:
        reader = csv.reader(fp)
        next(reader)
        data_set = []
        for line in reader:
            # # We only uses year, cause, state and death from the data set since this is all we need for the exercise.
            # year, _, cause, state, death, _ = line
            # year, death, = int(year), int(death)
            # # We filter away the 'United States' entry in order to only focus on states.1
            # data_set.append([year, cause, state, death])
            pass
    return data_set