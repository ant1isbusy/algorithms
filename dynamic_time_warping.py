import random
import matplotlib.pyplot as plt

BOLD_RED = "\033[1;31m"
RESET = "\033[0m"


def create_timeseries(length=7):
    vals = []
    for i in range(length):
        vals.append(random.randint(3, 20))
    return vals


def create_offset_timeseries(timeseries, offset=4):
    copy = [0] * offset + timeseries[:-offset]
    return copy


def warp_series(ts1, ts2, path):
    aligned_ts2 = [ts2[j - 1] for (_, j) in path]
    aligned_ts1 = [ts1[i - 1] for (i, j) in path]
    return aligned_ts1, aligned_ts2


def compute_dtw_matrix(timeseries):
    if len(timeseries) != 2:
        print(f"Error: compute_dtw_matrix() was given {len(timeseries)} timeseries")

    n = len(timeseries[0])
    m = len(timeseries[1])

    matrix = [[float("inf") for j in range(m + 1)] for i in range(n + 1)]
    matrix[0][0] = 0  # dp base case

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = abs(timeseries[0][i - 1] - timeseries[1][j - 1])
            matrix[i][j] = cost + min(
                matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]
            )

    # adding ts-values into the base case cols/rows for nicer representation
    matrix[0][1:] = timeseries[0]
    for i in range(1, n + 1):
        matrix[i][0] = timeseries[1][i - 1]

    return matrix


def backtrace_dtw(matrix):
    path = []
    sum_dtw = matrix[1][1]
    i, j = (len(matrix) - 1, len(matrix[1]) - 1)
    while i > 1 or j > 1:
        path.append((i, j))
        sum_dtw += matrix[i][j]
        if i > 1 and j > 1:
            min_val = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1])
            print(min_val)
            if min_val == matrix[i - 1][j - 1]:
                i, j = i - 1, j - 1
            elif min_val == matrix[i - 1][j]:
                i -= 1
            else:
                j -= 1

        elif i > 1:
            i -= 1
        else:
            j -= 1

    path.append((1, 1))
    path.reverse()

    print("Matrix:")
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(
                (
                    f"{BOLD_RED}{matrix[i][j]:>2}{RESET}"
                    if (i, j) in path
                    else f"{matrix[i][j]:>2}"
                ),
                end=" ",
            )
        print("")

    return sum_dtw, path


def plot_timeseries(timeseries: list[list[int]]):
    plt.plot(timeseries[0], label="Timeseries 1")
    plt.plot(timeseries[1], label="Timeseries 2")
    plt.xlabel("Time Points")
    plt.ylabel("Values")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    ts1 = create_timeseries(40)
    ts2 = create_offset_timeseries(ts1)
    timeseries = [ts1, ts2]
    dtw_mat = compute_dtw_matrix(timeseries)
    _, path = backtrace_dtw(dtw_mat)
    plot_timeseries(timeseries)
    timeseries = list(warp_series(ts1, ts2, path))
    plot_timeseries(timeseries)
