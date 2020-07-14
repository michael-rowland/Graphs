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
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)
        # self.vertices[v2].add(v1)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue
        q = Queue()
        # make a set if we've been here before
        visited = set()
        # enqueue our starting node
        q.enqueue(starting_vertex)
        # while our queue isn't empty
        while q.size():
            # dequeue whatever's at the front of the line (current node)
            current_node = q.dequeue()
            # if we haven't visited this node yet
            if current_node not in visited:
                print(current_node)
                # mark as visited
                visited.add(current_node)
                # add it's neighbors to queue
                for neighbor in self.get_neighbors(current_node):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        visited = set()
        s.push(starting_vertex)
        while s.size():
            current_node = s.pop()
            if current_node not in visited:
                print(current_node)
                visited.add(current_node)
                for neighbor in self.get_neighbors(current_node):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        print(starting_vertex)
        # mark this vertex as visited
        visited.add(starting_vertex)
        # for each neighbor, not visited: recurse on neighbor
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, start, end):
        """
        Return a list containing the shortest path from
        start to end in
        breath-first order.
        """
        q = Queue()
        visited = set()
        path = [start]
        q.enqueue(path)
        # while queue isn't empty
        while q.size():
            # dequeue the node at the front of the line
            current_path = q.dequeue()
            current_node = current_path[-1]
            # if this node is our target node: return it
            if current_node == end:
                return current_path
            # otherwise: mark as visited, get it's neighbors
            if current_node not in visited:
                visited.add(current_node)
                # for each neighbor: add to our queue
                for neighbor in self.get_neighbors(current_node):
                    q.enqueue(current_path + [neighbor])

    def dfs(self, start, end):
        """
        Return a list containing a path from
        start to end in
        depth-first order.
        """
        s = Stack()
        visited = set()
        path = [start]
        s.push(path)
        while s.size():
            current_path = s.pop()
            current_node = current_path[-1]
            if current_node == end:
                return current_path
            if current_node not in visited:
                visited.add(current_node)
                for neighbor in self.get_neighbors(current_node):
                    s.push(current_path + [neighbor])

    def dfs_recursive(self, start, end, path=None, visited=set()):
        """
        Return a list containing a path from
        start to end in
        depth-first order.

        This should be done using recursion.
        """
        # mark our node as visited, and
        visited.add(start)
        if not path:
            path = [start]
        # return if it's our target node
        if start == end:
            return path
        # iterate over neighbors
        for neighbor in self.get_neighbors(start):
            # check if visited
            if neighbor not in visited:
                # if not recurse
                result = self.dfs_recursive(neighbor, end, path + [neighbor], visited)
                # if visited
                if result:
                    return result


if __name__ == "__main__":
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

    """
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    """
    print(graph.vertices)

    """
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
    """
    # graph.bft(1)

    """
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    """
    # graph.dft(1)
    graph.dft_recursive(1)

    """
    Valid BFS path:
        [1, 2, 4, 6]
    """
    print(graph.bfs(1, 6))

    """
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    """
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
