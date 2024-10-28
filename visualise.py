# Plotting
import matplotlib.pyplot as plt
import numpy as np

def create_fig(data, params=[0.3,12]):
    alpha, size = params
    time = np.linspace(0, 600, 601) # min

    for key in data.keys():

        plt.plot(time, data[key]['mean_trace'], label=key)
        plt.fill_between(time, data[key]['upper_bound'], data[key]['lower_bound'], alpha=alpha)

    plt.tick_params(axis='both', which='major', labelsize=size)
    plt.tick_params(axis='both', which='minor', labelsize=size)
    plt.legend(prop={'size': size})
    plt.ylabel('Normalized FRET signal', fontsize=size)
    plt.xlabel('Time (s)', fontsize=size)
    plt.tight_layout()
    plt.savefig('Output.png')
    return plt.show()
