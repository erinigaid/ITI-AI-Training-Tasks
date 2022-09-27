import queue
class library:
    def __init__(self, val):
        self.val = val
        self.neighbors = None
        self.visited_right = False
        self.visited_left = False
        self.parent_right = None
        self.parent_left = None


    def bidirectional_search(s, t):
        def extract_path(node):
            node_copy = node
            path = []

            while node:
                path.append(node.val)
                node = node.parent_right

            path.reverse()
            del path[-1]

            while node_copy:
                path.append(node_copy.val)
                node_copy = node_copy.parent_left
            return path

        q = queue.Queue()
        q.put(s)
        q.put(t)
        s.visited_right = True
        t.visited_left = True

        while not q.empty():
            n = q.get()

            if n.visited_left and n.visited_right:  # if the node visited by both BFS's
                return extract_path(n)

            for node in n.neighbors:
                if n.visited_left == True and not node.visited_left:
                    node.parent_left = n
                    node.visited_left = True
                    q.put(node)
                if n.visited_right == True and not node.visited_right:
                    node.parent_right = n
                    node.visited_right = True
                    q.put(node)

        return False

    def Iteration_DFS(graph, start):
        stack = [start]
        visited = []
        while stack:
            vertex = stack.pop()
            if vertex in visited:
                continue
            visited.append(vertex)
            for neighbor in graph[vertex]:
                stack.append(neighbor)
        return visited

    def Recursive_DFS(graph, start, visited=[]):
        visited.append(start)
        for next in set(graph[start]) - set(visited):
            library.Recursive_DFS(graph, next, visited)
        return visited

    def bfs(graph,node,visited):
        visited.append(node)
        qq.append(node)

        while qq:
            m=qq.pop(0)
            print(m,end=" ")

            for neighbor in graph[m]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    qq.append(neighbor)

    def BCK(graph, start, goal, visited=[]):
        if not goal in visited:
            visited.append(start)
            for next in set(graph[start]) - set(visited):
                library.BCK(graph, next, goal, visited)
        return visited


n0 = library(0)
n1 = library(1)
n2 = library(2)
n3 = library(3)
n4 = library(4)
n5 = library(5)
n6 = library(6)
n7 = library(7)
n0.neighbors = [n1, n5]
n1.neighbors = [n0, n2, n6]
n2.neighbors = [n1]
n3.neighbors = [n4, n6]
n4.neighbors = [n3]
n5.neighbors = [n0, n6]
n6.neighbors = [n1, n3, n5, n7]
n7.neighbors = [n6]
visited=[]
qq=[]
graph={
    "A":["B","C","D"],
    "B":["E"],
    "C":["F","G"],
    "D":["H"],
    "E":["I"],
    "F":["J"],
    "G":[],
    "H":[],
    "I":[],
    "J":[]
}

print("Iteration DFS: \n",library.Iteration_DFS(graph,"A"))
print("Recursive DFS: \n",library.Recursive_DFS(graph,"A"))
print("BCK: \n",library.BCK(graph,"A","E"))
print("bidirectional: \n",library.bidirectional_search(n0,n4))
print("BFS: ")
print(library.bfs(graph,"A",visited))



