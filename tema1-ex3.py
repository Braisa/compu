import numpy as np
import matplotlib.pyplot as plt

function = lambda x : x**2 - 3*x + np.exp(x) - 2

x_start, x_end = -0.5, -0.2
x_middle = (x_start + x_end) / 2
stop_threshold = 1e-5

def check_root_bisection(func, x_left, x_right):
    x_center = (x_left + x_right) / 2
    # Root found
    if np.abs(func(x_center)) <= stop_threshold:
        return True, func(x_center), x_center, x_left, x_right
    # Change interval
    if func(x_center) * func(x_left) > 0:
        # Move right
        return False, func(x_center), x_center, x_center, x_right
    if func(x_center) * func(x_right) > 0:
        # Move left
        return False, func(x_center), x_center, x_left, x_center

def iteration_step(found, value, center, left, right):
    if found:
        print(f"Solución no intervalo ({x_start},{x_end}).")
        print(f"x = {center:6f}")
        print(f"f(x) = {value:6f}")
    else:
        return check_root_bisection(function, left, right)

_found, _value, _center, _left, _right = iteration_step(False, function(x_middle), x_middle, x_start, x_end)
while not _found:
    _found, _value, _center, _left, _right = iteration_step(_found, _value, _center, _left, _right)
iteration_step(_found, _value, _center, _left, _right)
