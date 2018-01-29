import unittest
from sorted_list import SortedList

class TestSortedList(unittest.TestCase):
	
    def test_isEmpty_on_empty_list(self):
        l = SortedList()
        self.assertTrue(l.isEmpty())
		
    def test_isEmpty_on_non_empty_list(self):
        l = SortedList()
        l.insert_item_fast('77')
        self.assertFalse(l.isEmpty())
		
    def test_linear_insertion_worst_case_scenario(self):
        l = SortedList()
        l.insert_item_slow(1)
        l.insert_item_slow(2)
        l.insert_item_slow(3)
        l.insert_item_slow(4)
        l.insert_item_slow(5)
        self.assertEqual(l.print_sorted_list(), [1,2,3,4,5])
	
    def test_linear_insertion_best_case_scenario(self):
        l = SortedList()
        l.insert_item_slow(5)
        l.insert_item_slow(4)
        l.insert_item_slow(3)
        l.insert_item_slow(2)
        l.insert_item_slow(1)
        self.assertEqual(l.print_sorted_list(), [1,2,3,4,5])
		
    def test_linear_insertion_stress_case(self):
        l = SortedList()
        for i in range(1000):
            l.insert_item_slow(i) 
        self.assertEqual(l.print_sorted_list(), range(1000))
		
    def test_binary_insertion_worst_case_scenario(self):
        l = SortedList()
        l.insert_item_fast(1)
        l.insert_item_fast(2)
        l.insert_item_fast(3)
        l.insert_item_fast(4)
        l.insert_item_fast(5)
        self.assertEqual(l.print_sorted_list(), [1,2,3,4,5])
		
    def test_binary_insertion_stress_case(self):
        l = SortedList()
        for i in range(1000):
            l.insert_item_fast(i)
        self.assertEqual(l.print_sorted_list(), range(1000))
	
    def test_remove_item(self):
        l = SortedList()
        for i in range(10):
            l.insert_item_slow(i)
        l.remove_item(5)
        self.assertEqual(l.print_sorted_list(), [0,1,2,3,4,6,7,8,9])
		
    def test_remove_item_for_nonexistent_index(self):
        l = SortedList()
        l.insert_item_fast(1)
        l.insert_item_fast(2)
        l.insert_item_fast(3)
        with self.assertRaises(IndexError):
            l.remove_item(3)
		
    def test_get_item(self):
        l = SortedList()
        for i in range(10):
            l.insert_item_slow(i)
        self.assertEqual(l.get_item(5), 5)

    def test_get_item_for_nonexistent_index(self):
        l = SortedList()
        l.insert_item_fast(1)
        l.insert_item_fast(2)
        l.insert_item_fast(3)
        with self.assertRaises(IndexError):
            l.get_item(3)   

if __name__ == '__main__':
    unittest.main()	
