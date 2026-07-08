"""
LÖSUNG 09: Stack (LIFO) & Queue (FIFO)
"""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):                    # 🟩 vorgegeben
        self.stack.append(item)

    def pop(self):                           # 🟨 SELBST
        if self.is_empty():
            return None
        removed = self.stack[-1]
        del self.stack[-1]
        return removed

    def peek(self):                          # 🟨 SELBST
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):                      # 🟨 SELBST
        return len(self.stack) == 0

    def display(self):                       # 🟨 SELBST
        print(self.stack)


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):                 # 🟩 vorgegeben
        self.queue.append(item)

    def dequeue(self):                       # 🟨 SELBST
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def display(self):                       # 🟨 SELBST
        print(self.queue)


s = Stack()
for x in ["A", "B", "C"]:
    s.push(x)
print("pop:", s.pop())       # C
s.display()                  # ['A', 'B']

q = Queue()
for x in ["A", "B", "C"]:
    q.enqueue(x)
print("dequeue:", q.dequeue())   # A
q.display()                      # ['B', 'C']
