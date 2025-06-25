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
