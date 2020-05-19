import heapq

# graph implemented as dict
# {node: set of weighted edges implemented as {(nbr, weight)}}

def dijkstra(graph, source):
    # takes graph and a source node

    # initialization
    to_visit = []
    for node in graph:
        dist = float('inf')
        prev = None
        if node == source:
            dist = 0
        to_visit.append([dist, node, prev])
    heapq.heapify(to_visit)
    # to return
    # {node:(distance, prev)}
    visited = {}
    
    # main loop
    while to_visit:
        # pair of (current_dist, current_node)
        current_pair = heapq.heappop(to_visit)
        current_node = current_pair[1]
        current_dist = current_pair[0]
        prev = current_pair[2]
        # add to visited
        visited[current_node] = (current_dist, prev)

        # relaxation step
        for edge in graph[current_node]:
            if edge[0] in visited:
                continue
            # find index in to_visit
            index = 0
            while index < len(to_visit):
                if to_visit[index][1] == edge[0]:
                    break
                index += 1

            dist = to_visit[index][0]
            if dist > current_dist + edge[1]:
                to_visit[index][0] = current_dist + edge[1]
                to_visit[index][2] = current_node
                # maintain heap property; to be improved
                heapq.heapify(to_visit)
    
    return visited

graph = {0:{(1,10), (3,5)}, 1:{(2,1), (3,2)}, 2:{(4,4)}, 3:{(1,3), (2,9), (4,2)}, 4:{(2,6), (0,7)}}
for source in graph:
    shortestpaths = dijkstra(graph, source)
    print('source: {}'.format(source))
    for node in shortestpaths:
        print('{}: distance:{}, prev:{}'.format(node, shortestpaths[node][0], shortestpaths[node][1]))