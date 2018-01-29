import unittest
from stack import Stack

class TestStack(unittest.TestCase):
    def test_isEmpty_on_empty_stack(self):
		s = Stack()
		self.assertTrue(s.isEmpty())
	
	#also tests push() method	
    def test_isEmtpy_on_non_empty_stack(self):
        s = Stack()
        s.push('cat')
        s.push('dog')
        self.assertFalse(s.isEmpty())
                    
    def test_printStack_on_empty_stack(self):
        s = Stack()
        self.assertEqual(s.printStack(), [])
          
    def test_printStack_on_not_empty_stack(self):
        s = Stack()
        s.push('1')
        s.push('2')
        s.push('3')
        self.assertEqual(s.printStack(), ['3', '2', '1'])   
		
    def test_pop_on_empty_stack(self):
        s = Stack()
        with self.assertRaises(IndexError):
            s.pop()
			
    def test_pop_on_non_empty_stack(self):
        s = Stack()
        s.push('1')
        s.push('2')
        s.push('3')
        s.pop()
        self.assertEqual(s.printStack(), ['2', '1'])
    
    def test_peek_on_empty_stack(self):
        s = Stack()
        with self.assertRaises(IndexError):
            s.peek()
                
    def test_peek_on_non_empty_stack(self):
        s = Stack()
        s.push('1')
        s.push('2')
        s.push('3')
        self.assertEqual(s.peek(), '3')
        
    def test_size_of_empty_stack(self):
        s = Stack()
        self.assertEqual(s.size(), 0)
        
    def test_size_of_not_empty_stack(self):
        s = Stack()
        s.push('1')
        s.push('2')
        s.push('3')
        self.assertEqual(s.size(), 3)
     
if __name__ == '__main__':
    unittest.main()	
