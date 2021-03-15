
class Graph:
    graph_dict = {}

    def add_node(self, node, neighbours):
        self.graph_dict[node] = neighbours


    def add_edge(self, node, neighbour):
        if node not in self.graph_dict:
            self.graph_dict[node] = [neighbour]
        elif neighbour not in self.graph_dict[node]:
            self.graph_dict[node].append(neighbour)


    def show_edges(self):
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                print("(", node, ", ", neighbour, ")")

    
    def WRONG_d_f_s(self, start, stack = [], visited = {}, paths = []):
        if len(stack) == 0:
            if visited.get(start, False):
                return paths
            
            print("SEARCHING FOR NODES CONNECTED TO: ", start)
            stack.append(start)

        st_l = len(stack)
        current = stack[st_l - 1] if st_l else start

        if visited.get(current, False): 
            stack.pop()
            return self.d_f_s(start, stack, visited, paths)

        visited[current] = True

        for node in self.graph_dict[current]:
            if not visited.get(node, False) and node not in stack:
                stack.append(node)

        if len(stack) == st_l:
            paths.append(stack)
            print("Path found!")
            print([node for node in stack if visited.get(node, False)])

        self.d_f_s(start, stack, visited, paths)

    
    def right_d_f_s(self, visited, node, path):
        if node not in visited:
            visited.add(node)
            path.append(node)

            for neighbour in self.graph_dict[node]:
                self.right_d_f_s(visited, neighbour, path)


    def component_search(self):
        colors = ('blue', 'orange', 'yellow', 'red', 'green', 'pink' 'purple')
        components = {}

        visited = set()
        i = 0

        for node in self.graph_dict:
            if node not in visited:
                path=[]
                self.dfs(node, visited, path)
                components[colors[i]] = path
                i += 1

        for comp in components:
            print(f'{comp}: {components[comp]}')

    
    def dfs(self, node, visited = set(), component = []):
        if node not in visited:
            visited.add(node)
            component.append(node)

            for neighbour in self.graph_dict[node]:
                self.dfs(neighbour, visited, component)


    def b_f_s(self, node, i = 0, queue = [], visited = set()):
        if node not in visited:
            visited.add(node)
            print(node)

            for neighbour in self.graph_dict[node]:
                queue.append(neighbour)

            print(visited, queue)

        if len(queue) > i:
            self.b_f_s(queue[i], i, queue, visited)

        i += 1


    def my_bfs(self, start):
        print(start)
        visited = set(start)
        queue = self.graph_dict[start]
        i = 0

        while len(queue) > i:
            node = queue[i]

            if node not in visited:
                visited.add(node)
                print(node)

                queue += self.graph_dict[node]

            i += 1

    
    def bfs(self, node):
        pass

                

if __name__ == "__main__":

    d_g = Graph()
    d_g.add_node('A', ['B', 'C'])
    d_g.add_node('B', ['D', 'C'])
    d_g.add_node('C', ['D'])
    d_g.add_node('D', ['J', 'C'])
    d_g.add_node('E', ['F', 'I'])
    d_g.add_node('F', ['C', 'G', 'Q'])
    d_g.add_node('G', ['F', 'J'])
    d_g.add_node('H', ['N', 'M'])
    d_g.add_node('I', ['S'])
    d_g.add_node('J', ['D', 'G'])
    d_g.add_node('K', ['T'])
    d_g.add_node('L', ['P', 'M'])
    d_g.add_node('M', ['N', 'O', 'H', 'L'])
    d_g.add_node('N', ['M', 'H'])
    d_g.add_node('O', ['M'])
    d_g.add_node('P', ['L'])
    d_g.add_node('Q', [])
    d_g.add_node('R', [])
    d_g.add_node('S', [])
    d_g.add_node('T', ['K'])

    # d_g.d_f_s('H')
    # d_g.d_f_s('M')
    # d_g.d_f_s('A')
    # d_g.d_f_s('E')

    # d_g.right_d_f_s(set(), 'A')

    # und_g = Graph()
    # und_g.add_node('A', ['B', 'C'])
    # und_g.add_node('B', ['A', 'D', 'C'])
    # und_g.add_node('C', ['A', 'B', 'D'])
    # und_g.add_node('D', ['B', 'J', 'C'])
    # und_g.add_node('E', ['F', 'Q', 'I'])
    # und_g.add_node('F', ['E'])
    # und_g.add_node('G', ['J'])
    # und_g.add_node('H', ['N', 'M'])
    # und_g.add_node('I', ['S', 'E'])
    # und_g.add_node('J', ['D', 'G'])
    # und_g.add_node('K', ['T'])
    # und_g.add_node('L', ['P', 'M'])
    # und_g.add_node('M', ['N', 'O', 'H', 'L'])
    # und_g.add_node('N', ['M', 'H'])
    # und_g.add_node('O', ['M'])
    # und_g.add_node('P', ['L'])
    # und_g.add_node('Q', ['E'])
    # und_g.add_node('R', [])
    # und_g.add_node('S', ['I'])
    # und_g.add_node('T', ['K'])

    # und_g.right_d_f_s(set(), 'D')
    # und_g.component_search()
    # und_g.my_bfs('A')
    # d_g.component_search()



    und_g = Graph()
    und_g.add_node('A', ['B', 'C'])
    und_g.add_node('B', ['A', 'D', 'C'])
    und_g.add_node('C', ['A', 'B', 'D', 'F'])
    und_g.add_node('D', ['B', 'J', 'C'])
    und_g.add_node('E', ['I', 'F'])
    und_g.add_node('F', ['E', 'C', 'G', 'Q'])
    und_g.add_node('G', ['F', 'J'])
    und_g.add_node('H', ['N', 'M', 'J'])
    und_g.add_node('I', ['S', 'E', 'R'])
    und_g.add_node('J', ['D', 'G', 'H'])
    und_g.add_node('K', ['T', 'R', 'L'])
    und_g.add_node('L', ['P', 'K', 'M'])
    und_g.add_node('M', ['N', 'O', 'H', 'L'])
    und_g.add_node('N', ['M', 'H'])
    und_g.add_node('O', ['M'])
    und_g.add_node('P', ['L'])
    und_g.add_node('Q', ['F'])
    und_g.add_node('R', ['K', 'I'])
    und_g.add_node('S', ['I'])
    und_g.add_node('T', ['K'])

    und_g.my_bfs('A')

    
