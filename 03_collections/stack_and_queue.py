"""A stack (last in, first out) and a queue (first in, first out)."""

from collections import deque


class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if not self._items:
            raise IndexError("peek at empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        return not self._items

    def __len__(self) -> int:
        return len(self._items)


class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if not self._items:
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def is_empty(self) -> bool:
        return not self._items

    def __len__(self) -> int:
        return len(self._items)


def is_balanced(text: str) -> bool:
    """Use a stack to check that brackets are balanced."""
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = Stack()
    for ch in text:
        if ch in pairs.values():
            stack.push(ch)
        elif ch in pairs:
            if stack.is_empty() or stack.pop() != pairs[ch]:
                return False
    return stack.is_empty()


if __name__ == "__main__":
    print(is_balanced("{[()]}"))
    print(is_balanced("([)]"))
    queue = Queue()
    for job in ("build", "test", "deploy"):
        queue.enqueue(job)
    while not queue.is_empty():
        print("running", queue.dequeue())
