"""
    PROBLEM: I need a way to transport data around the app. Ideally it would be relatively unopinionated and doesn't care who is giving it data and where that data is going. 
    
    I'm thinking I will probably only ever require a single item to be stored in the queue at a time.
    
    This class is private. This should not be a public implementation.

"""


class DataQueue:
    def __init__(self):
        self._queue = []

    def __str__(self) -> str:
        output_string = ''
        if len(self._queue) > 0:
            for i in self._queue:
                output_string += str(i)
        return output_string

    def __repr__(self):
        return f'[{self._queue}]'

    def enqueue(self, item):
        self._queue.append(item)

    def dequeue(self):
        return self._queue.pop(0)

    def is_empty(self) -> bool:
        return True if len(self._queue) == 0 else False

    def view_queue(self):
        return self._queue

    def flush_queue(self):
        self._queue = []


dq = DataQueue()

dq.enqueue(1)
print(dq.view_queue())
