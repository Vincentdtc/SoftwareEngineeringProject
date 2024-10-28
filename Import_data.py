# This file will import the raw data and store it as a dict of dicts. In each dict there will be the data of that day.
import pandas as pd
import os

def create_dict(dir='Experimental_data'):
    dict = {}
    dir = os.listdir(dir)
    for filename in dir:
        print(filename)
        data = pd.read_excel(filename)
        dict[filename].append(data)
    return dict

output = create_dict()


# test = pd.read_excel('Experimental_data/Data_22022023.xlsx')
# wt = test['Wt']

# # displaying the DataFrame
# print(test.head())
# print(type(wt))