"""Let's build queues!"""

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item) # add item to the end of the queue

    def dequeue(self):
        return self.items.pop(0) if self.items else None # removes and returns the front item, or None if empty
    
    def peek(self):
        return self.items[0] if self.items else None # returns the front item without removing it, or None if empty
    
    def is_empty(self):
        return len(self.items) == 0 # returns True if queue is empty, False otherwise
    

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())  # Output: 1
    print(queue.peek())     # Output: 2
    print(queue.is_empty()) # Output: False