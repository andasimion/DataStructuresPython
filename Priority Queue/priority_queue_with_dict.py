class PriorityQueueWithDict:
    
    def __init__ (self):
        self.dict = {}
        
    def isEmpty(self):
        return bool(self.dict)
        
# keys are the priority and values are list that contain the items 
    def enqueue(self, priority, item):
        self.dict.setdefault(priority, []).append(item)

    def values_at_index(self, i):
        return self.dict[sorted(self.dict.keys())[i]]
	    
    def dequeue(self):
        if self.dict == {}:
             raise KeyError ("Empty priority queue!")
        i = 0
        index = len(self.dict.keys()) - 1
        for key in self.dict:
            if self.values_at_index(i) != [] and i <= index:
                del self.values_at_index(i)[0]
                return
            else:
                i = i + 1

#returns the first element to be dequeued                
    def first(self):
        if self.dict == {}:
            return None
        i = 0
        index = len(self.dict.keys()) - 1
        for key in self.dict:
            if self.values_at_index(i) != [] and i <= index:
                return self.values_at_index(i)[0]
            else:
                i = i + 1
                
#prints the values depending on the priority and the order of insertion in the dictionary
    def printPriorityQueue(self):
        ordered_values = []
        i = 0
        for key in self.dict:
            ordered_values += self.values_at_index(i)
            i = i + 1
        return ordered_values
                
    def size(self):
        return len(self.printPriorityQueue())
        

