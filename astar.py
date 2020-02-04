# https://gist.github.com/bellbind/224175
import numpy as np

# pythran export heappush((float, (int, int)) list, (float, (int, int)))
def heappush(heap, val):
    cur = len(heap)
    heap.append(val)
    while cur > 0:
        parent = (cur - 1) // 2
        if heap[parent] <= heap[cur]:
            break
        heap[cur], heap[parent] = heap[parent], heap[cur]
        cur = parent


# pythran export heappop((float, (int, int)) list)
def heappop(heap):
    ret = heap[0]
    last = heap.pop()
    size = len(heap)
    if size == 0:
        return ret
    heap[0] = last
    cur = 0
    while True:
        ch1 = 2 * cur + 1
        if ch1 >= size:
            return ret
        ch2 = ch1 + 1
        child = ch2 if ch2 < size and heap[ch2] < heap[ch1] else ch1
        if heap[cur] <= heap[child]:
            return ret
        heap[child], heap[cur] = heap[cur], heap[child]
        cur = child


# def in_bounds(self, position):
#     return 0 <= position[0] < self.width and 0 <= position[1] < self.height

# def heuristic_manhattan(self, source, target):
#     return abs(source[0] - target[0]) + abs(source[1] - target[1])

# pythran export find_path(int [:,:], (int, int):(int, int) dict, (int, int), (int, int))
# pythran export find_path(int [:,:], (int, int):(int, int) dict, (int, int), (int, int), bool)
def find_path(grid, came_from, source, target, allow_diagonal: bool = True):
    # type: (np.ndarray, Dict[Tuple[int, int], Tuple[int, int]], Tuple[int, int], Tuple[int, int], bool) -> (List[Tuple[int, int]])
    directions = [
        (0, 1, 1),
        (0, -1, 1),
        (1, 0, 1),
        (-1, 0, 1),
        (1, 1, 2 ** 0.5),
        (1, -1, 2 ** 0.5),
        (-1, -1, 2 ** 0.5),
        (-1, 1, 2 ** 0.5),
    ]
    if not allow_diagonal:
        directions = directions[:4]

    open_set = []
    closed_set = set()
    cost = {}  # type: Dict[Tuple[int, int], float]

    cost[source] = 0.0
    heappush(open_set, (0, source))

    while open_set:
        current = heappop(open_set)[1]
        if current in closed_set:
            continue

        closed_set.add(current)

        if current == target:
            # print(f"Constructing path. Open set size: {len(open_set)}, closet set size: {len(closed_set)}")
            path = []
            path.append(current)
            while current != source:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

        for direction in directions:
            child = (current[0] + direction[0], current[1] + direction[1])
            # Needs to do bounds check if the grid has no outside wall, e.g. air units
            if child in closed_set or not grid[child[1], child[0]]:
                continue

            child_g = cost[current] + direction[2]
            child_h = abs(child[0] - target[0]) + abs(child[1] - target[1])
            child_f = child_g + child_h

            # https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
            heappush(open_set, (child_f, child))
            came_from[child] = current
            cost[child] = child_g
    return []
