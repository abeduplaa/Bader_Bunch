def grade_ride(car,ride):

    distance = abs(pickup_x - current_x) + abs(pickup_y - current_y)

    waiting_t = start_t - current_t - distance

    driving_t = abs(dropoff_x - pickup_x) + abs(dropoff_y - pickup_y)

    if finish_t < (waiting_t + distance + current_t + driving_t):
        return 0

    if waiting_t >= 0:
        bonus = b
    else:
        bonus = 0

    points = bonus + driving_t - waiting_t - distance
