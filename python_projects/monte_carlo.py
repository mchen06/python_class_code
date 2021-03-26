import random
import math

def throw_dart(radius):
    side_1 = radius
    side_2 = side_1 * -1
    x_coor = random.uniform(side_2, side_1)
    y_coor = random.uniform(side_2, side_1)
    return x_coor, y_coor

def in_circle(x_coor, y_coor, radius):
    return x_coor ** 2 + y_coor ** 2 <= radius ** 2

def circle_area(num_darts, radius):
    dart_in_area = 0
    for x in range(num_darts):
        x_coor, y_coor = throw_dart(radius)
        if in_circle(x_coor, y_coor, radius):
            dart_in_area = dart_in_area + 1
    cir_percent = dart_in_area / num_darts
    return cir_percent * (radius * 2) ** 2
