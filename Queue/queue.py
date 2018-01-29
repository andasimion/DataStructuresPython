class Queue:
    def __init__(self):
        self.items = []
		
    def isEmpty(self):
        return self.items == []
		
    def enqueue(self, item):
        self.items.append(item)
		
    def dequeue(self):
        if len(self.items) == 0:
            raise IndexError ("Empty queue!")
        self.items.pop(0)

#retrieves the next element that is going to be poped        
    def first(self):
        if len(self.items) == 0:
            raise IndexError ("Empty queue!")
        return self.items[0]
		
    def size(self):
        return len(self.items)
	
	#prints the elements in the order that they will be dequeued
    def printQueue(self):
        return self.items
			

