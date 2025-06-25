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