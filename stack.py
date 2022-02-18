

class Stack:
    def __init__(self,item):
        self.data = item

    def push(self,data):
        self.data.append(data)

    def pop(self):
        if self.data:
            return self.data.pop()

    def __len__(self):
        return len(self.data)
