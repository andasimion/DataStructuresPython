import unittest
from queue import Queue

class TestQueue(unittest.TestCase):
    def test_isEmpty_on_empty_queue(self):
        q = Queue()
        self.assertTrue(q.isEmpty())
        
    def test_isEmpty_on_non_empty_queue(self):
        q = Queue()
        q.enqueue('A')
        self.assertFalse(q.isEmpty())
    
    def test_printQueue_on_empty_queue(self):
        q = Queue()
        self.assertEqual(q.printQueue(), [])
    
    #also test enqueue method
    def test_printQueue_on_non_empty_queue(self):
        q = Queue()
        q.enqueue('1')
        q.enqueue('2')
        q.enqueue('3')
        q.enqueue('4')
        self.assertEqual(q.printQueue(), ['1', '2', '3', '4'])
    
    def test_dequeue_on_empty_queue(self):
        q = Queue()
        with self.assertRaises(IndexError):
            q.dequeue()

    def test_dequeue_on_non_empty_queue(self):
        q = Queue()
        q.enqueue('1')
        q.enqueue('2')
        q.enqueue('3')
        q.dequeue()
        q.enqueue('4')
        self.assertEqual(q.printQueue(),['2', '3', '4'])
        
    def test_first_on_empty_queue(self):
        q = Queue()
        with self.assertRaises(IndexError):
            q.first()
          
    def test_first_on_non_empty_queue(self):
        q = Queue()
        q.enqueue('1')
        q.enqueue('2')
        q.enqueue('3')
        self.assertEqual(q.first(), '1')
    
    def test_size_on_empty_queue(self):
        q = Queue()
        self.assertEqual(q.size(), 0)

    def test_size_on_non_empty_queue(self):
        q = Queue()
        q.enqueue('1')
        q.enqueue('2')
        q.enqueue('3')
        q.dequeue()
        q.enqueue('4')
        self.assertEqual(q.size(), 3)
         

if __name__ == '__main__':
    unittest.main()	
