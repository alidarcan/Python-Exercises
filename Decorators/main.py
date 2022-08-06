import time


def speed_calc_decorator(function):
    current_time = time.time()
    function()
    end_time = time.time()
    time_difference = end_time - current_time
    print(f"{function.__name__} time speed : {time_difference}")
    pass


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i
