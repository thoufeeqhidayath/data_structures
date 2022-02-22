from heapq import *
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)

class PQ:
    def __init__(self,items =None):
        if items:
            heapify(items)
            self.elements = items
        else:
            self.elements = []

    def add(self,task):
        heappush(self.elements,task)

    def pop(self):
        return heappop(self.elements)

p  =PQ()
p.add([1,1,"thoufeeq"])
p.add([2,3,"thoufeeq hidayath"])
p.add([2,2,"thoufeeq hidayath new"])
p.add([5,4,"india"])
p.add([4,5,"pakistan"])

print(p.pop())

print(p.pop())

print(p.pop())

print(p.pop())
print(p.pop())

print(p.pop())