import heapq
import math

graph = {}
hue_table = {}

with open("input.txt", "r") as f:
    inp = f.readlines()

for i in inp:
    node = i.strip().split()
    city = node[0]
    h = int(node[1])
    hue_table[city] = h
    neighbors = node[2:]
    graph[city] = []
    for j in range(0, len(neighbors), 2):
        neighbor = neighbors[j]
        distance = int(neighbors[j+1])
        graph[city].append((neighbor, distance))

def a_star_search(graph, heuristics, start, destination):
    # Priority queue to store (cost, city, path)
    queue = [(0 + heuristics[start], 0, start, [start])]
    visited = set()

    while queue:
        f_cost, g_cost, current, path = heapq.heappop(queue)

        if current in visited:
            continue
        visited.add(current)

        if current == destination:
            return path, g_cost

        for neighbor, distance in graph[current]:
            if neighbor not in visited:
                new_g_cost = g_cost + distance
                f_cost = new_g_cost + heuristics[neighbor]
                heapq.heappush(queue, (f_cost, new_g_cost, neighbor, path + [neighbor]))

    return None, None

start = 'Arad'
destination = 'Bucharest'

path, total_distance = a_star_search(graph, hue_table, start, destination)
if path:
    print(f"Path: {' -> '.join(path)}")
    print(f"Total distance: {total_distance} km")
else:
    print("NO PATH FOUND")
