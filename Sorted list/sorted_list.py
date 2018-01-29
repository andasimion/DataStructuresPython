class SortedList:
	
    def __init__(self):
        self.items = []
	
    def isEmpty(self):
	    return self.items == []

    # insertion using liniar search O(n)
    def insert_item_slow(self, item):
	    if len(self.items) == 0:
		    self.items.append(item)
		    return 
	    index = 0
	    for i in range(len(self.items)):
		    if item <= self.items[i]:
			    break
		    else:
			    index = i + 1
	    self.items.insert(index, item)
	
    # insertion using binary search	O(log n)
    def insert_item_fast(self, item):
	    if  len(self.items) == 0:
		    self.items.append(item)
		    return
	    min_index = 0
	    max_index = len(self.items)
	    while min_index < max_index:
		    index = (min_index + max_index)/2
		    if item <= self.items[index]:
			    max_index = index 
		    else:
			    min_index = index + 1
	    self.items.insert(min_index, item)
    
    def remove_item(self, index):
        if index > len(self.items) - 1:
            raise IndexError ("The list is too short!")
        self.items.pop(index)

    def get_item(self, index):
        if index > len(self.items) - 1:
            raise IndexError ("The list is too short!")
        return self.items[index]
	
    def size(self):
	    return len(self.items)

    def print_sorted_list(self):
	    return self.items
	
