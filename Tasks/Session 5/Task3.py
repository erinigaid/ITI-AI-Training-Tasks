import queue
class Node:
    def __init__(self,val):
        self.val=val
        self.neighbors=None
        self.visited_right=False
        self.visited_left=False
        self.parent_right=None
        self.parent_left=None

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

            if n.visited_left and n.visited_right:
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

n0= Node('a')
n1= Node('b')
n2= Node('c')
n3= Node('d')
n4= Node('e')
n5= Node('f')
n6= Node('g')
n7= Node('h')
n0.neighbors=[n1,n5]
n1.neighbors=[n0,n2,n6]
n2.neighbors=[n1]
n3.neighbors=[n4,n6]
n4.neighbors=[n3]
n5.neighbors=[n0,n6]
n6.neighbors=[n1,n3,n5,n7]
n7.neighbors=[n6]
myclass=Node
print("Bidirectional search: ",myclass.bidirectional_search(n0,n4))
