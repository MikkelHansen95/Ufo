'''
    Download from URL to file 
'''

import os
from urllib import request as req

def download(from_url, to_file): 
    if not os.path.isfile(to_file):
        req.urlretrieve(from_url, to_file)


