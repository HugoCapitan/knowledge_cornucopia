from collections import deque
import sys
sys.setrecursionlimit(1000000)

class LinkedList:
    def __init__(self, elements = []):
        self.head = None
        self.last_key = -1
        self.length = 0

        if len(elements):
            self.head = Node(elements.pop(0), 0)
            self.last_key = 0
            self.length += 1

            prev_elem = self.head
            for data in elements:
                self.last_key += 1
                self.length += 1
                new_node = Node(data, self.last_key)
                prev_elem.next = new_node
                
                prev_elem = new_node

    
    def add(self, new_data):
        self.last_key += 1
        self.length += 1
        new_node = Node(new_data, self.last_key, self.head)
        self.head = new_node


    def remove(self):
        if self.head is not None:
            old_head_data = self.head.data
            self.head = self.head.next
            self.length -= 1 

            return old_head_data
        else:
            return None


    def reverse_iter_space(self):
        new_head = self.head
        og_head = self.head
        is_first_run = True

        while og_head.next is not None:
            previous_node = None

            for node in self:
                if node.next == None:
                    previous_node.next = None
                    node.next = previous_node

                    break
 
                previous_node = node

            if is_first_run:
                new_head = node
                is_first_run = False

        self.head = new_head


    def reverse_iter_time(self):
        llist_queue = deque()

        while self.length:
            llist_queue.append(self.remove())

        while len(llist_queue):
            self.add(llist_queue.popleft())

    
    def revers_rec(self, current_node=None, previous_node=None):
        if current_node is None and previous_node is None:
            current_node = self.head
        if current_node is not None:
            self.revers_rec(current_node.next, current_node)

            if current_node.next == None:
                self.head = current_node

            current_node.next = previous_node

    
    def __iter__(self):
        current_element = self.head
        while current_element != None:
            yield current_element
            current_element = current_element.next


    def __repr__(self):
        if self.head == None:
            return 'None'

        representation = ''
        for current_element in self:
            representation += f'{current_element.data} -> '

        representation += 'END'

        return representation


class Node:
    def __init__(self, data, key, next = None):
        self.data = data
        self.next = next
        self.key = key

    def __repr__(self):
        return f'({self.key}, {self.data})'


if __name__ == '__main__':

    llist = LinkedList(['S', 'o', 'f', 'i', 'a'])
    print("-- CREATING LIST -- \n ['S', 'o', 'f', 'i', 'a']")
    print('-- LIST CREATED -- \n', llist)
    llist.reverse_iter_space()
    print('-- REVERSING -- \n',  llist)
    llist.add('e.e')
    print('-- ADDING "e.e" -- \n ', llist)
    llist.reverse_iter_space()
    print('-- REVERSING AGAIN -- \n', llist)
    llist.add('UwU')
    print('-- ADDING "UwU" -- \n ', llist)
    llist.reverse_iter_time()
    print('-- Reversing quite easier -- \n', llist)
    llist.revers_rec()
    print('-- Reversing Recursively -- \n', llist)
