# Applying Uniform Cost Search Al
mygraph = {
    "Easthampton": [("Westhampton", 10), ("Northhampton", 6), ("SoutHadley", 11)],
    "Northhampton": [("Westhampton", 10), ("Easthampton", 6), ("SoutHadley", 11), ("Hadley", 4), ("Florence", 2)],
    "Florence": [("Northhampton", 2), ("Williamsburg", 6), ("Hatfield", 5)],
    "Hatfield": [("Amherst", 11), ("Hadley", 7), ("Whately", 6), ("Florence", 5)],
    "Whately": [("Ghoshen", 14), ("Williamsburg", 9), ("Hatfield", 6), ("Amherst", 14)]
}


def path_cost(path):
    total_cost = 0
    for(node, cost) in path:
        total_cost = total_cost+cost
    return total_cost, path[-1][0]


def myucs(mygraph, start, goal):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=path_cost)
        path = queue.pop(0)
        node = path[-1][0]
        if node not in visited:
            visited.append(node)
            if node == goal:
                return path
            else:
                neighbour_nodes = mygraph.get(node, [])

                for (node2, cost) in neighbour_nodes:
                    new_path = path.copy()
                    new_path.append((node2, cost))
                    queue.append(new_path)
        else:
            continue


answer_path = myucs(mygraph, "Easthampton", "Whately")
a, b = path_cost(answer_path)
print(answer_path)
print("Total Path cost = ", a)
print("Shortest path = ", [node for node, cost in answer_path])
