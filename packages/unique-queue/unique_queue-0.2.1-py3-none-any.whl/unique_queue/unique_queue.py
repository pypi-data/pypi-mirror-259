# MIT License

# Copyright (c) 2024 StudioBreeze

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import queue
from typing import Iterable

class UniqueQueue:
    """A FIFO queue, but which ignores attempts to re-add duplicate items, even after they're popped."""
    
    def __init__(self, init_items: Iterable = []):
        self.queue = queue.Queue()
        self.unique_set = set()

        # add the init items
        self.extend(init_items)

    def push(self, item):
        if item not in self.unique_set:
            self.queue.put(item)
            self.unique_set.add(item)

    def pop(self):
        if not self.queue.empty():
            item = self.queue.get()
            return item
        else:
            raise IndexError("pop from an empty queue")

    def extend(self, items: Iterable):
        for item in items:
            self.push(item)

    def total_count(self):
        return len(self.unique_set)
    
    def completed_count(self):
        return self.total_count() - self.remaining_count()

    def remaining_count(self):
        return self.queue.qsize()

    def __len__(self):
        return self.queue.qsize()
    
    def empty(self):
        return self.queue.empty()
