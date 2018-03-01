import numpy as np

# Sorts the table (points, car_idx, ride_idx) in descending order
def sortTable(possible_rides):

    return sorted(possible_rides, key=lambda x: x[0], reverse=True);

    


