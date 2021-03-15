# Implementation requirements
# Append and Pop methods
# Peek method
# 

class LinkedList:
    def __init__(self, nodes = None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    
    # def append(self, data):
    #     newNode = Node(data, None)

    #     if self.head == None and self.tail == None:
    #         self.head = newNode
    #         self.tail = newNode
    #     else:
    #         self.tail.next = newNode
    #         self.tail = newNode


    def add_first(self, node):
        node.next = self.head
        self.head = node


    def add_last(self, node):
        if not self.head:
            self.head = node

        for current_node in self:
            pass
        
        current_node.next = node


    def add_after(self, target_node_data, new_node):
        if not self.head:
            raise Exception('List is empty')

        for current_node in self:
            if current_node.data == target_node_data:
                new_node.next = current_node.next
                current_node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)


    def add_before(self, target_node_data, new_node):
        if not self.head:
            raise Exception('List is empty')

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        node_before = self.head
        for current_node in self:
            if current_node.data == target_node_data:
                node_before.next = new_node
                new_node.next = current_node

                return

            node_before = current_node

        raise Exception("Node with data '%s' not found" % target_node_data)



    def __iter__(self):
        node = self.head 
        
        while node is not None:
            yield node
            node = node.next
    

    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next

        nodes.append("None")
        return '->'.join(nodes)


class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __repr__(self):
        return self.data


if __name__ == "__main__":
    # llist = LinkedList()
    # print(llist)

    # llist.append("a")
    # print(llist)

    # llist.append("b")
    # llist.append("c")
    # llist.append("d")
    # llist.append("e")
    # print(llist)
    # print("Take a peek!", llist.peek())
    # print(llist)


    llist = LinkedList(["a", "b", "c", "d"])
    print(llist)

    llist.add_first(Node("aa"))
    print(llist)

    llist.add_last(Node("e"))
    print(llist)

    llist.add_after("c", Node("cc"))
    print(llist)

    llist.add_before("b", Node("bb"))
    print(llist)

    llist.add_before('aa', Node('0'))
    print(llist)

