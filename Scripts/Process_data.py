import numpy as np

def moving_average(x, N):
    n = int(N/2)
    y = x[0]
    a=np.empty(n); a.fill(y)
    cumsum = np.cumsum(np.insert(x, 0, a)) 
    return (cumsum[N:] - cumsum[:-N]) / float(N)

def process_data(input, N=10):
    dict = {}
    for column in input[next(iter(input))]:
        dict[column] = {}
         # loops through column names of the first entry of the dict.
        list = [] # contains raw data per entry
        for key in input.keys():
            data = input[key][column]
            list.append(moving_average(data, N))
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
