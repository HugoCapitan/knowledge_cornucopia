# QuickSort

Quicksort is a sorting algorithm that uses the paradigm divide and conquer, it consists of taking a pivot value from the array to sort and use it to sort the other elements.

It basically starts by choosing a pivot value and sorting all the smaller elements to the left of the pivot and the larger to its right.

Then it proceeds to sort the subarrays of the smaller elements and the larger and so on recursively until there's nothing more to sort.

```py
# This method assumes that l < r
def partition(arr, l, r):
    i = l - 1
    pivot = arr[r]

    for j in range(l, r):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]

    return i + 1

def quicksort(arr, l, r):
    if l < r`
        partition_index = partition(arr, l, r)

        quicksort(arr, l, partition_index)
        quicksort(arr, partition_index + 1, r)

```

# Graphs
Networks of nodes connected by edges or arcs. 

- Arc: directed connection between two nodes.
- Edge: undirectional connection between two nodes.

Some common algorithms in graphs include:
- Finding a path between two nodes.
- Finding the shortest path between two nodes.
- Determining cycles in the graph.
- Finging a path that reaches all nodes.

The connection between nodes can also have weights or costs associated with them and we might be interested in finding the cheapest path between two nodes for example.

We can simply represent a graph by creating a dictionary in which the keys are the nodes and the values of each node are lists of the nodes that are connected by a direct arc from that node.

```py
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}
```

# Depth First Search
 
The DFS is the most fundamental search algorithm used to explores nodes and edges of a graph.

- Time complexity of O(V+E) -> O(Vertices + Edges)
- Buiñding block of other algorithms

The algorithm basically consists on traversing a graph depth first without regard for which edges it takes next until it cannot go further at which point backtracks and continues.


# Breadth first search

Is another fundamental algorithm for traversing graphs and trees, it's particularly usefull to find the shortest path between two nodes.

This algorithm relies on queue to track which nodes to visit next. Upon reaching a new node the algorithm adds it to the queue to visit later


# Hash tables
Is a data structure that allows for a very fast retrieval of data, no matter the size of the data, nor the size of the table

A hash table uses an array as the way of staoring the data, if we want to retrieve an asset from the array, the time complexity would be O(n) if we don't know at which index the data is stored, however, if we have the index, the time complexity will be O(1)

A hash table implements a hasing function, which hashes a "Key" (typically a String) into an integer hash, and then maps that hash to an index, in which the data will be stored.

This way, if we ever want to retrieve our data we just need to pass our key into the hash function and we will get the index in which the data is stored.

One common issue with these hash tables is what do we do if two different keys land on the same index. These cases can be solved using one of two approaches:

- Open Addressing
  Open addressing will look into the next index in the array if the one returned by the hash table is already occupied.

  - We can advance 1 index each time we find an occupied index.
  - We can add 3 to the next index in which we search
  - We can use quadrating probing (failed attempts)^2

- Closed Addressing
  Instead of just storing the data in the root of the array, we store a linked list, and everytime a new key-data pair lands on that index, we append it to the linked list in that index.

Each approach has its downsides, and which is best for each case will probably have somthing to do with the Load Factor, which is the factor between the size of the array and the data stored

