import random
import matplotlib.pyplot as plt

def create_timeseries(length = 7):
    vals = []
    for i in range(length):
        vals.append(random.randint(3, 20))
    print(vals)
    return vals

def create_offset_timeseries(timeseries, offset = 3):
    pass

def compute_dtw_matrix(timeseries):
    if len(timeseries) != 2:
        print(f"Error: compute_dtw_matrix() was given {len(timeseries)} timeseries")

    n = len(timeseries[0])
    m = len(timeseries[1])

    matrix = [[float('inf') for j in range(m+1)] for i in range(n+1)]
    matrix[0][0] = 0 # dp base case

    for i in range(1,n+1):
        for j in range(1,m+1):
           cost = abs(timeseries[0][i-1] - timeseries[1][j-1])
           matrix[i][j] = cost + min(matrix[i-1][j],
                                     matrix[i][j-1],
                                     matrix[i-1][j-1])

    # adding ts-values into the base case cols/rows for nicer representation
    matrix[0][1:] = timeseries[0]
    for i in range(1, n+1):
        matrix[i][0] = timeseries[1][i-1]

    print("Matrix:")
    for row in matrix:
        for col in row:
            print(f"{col:>2}", end=" ")
        print("")

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


    
