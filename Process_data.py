import numpy as np
from Import_data import create_dict

def process_data(data):
    dict = {}
    for column in data[next(iter(data))]:
        dict[column] = {}
         # loops through column names of the first entry of the dict.
        list = [] # contains raw data per entry
        for key in data.keys():
            list.append(data[key][column])
        # calculate mean and std per data category
        mean_trace = np.mean(list, axis=0)
        std = np.std(list, axis=0)
        # generate lower and upper bounds of each trace.
        upper_bound = mean_trace + std
        lower_bound = mean_trace - std
        # store calculated values in dict
        dict[column]['mean_trace'] = mean_trace
        dict[column]['upper_bound'] = upper_bound
        dict[column]['lower_bound'] = lower_bound

    return dict

# d = create_dict()
# test = process_data(d)
# print(np.shape(test['E694D']['upper_bound']))