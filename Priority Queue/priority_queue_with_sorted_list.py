class PriorityQueueWithSortedList:
    
    def __init__ (self):
        self.items = []

    def isEmpty(self):
        return self.items == []

#inserts using binary search tuples where the first element is the priority and the second one is the item
    def enqueue(self, priority, item):
        min_index = 0
        max_index = len(self.items)
        while min_index < max_index:
            index = (min_index + max_index)/2
            if self.items[index][0] <= priority:
                min_index = index + 1
            else:
                max_index = index
        self.items.insert(min_index, (priority, item))
        
    def dequeue(self):
        if len(self.items) == 0:
            raise IndexError ("Empty list!")
        self.items.pop(0)

#returns the first element to be dequeued         
    def first(self):
        if len(self.items) == 0:
            return None
        return self.items[0][1]
        
    def printPriorityQueue(self):
        return self.items
        
