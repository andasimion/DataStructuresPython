class Stack:
    def __init__(self):
        self.items = []
		
    def isEmpty(self):
        return self.items == []
	
    def push(self, item):
        self.items.append(item)

#pop() retrives and removes the last item of the stack
    def pop(self):
        if len(self.items) == 0:
            raise IndexError ("The stack is empty!")
        self.items.pop() 
# retrives the next element that is going to pe popped    
    def peek(self):
        if len(self.items) == 0:
            raise IndexError ("The stack is empty!")
        return self.items[-1]
        
    def size(self):
        return len(self.items)
	
	#prints the elements in the order that they will be poped	
    def printStack(self):
        return list(reversed(self.items))
