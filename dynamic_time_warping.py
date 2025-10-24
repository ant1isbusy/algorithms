import random
import matplotlib.pyplot as plt

def create_timeseries(length = 7):
    vals = []
    for i in range(length):
        vals.append(random.randint(3, 20))

    return vals

def create_offset_timeseries(timeseries, offset = 3):
    pass

def compute_dtw_matrix(timeseries):
    if len(timeseries) != 2:
        print(f"Error: function was given {len(timeseries)} timeseries")

    matrix = [[0 for n in range(len(timeseries[0]))] for m in range (len(timeseries[1]))]
    for row in matrix:
        print(row)

def plot_timeseries(timeseries: list[list[int]]):
    plt.plot(timeseries[0], label='Timeseries 1')
    plt.plot(timeseries[1], label='Timeseries 2')
    plt.xlabel('Time Points')
    plt.ylabel('Values')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    timeseries = [create_timeseries() for _ in range(2)]
    compute_dtw_matrix(timeseries)
    plot_timeseries(timeseries)


    
