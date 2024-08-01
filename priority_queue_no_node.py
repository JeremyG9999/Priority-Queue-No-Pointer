import heapq
class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.index = 0
    def push(self, priority, item):
        heapq.heappush(self.queue, (priority, self.index, item))
        self.index += 1
    def pop(self):
        return heapq.heappop(self.queue)[-1]
    def is_empty(self):
        return len(self.queue) == 0
    def print_priorityQ(self):
        for priority, index, item in self.queue:
            print(f"Priority: {priority}, Index: {index}, Item: {item}")
def main():
    priorityQ = PriorityQueue()
    priorityQ.push(3, "task1")
    priorityQ.push(4, "task2")
    priorityQ.push(5, "task3")
    priorityQ.pop()
    print("Priority Queue:")
    priorityQ.print_priorityQ()
main()