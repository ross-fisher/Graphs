"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if self.vertices.get(vertex_id) is None:
            self.vertices[vertex_id] = set()


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.vertices[v1].add(v2)


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices.get(vertex_id)


    # bft uses a queue
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()
        while q.size():
            node = q.dequeue()
            if node in visited:
                continue
            print(node)
            visited.add(node)
            neighbors = self.get_neighbors(node)
            for neighbor in neighbors:
                if neighbor not in visited:
                    q.enqueue(neighbor)


    # uses a stack
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        while s.size():
            node = s.pop()
            if node in visited:
                continue
            print(node)
            visited.add(node)
            neighbors = self.get_neighbors(node)
            for neighbor in neighbors:
                if neighbor not in visited:
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()

        def loop(vertex):
            if vertex in visited:
                return
            visited.add(vertex)
            print(vertex)

            neighbors = self.get_neighbors(vertex)
            for neighbor in neighbors:
                loop(neighbor)

        loop(starting_vertex)

       # print(starting_vertex)
#        neighbors = self.get_neighbors(starting_vertex)
#        for neighbor in neighbors:
#            dft(self, neighbor)



    # deque the first path
    # grab the vertex from the end of the path
    # enque a path
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()
        while q.size():
            path = q.dequeue()
            last_node = path[-1]
            if last_node in visited:
                continue
            elif last_node == destination_vertex:
                return path
            visited.add(last_node)
            for neighbor in self.get_neighbors(last_node):
                new_path = path.copy()
                new_path.append(neighbor)
                q.enqueue(new_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        visited = set()
        while True:
            path = s.pop()
            last_vertex = path[-1]

            if last_vertex == destination_vertex:
                return path
            elif last_vertex in visited:
                continue

            visited.add(last_vertex)

            for neighbor in self.get_neighbors(last_vertex):
                new_path = path.copy()
                new_path.append(neighbor)
                s.push(new_path)


    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited = set()
        result = None

        def loop(path):
            nonlocal result
            vertex = path[-1]
            if result or vertex in visited:
                return

            if vertex == destination_vertex:
                result = path
                return

            visited.add(vertex)
            for neighbor in self.get_neighbors(vertex):
                new_path = path.copy()
                new_path.append(neighbor)
                loop(new_path)


        loop([starting_vertex])
        return result


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
   graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
