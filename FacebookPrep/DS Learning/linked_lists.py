# Using colletctions.deque

from collections import deque

deque()
# deque([])

deque(['a', 'b', 'c'])
# deque(['a', 'b', 'c'])

llist = deque("abcde")
# deque(['a', 'b', 'c', 'd', 'e'])

llist.append('f') 
# Will append to the right of the linked list

llist.pop()
# 'f'
# deque(['a', 'b', 'c', 'd', 'e'])

llist.appendleft('z')
# deque(['z', 'a', 'b', 'c', 'd', 'e'])

llist.popleft()
# 'z'
# deque(['a', 'b', 'c', 'd', 'e'])

## To implement stacks we can simply use the appendleft and popleft methods
history = deque()
history.appendleft("https://realpython.com/")
history.appendleft("https://realpython.com/pandas-read-write-files/")
history.appendleft("https://realpython.com/python-csv/")

# deque(['https://realpython.com/python-csv/',
#        'https://realpython.com/pandas-read-write-files/',
#        'https://realpython.com/'])


history.popleft()
history.popleft()
history
# deque(['https://realpython.com/'])

    


