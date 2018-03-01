import numpy as np

# Remove entries with zero and negative points
def cleanSortedTable(possible_rides_sorted):

    # Get table dimension
    dim = possible_rides_sorted.shape;
    rows = dim[0];
    columns = dim[1];
    bad_rows = [];
    # Iterate over the table
    for i in range(0,rows):
        # Find entries with zero or negative points
        if possible_rides_sorted[i][0] == 0 or possible_rides_sorted[i][0] < 0:
            bad_rows.append(i)

    return np.delete(possible_rides_sorted, bad_rows, 0)
