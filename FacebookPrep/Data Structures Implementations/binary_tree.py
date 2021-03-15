from collections import deque

class BinaryTree():
    def __init__(self, init_data):
        if type(init_data) == list:
            self.root = None
            self.create_from_list(deque(init_data))
        else:
            self.root = Node(init_data)

    
    def create_from_list(self, new_elems, queue = deque()): 
        if len(new_elems):      
            new_node = Node(new_elems.popleft())

            if not len(queue):
                self.root = new_node
            else:
                current_elem = queue[0]

                if not current_elem.left:
                    current_elem.left = new_node
                else:
                    current_elem.right = new_node
                    queue.popleft()

            queue.append(new_node)
            self.create_from_list(new_elems, queue)
        else:
            return "Done!"
    

    def get_height(self, start):
        if not start:
            return -1

        left_height = self.get_height(start.left)
        right_height = self.get_height(start.right)

        return max(left_height, right_height) + 1



    def bfs(self, queue, traversal = ''):
        if len(queue):
            current_item = queue.popleft()
            if current_item != None:
                queue.append(current_item.left)
                queue.append(current_item.right)

                traversal += f'{current_item.data}-'

            traversal = self.bfs(queue, traversal)
            
        return traversal


    def pre_order_traverse(self, start, traverse_string = ''):
        if start:
            traverse_string += f'{start.data}-'

            traverse_string = self.pre_order_traverse(start.left, traverse_string)
            traverse_string = self.pre_order_traverse(start.right, traverse_string)

        return traverse_string

    def in_order_traverse(self, start, traversal = ''):
        if start:
            traversal = self.in_order_traverse(start.left, traversal)

            traversal += f'{start.data}-'

            traversal = self.in_order_traverse(start.right, traversal)

        return traversal


class Node():
    def __init__(self, data):
        self.data = data;
        self.right = None;
        self.left = None;




# tree = BinaryTree('G')
# tree.root.left = Node('B')
# tree.root.left.left = Node('A')
# tree.root.left.right = Node('D')
# tree.root.left.right.left = Node('C')
# tree.root.left.right.right = Node('F')
# tree.root.left.right.right.left = Node('E')
# tree.root.right = Node('H')
# tree.root.right.right = Node('J')
# tree.root.right.right.left = Node('I')
# tree.root.right.right.right = Node('A')

tree = BinaryTree([6,3,7,30,6,65,12,2,45,23,632,65,23,21])
# tree = BinaryTree(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

print(tree.pre_order_traverse(tree.root, ''))
print(tree.in_order_traverse(tree.root))
print( tree.bfs(deque([tree.root])) ) 
print(tree.get_height(tree.root))
