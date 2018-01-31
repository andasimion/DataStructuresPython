import unittest
from priority_queue_with_sorted_list import PriorityQueueWithSortedList

class TestPriorityQueueWithSortedList(unittest.TestCase):
    
    def test_isEmpty_on_empty_priority_queue(self):
        q=PriorityQueueWithSortedList()
        self.assertTrue(q.isEmpty())
        
    def test_isEmpty_on_non_empty_priority_queue(self):
        q=PriorityQueueWithSortedList()
        q.enqueue(1, 'A')
        self.assertFalse(q.isEmpty())
        
    def test_enqueue(self):
        q=PriorityQueueWithSortedList()
        q.enqueue(1, 'A')
        q.enqueue(0, 'B')
        q.enqueue(0, 'C')
        q.enqueue(2, 'D')
        self.assertEqual(q.printPriorityQueue(), [(0, 'B'), (0, 'C'),(1, 'A'), (2, 'D')])
        
    def test_dequeue_on_empty_priority_queueu(self):
        q=PriorityQueueWithSortedList()
        with self.assertRaises(IndexError):
            q.dequeue()

    def test_dequeue_on_non_empty_priority_queueu(self):
        q=PriorityQueueWithSortedList()
        q.enqueue(1, 'A')
        q.enqueue(0, 'B')
        q.enqueue(2, 'C')
        q.dequeue()
        self.assertEqual(q.printPriorityQueue(), [(1, 'A'), (2, 'C')])
    
    def test_first_on_empty_priority_queue(self):
        q=PriorityQueueWithSortedList()
        self.assertEqual(q.first(), None)
        
    def test_first_on_non_empty_priority_queue(self):
        q=PriorityQueueWithSortedList()
        q.enqueue(1, 'A')
        q.enqueue(0, 'B')
        q.enqueue(2, 'C')
        self.assertEqual(q.first(), 'B')
        
if __name__ == '__main__':
    unittest.main()

	
