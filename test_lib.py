import math

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
