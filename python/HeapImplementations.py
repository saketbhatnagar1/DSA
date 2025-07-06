import heapq

# Min-Heap Implementation
def min_heap_demo():
    print("=== Min Heap ===")
    min_heap = []
    heapq.heappush(min_heap, 10)
    heapq.heappush(min_heap, 1)
    heapq.heappush(min_heap, 5)
    print("Heap content:", min_heap)

    print("Pop min:", heapq.heappop(min_heap))
    print("Heap after pop:", min_heap)

# Max-Heap Implementation
def max_heap_demo():
    print("\n=== Max Heap ===")
    max_heap = []
    heapq.heappush(max_heap, -10)
    heapq.heappush(max_heap, -1)
    heapq.heappush(max_heap, -5)
    print("Heap content (negated):", max_heap)

    print("Pop max:", -heapq.heappop(max_heap))
    print("Heap after pop:", [-x for x in max_heap])

# Custom Object Heap (e.g., Task Scheduler)
def custom_heap_demo():
    print("\n=== Custom Object Heap (Priority Queue) ===")
    tasks = []
    heapq.heappush(tasks, (2, "Write code"))
    heapq.heappush(tasks, (1, "Sleep"))
    heapq.heappush(tasks, (3, "Eat"))

    while tasks:
        priority, task = heapq.heappop(tasks)
        print(f"Task: {task} (priority: {priority})")

# Main execution
if __name__ == "__main__":
    min_heap_demo()
    max_heap_demo()
    custom_heap_demo()
'''
        1
       / \
      3   5
     / \
    4   8
    Min heap


        10
       /  \
      5    3
     / \
    1   2
    Max Heap



| Operation              | Time Complexity | Notes                                                         |
| ---------------------- | --------------- | ------------------------------------------------------------- |
| Insert (`push`)        | O(log n)        | Inserts at the bottom, then "heapify up"                      |
| Delete Min/Max (`pop`) | O(log n)        | Removes root, replaces with last element, then "heapify down" |
| Peek (`top`)           | O(1)            | Get the root element                                          |

How is it Implemented?
Although heaps are conceptually trees, they are implemented using arrays/lists:

For an element at index i:

Left child is at 2*i + 1

Right child is at 2*i + 2

Parent is at (i - 1) // 2

Example array for min-heap [1, 3, 5, 4, 8] represents this tree:

         1
       / \
      3   5
     / \
    4   8

'''

# A Python program to demonstrate common binary heap operations

# Import the heap functions from python library
from heapq import heappush, heappop, heapify 

# heappop - pop and return the smallest element from heap
# heappush - push the value item onto the heap, maintaining
#             heap invarient
# heapify - transform list into heap, in place, in linear time

# A class for Min Heap
class MinHeap:
    
    # Constructor to initialize a heap
    def __init__(self):
        self.heap = [] 

    def parent(self, i):
        return (i-1)/2
    
    # Inserts a new key 'k'
    def insertKey(self, k):
        heappush(self.heap, k)           

    # Decrease value of key at index 'i' to new_val
    # It is assumed that new_val is smaller than heap[i]
    def decreaseKey(self, i, new_val):
        self.heap[i]  = new_val 
        while(i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            # Swap heap[i] with heap[parent(i)]
            self.heap[i] , self.heap[self.parent(i)] = (
            self.heap[self.parent(i)], self.heap[i])
            
    # Method to remove minimum element from min heap
    def extractMin(self):
        return heappop(self.heap)

    # This function deletes key at index i. It first reduces
    # value to minus infinite and then calls extractMin()
    def deleteKey(self, i):
        self.decreaseKey(i, float("-inf"))
        self.extractMin()

    # Get the minimum element from the heap
    def getMin(self):
        return self.heap[0]

# Driver pgoratm to test above function
heapObj = MinHeap()
heapObj.insertKey(3)
heapObj.insertKey(2)
heapObj.deleteKey(1)
heapObj.insertKey(15)
heapObj.insertKey(5)
heapObj.insertKey(4)
heapObj.insertKey(45)

