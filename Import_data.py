# This file will import the raw data and store it as a dict of panda dataframes. In each dict entry there will be the data of that file.
import pandas as pd
import os

def create_dict(path='Experimental_data'):
    dict = {}
    dir = os.listdir(path)
    for filename in dir:
        print(path + '/' + filename)
        data = pd.read_excel(path + '/' + filename)
        dict[filename] = data
    return dict

# output = create_dict()
# print(output['Data_22022023.xlsx'].head())
