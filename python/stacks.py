"""let's build stacks!"""

class Stack:
    def __init__(self):
        self.items = [] #initialize an empty list to store stack items

    def push(self, item):
        self.items.append(item) # add item to the top of stack
    
    def pop(self):
        return self.items.pop() if self.items else None #removes the top item without removing it, or None if empty
    
    def peek(self):
        return self.items[-1] if self.items else None #returns the top item removing it, or None if empty
    
    def is_empty(self):
        return len(self.items) == 0 #returns True if stack is empty, False otherwise

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())  # Output: 3
    print(stack.peek()) # Output: 2
    print(stack.is_empty()) # Output: False