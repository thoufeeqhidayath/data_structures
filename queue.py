

class Queue():
    def __init__(self,data:list):
        self.data = data

    def is_empty(self):
        return len(self.data)==0

    def enqueue(self,value):
        self.data.append(value)

    def dequeue(self,):
        if self.data:
         return self.data.pop(0)
    def __repr__(self):
        return str(self.data)

# q =Queue([1,2,3,4,5])
# q.enqueue(6)
# q.enqueue(7)
# print(q)
# q.dequeue()
#
# print(q)
# q.dequeue()
#
# print(q)
