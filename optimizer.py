import os
import numpy as np

class Optimizer:

    def __init__(self,constraints, rides):
        self.num_rows = constraints[0]
        self.num_cols = constraints[1]
        self.num_cars = constraints[2]
        self.num_rides= constraints[3]
        self.bonus    = constraints[4]
        self.num_timeSteps = constraints[5]
        self.output_list = [ [] for _ in range(self.num_cars)]
        #car = [index, x_pos, y_pos, unvailable_counter]
        self.cars = []
        for i in range(self.num_cars):
            self.cars.append([i,0,0,0])

        #rides = [start_x, start_y, finish_x, finish_y, start_time, finish_time, is_taken]
        self.rides = rides
    
    def optimize(self,t):
        '''finds optimal next rides in one timestep'''
        global_possible_rides = []
        for car in self.cars:
            #available cars
            if car[3] == 0:
                global_possible_rides.extend(self.grade_rides(car,t))
        
        sortedTable = self.sortTable(global_possible_rides)
        print(sortedTable)
        self.clean(sortedTable)
        self.assign(sortedTable)

        #TODO decrease unavailable_counters

    def assign(self, table):
        for entry in table:
            #step 1: set car_unavailable_steps 
            #step 2: set location to finish point
            #step 3: add to output file
            #step 4: clean table

            current_car_idx = self.cars[entry[1][0]]
            current_ride = entry[2]
            if current_ride[6] == False:           
                for c in self.cars:
                    if c[0] == current_car_idx:
                        if c[3] == 0:
                            distance = abs(current_ride[0] - c[1]) + abs(current_ride[1] - c[2])
                            waiting_t = current_ride[4] - t - distance
                            driving_t = abs(current_ride[2] - current_ride[0]) + abs(current_ride[3] - current_ride[1])
                        
                            c[3]  = distance + waiting_t + driving_t
                            c[1] = current_ride[2]
                            c[2] = current_ride[3]
                            self.output_list[current_car_idx].extend(self.rides.index(current_ride))

            
        
    # Remove entries with zero and negative points
    def clean(self, possible_rides_sorted):
        # Get table dimension
        rows = len(possible_rides_sorted)
        bad_rows = []
        # Iterate over the table
        for i in range(0,rows):
            # Find entries with zero or negative points
            if possible_rides_sorted[i][0] == 0 or possible_rides_sorted[i][0] < 0:
                del possible_rides_sorted[i]

        # return np.delete(possible_rides_sorted, bad_rows, 0)


    def grade_rides(self, car, t):
        possible_rides = []
        for ride in self.rides:
            possible_points = self.grade_ride(car,ride,t)
            possible_rides.append([possible_points,car,ride])
        return possible_rides



    def grade_ride(self,car,ride,t):
        distance = abs(ride[0] - car[1]) + abs(ride[1] - car[2])
        waiting_t = ride[4] - t - distance
        driving_t = abs(ride[2] - ride[0]) + abs(ride[3] - ride[1])

        # filter impossible lines
        if ride[5] < (waiting_t + distance + t + driving_t):
            return 0

        # find out if bonus applies
        if waiting_t >= 0:
            bonus = self.bonus
        else:
            bonus = 0

        points = bonus + driving_t - waiting_t - distance
        return points

    # Sorts the table (points, car_idx, ride_idx) in descending order
    def sortTable(self, possible_rides):
        return sorted(possible_rides, key=lambda x: x[0], reverse=True)


def inputs(file_name):
    cwd = os.getcwd()
    rides = []
    #print(cwd)

    F = open(cwd+"/input/"+file_name,'r')
    conditions_2 = F.readline()
    conditions_1 = conditions_2.rstrip('\n')
    conditions   = [int(n) for n in conditions_1.split()]
    for line in F:
        line_noend = line.rstrip('\n')
        line_int = [int(n) for n in line_noend.split()]
        line_int.append(False)
        rides.append(line_int)

    return conditions, rides

def main():
    # initialize variables
    file_name = "a_example.in"
    conditions, rides = inputs(file_name)
    optimizer = Optimizer(conditions, rides)

    # loop over timestetps
    for t in range(optimizer.num_timeSteps):
        print("time = ",t)
        optimizer.optimize(t)
        print("\n")


    print(optimizer.output_list)
    for i in optimizer.output_list:
        a = len(i)
        i = [a] + i

    F = open("output.txt","w")
    F.writelines(str(i)) 
    F.close()


if __name__ == "__main__":
    main()