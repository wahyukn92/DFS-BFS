#Game Greedy Spiders

spiders = {
        '1': ['2', '3', '4'],
        '2': ['3', '8'],
        '3': ['4', '5','6','7','8'],
        '4': ['5'],
        '5': ['6'],
        '6': ['7','11'],
        '7': ['8','9','10','11'],
        '8': ['9'],
        '9': ['10'],
        '10': ['11']
        
        }

def bfs(graph, start, end):
    queue = []
    queue.append([start])
    while queue:
        route = queue.pop(0)
        node = route[-1]
        if node == end:
            return route
        for branch in graph.get(node, []):
            new_route = list(route)
            new_route.append(branch)
            queue.append(new_route)

    contents = len(queue)
    if contents == 0:
            print("Not found, try again")

#bfs(spiders, '1', '11')

def dfs(graph, start, end):
    queue = []
    queue.append([start])
    while queue:
        route = queue.pop(-1)
        node = route[-1]
        if node == end:
            return route
        for branch in graph.get(node, []):
            new_route = list(route)
            new_route.append(branch)
            queue.append(new_route)

    contents = len(queue)
    if contents == 0:
            print("Not found, try again")

#dfs(spiders, '1', '11')


