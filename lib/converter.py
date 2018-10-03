'''
    Converts the CSV file into a more useful representation of the data for our exercise.
'''
import csv
import dateutil.parser
import ast

def convert(file_name):
    '''
        This function cleans the data in the given CSV file
    '''
    print('Reading data from file to memory ...')
    with open(file_name, encoding='utf-8') as fp:
        reader = csv.reader(fp)
        next(reader)
        data_set = []
        # data_set = [line for line in reader]
        print('Cleaning up data ...')
        for line in reader:
            try:
                adult,_,budget,genres,_,_,_,original_language,_,overview,popularity,_,_,production_countries,release_date,revenue,runtime,_,_,_,title,_,_,_ = line
                # Converting strings to int, float or date:
                genres,production_countries = ast.literal_eval(genres),ast.literal_eval(production_countries)
                budget,popularity,release_date,revenue,runtime = int(budget), float(popularity), dateutil.parser.parse(release_date), int(revenue), float(runtime)                
                # Appending cleaned data to array:
                data_set.append([adult,budget,genres,original_language,overview,popularity,production_countries,release_date,revenue,runtime,title])
            except:
                # Some data in the data set is not in standard format..!
                pass
    print('Finished reading and cleaning data ...')
    return data_set