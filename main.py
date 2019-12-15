import test_lib
import time
import math


from contextlib import contextmanager


@contextmanager
def time_this(label):
    start = time.perf_counter_ns()
    try:
        yield
    finally:
        end = time.perf_counter_ns()
        print(f"TIME {label}: {(end-start)/1000000000} sec")


# pythran export dist1(float, float, float, float)
def dist1(x0, y0, x1, y1):
    return ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5


# pythran export dist2(float, float, float, float)
def dist2(x0, y0, x1, y1):
    return (math.pow(x1 - x0, 2) + math.pow(y1 - y0, 2)) ** 0.5


# pythran export dist3(float, float, float, float)
def dist3(x0, y0, x1, y1):
    return math.sqrt(math.pow(x1 - x0, 2) + math.pow(y1 - y0, 2))


# pythran export dist1_sq(float, float, float, float)
def dist1_sq(x0, y0, x1, y1):
    return (x1 - x0) ** 2 + (y1 - y0) ** 2


# pythran export dist2_sq(float, float, float, float)
def dist2_sq(x0, y0, x1, y1):
    return math.pow(x1 - x0, 2) + math.pow(y1 - y0, 2)


# pythran export dist3_sq(float, float, float, float)
def dist3_sq(x0, y0, x1, y1):
    return math.pow(x1 - x0, 2) + math.pow(y1 - y0, 2)

x0, y1, x1, y1 = 3, 4, 5, 6.7

for function, label in zip([test_lib.dist1, test_lib.dist2, test_lib.dist3, test_lib.dist1_sq, test_lib.dist2_sq, test_lib.dist3_sq, dist1, dist2, dist3, dist1_sq, dist2_sq, dist3_sq], 6*["dist1_pythran"] + 6*["dist1_python"]):
    if label == "dist1_python":
        print()
    with time_this(label):
        for n in range(10**6):
            function(x0, y1, x1, y1)
