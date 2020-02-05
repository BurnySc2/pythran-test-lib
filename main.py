import test_lib
import astar

import time
import math


from contextlib import contextmanager

from typing import List


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


def dist_test():
    x0, y1, x1, y1 = 3.0, 4.0, 5.0, 6.7
    for function, label in zip(
        [
            test_lib.dist1,
            test_lib.dist2,
            test_lib.dist3,
            test_lib.dist1_sq,
            test_lib.dist2_sq,
            test_lib.dist3_sq,
            dist1,
            dist2,
            dist3,
            dist1_sq,
            dist2_sq,
            dist3_sq,
        ],
        6 * ["dist1_pythran"] + 6 * ["dist1_python"],
    ):
        if label == "dist1_python":
            print()
        function(x0, y1, x1, y1)
        with time_this(label):
            for n in range(10 ** 6):
                function(x0, y1, x1, y1)


def pathfinding_automaton_test():
    import numpy as np

    def read_maze(file_name: str) -> List[List[int]]:
        with open(file_name, "r") as text:
            m = text.read()
        lines = m.split("\n")
        final_maze = []
        for y in range(0, len(lines[0])):
            maze_line = []
            final_maze.append(maze_line)
            for x in range(0, len(lines)):
                maze_line.append(int(lines[x][y]))
        return final_maze

    grid = np.asarray(read_maze("AutomatonLE.txt"))

    # Find path from main ramp to main ramp on automaton
    start = (51, 32)
    goal = (129, 150)
    path = astar.find_path(grid, {}, start, goal, True)
    print(path)
    with time_this("Test pathfinding"):
        for n in range(10 ** 3):
            astar.find_path(grid, {}, start, goal, True)


def pathfinding_basic_test():
    import numpy as np

    grid = np.ones((10, 10)).astype(int)
    grid[0, :] = 0
    grid[9, :] = 0
    grid[:, 0] = 0
    grid[:, 9] = 0
    print(grid)

    start = (1, 1)
    goal = (6, 8)
    path = astar.find_path(grid, {}, start, goal, True)
    print(path)
    with time_this("Test pathfinding"):
        for n in range(10 ** 3):
            astar.find_path(grid, {}, start, goal, True)


if __name__ == "__main__":
    # dist_test()
    pathfinding_automaton_test()
    # pathfinding_basic_test()
