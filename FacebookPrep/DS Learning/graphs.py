class Graph:
    
    graph_dict = {}

    def __init__(self):
        pass


    def addNode(self, name, neighbours):
        if name not in self.graph_dict:
            self.graph_dict[name] = neighbours


    def add_edge(self, node, neighbour):
        if node not in self.graph_dict:
            self.graph_dict[node] = [neighbour]
        elif neighbour not in self.graph_dict[node]:
            self.graph_dict[node].append(neighbour)


    def show_edges(self):
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                print("(", node, ", ", neighbour, ")")


    def find_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path

        for node in self.graph_dict[start]:
            if node not in path:
                newPath = self.find_path(node, end, path)
                if newPath:
                    return newPath

    
    # Homework
    def closest_path(self, start, end, paths: []):
        pass


    # Homework
    def b_f_s(self, start):
        visited = {}

        for i in self.graph_dict:
            visited[i] = False

        queue = []
        queue.append(start)
        visited[start] = True

        while len(queue) != 0:
            start = queue.pop(0)
            for node in self.graph_dict[start]:
                if not visited[node]:
                    visited[node] = True
                    queue.append(node)
            
            print(start, end=" ")


    # Homework
    def d_f_s(self):
        pass

if __name__ == '__main__':   
    g = Graph()
    g.add_edge('1', '2')
    g.add_edge('1', '3')
    g.add_edge('2', '3')
    g.add_edge('2', '1')
    g.add_edge('3', '1')
    g.add_edge('3', '2')
    g.add_edge('3', '4')
    g.add_edge('4', '3')
    g.show_edges()
    

    # Note that this method for finding a path doesnt checks if it's the closest
    print(g.b_f_s('1'))
