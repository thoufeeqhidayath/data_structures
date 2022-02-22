from heapq import heappush
from heapq import *

def heapsort(iterable):
    h = []
    for value in iterable:
       heappush(h, value)
    return [heappop(h) for i in range(len(h))]

print(heapsort([5,9,1,2,3,4,10,12]))


heap_data = []
heappush(heap_data,10)
heappush(heap_data,6)
heappush(heap_data,7)
heappush(heap_data,2)
heappush(heap_data,5)
heappush(heap_data,2)
heappush(heap_data,22)
print(heap_data)
print(heappop(heap_data))
print(heappop(heap_data))
print(heappop(heap_data))
print(heappop(heap_data))
print(heappop(heap_data))
print(heappop(heap_data))
nlargest([5,6,1,2,3,101,102,3,21,2])

