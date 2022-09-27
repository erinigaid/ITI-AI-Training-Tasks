def BCK(graph,start,goal,visited=[]):
    if not goal in visited:
        visited.append(start)
        for next in set(graph[start])-set(visited):
            BCK(graph,next,goal,visited)
    return visited

gdict={
    "a":["b","c"],
    "b":["a","d"],
    "c":["a","d"],
    "d":["e"],
    "e":["a"]
}
print(BCK(gdict,'a','e'))
