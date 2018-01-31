import unittest
from priority_queue_with_dict import PriorityQueueWithDict

class TestPriorityQueueWithDict(unittest.TestCase):

    def test_isEmpty_on_empty_priority_queue(self):
        q = PriorityQueueWithDict()
        self.assertFalse(q.isEmpty())
    
    def test_isEmpty_on_non_empty_priority_queue(self):
        q = PriorityQueueWithDict()
        q.enqueue(1,'A')
        q.enqueue(1,'B')
        self.assertTrue(q.isEmpty())
        
    def test_enqueue(self):
        q = PriorityQueueWithDict()
        q.enqueue(1, 'A')
        q.enqueue(0, 'B')
        q.enqueue(1, 'C')
        q.enqueue(2, 'D')
        q.enqueue(1, 'E')
        q.enqueue(0, 'F')
        self.assertEqual(q.printPriorityQueue(), ['B', 'F', 'A', 'C', 'E', 'D'])
        
    def test_dequeue_on_empty_priority_queue(self):
        q = PriorityQueueWithDict()
        with self.assertRaises(KeyError):
            q.dequeue()
            
    def test_dequeue_on_non_empty_priority_queue(self):        
        q = PriorityQueueWithDict()
        q.enqueue(1, 'A')
        q.enqueue(0, 'B')
        q.enqueue(1, 'C')
        q.enqueue(2, 'D')
        q.enqueue(1, 'E')
        q.enqueue(0, 'F')
        q.dequeue()
        self.assertEqual(q.printPriorityQueue(), ['F', 'A', 'C', 'E', 'D']) 
    
    def test_first_on_empty_priority_queue(self):
         q = PriorityQueueWithDict()
         self.assertEqual(q.first(), None)
    
    def test_first_on_non_empty_priority_queue(self):
         q = PriorityQueueWithDict()
         q.enqueue(1, 'A')
         q.enqueue(2, 'D')
         q.enqueue(0, 'F')
         q.enqueue(0, 'E')
         self.assertEqual(q.first(), 'F')
              
    def test_size_on_empty_priority_queue(self):        
        q = PriorityQueueWithDict()
        self.assertEqual(q.size(), 0)
         
    def test_size_on_non_empty_priority_queue(self):        
        q = PriorityQueueWithDict()
        q.enqueue(1, 'A')
        q.enqueue(0, 'B')
        q.enqueue(1, 'C')
        self.assertEqual(q.size(), 3) 
        
if __name__ == '__main__':
    unittest.main()

	



