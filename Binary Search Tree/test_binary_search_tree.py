import unittest
from binary_search_tree import Node, BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):
    def test_insert_value_when_no_item_is_inserted(self):
        a = BinarySearchTree()
        self.assertEqual(a.print_BST(), "()")
        
    def test_insert_value_when_one_item_is_inserted(self):
        a = BinarySearchTree()
        a.insert_value(11)
        self.assertEqual(a.print_BST(), "(11)")
        
    def test_insert_value_when_more_than_one_item_is_inserted(self):
        a = BinarySearchTree()
        a.insert_value(10)
        a.insert_value(7)
        a.insert_value(3)
        a.insert_value(4)
        a.insert_value(8)
        a.insert_value(12)
        a.insert_value(11)
        self.assertEqual(a.print_BST(), "(10 (7 (3 () (4)) (8)) (12 (11) ()))")
        
    def test_search_value_in_BST_for_empty_BST(self):
        a = BinarySearchTree()
        self.assertEqual(a.search_value_in_BST(10), False)
        
    def test_search_value_in_BST_for_non_empty_BST(self):
        a = BinarySearchTree()
        a.insert_value(10)
        a.insert_value(7)
        a.insert_value(3)
        a.insert_value(4)
        a.insert_value(8)
        a.insert_value(12)
        a.insert_value(11)
        self.assertEqual(a.search_value_in_BST(10), True)
        self.assertEqual(a.search_value_in_BST(100), False)
        
    def test_find_parent_for_rootNode(self):
        a = BinarySearchTree()
        a.insert_value(10)
        a.insert_value(7)
        a.insert_value(3)
        self.assertEqual(a.find_parent(a.search_node(10)), None)
    
    def test_find_parent_for_rootNode(self):
        a = BinarySearchTree()
        a.insert_value(50)
        a.insert_value(30)
        a.insert_value(25)
        a.insert_value(27)
        a.insert_value(13)
        a.insert_value(17)
        a.insert_value(3)
        self.assertEqual(a.find_parent(a.search_node(3)).data, 13)   
         
    def test_find_max(self):
        a = BinarySearchTree()
        a.insert_value(10)
        a.insert_value(7)
        a.insert_value(13)  
        a.insert_value(6)
        a.insert_value(15)  
        self.assertEqual(a.find_max(), 15) 
        self.assertEqual(a.find_min(), 6)    

    def test_find_min(self):
        a = BinarySearchTree()
        a.insert_value(10)
        a.insert_value(7)
        a.insert_value(13)  
        a.insert_value(6)
        a.insert_value(15)  
        self.assertEqual(a.find_min(), 6)         
    
    def test_delete_value_when_value_not_in_BST(self):
        a = BinarySearchTree()
        a.insert_value(10)
        a.insert_value(17)
        a.insert_value(8)
        a.insert_value(3)
        a.delete_value(22)
        self.assertEqual(a.print_BST(), '(10 (8 (3) ()) (17))')
        
    def test_delete_value_when_leaf_node_deleted(self):
        a = BinarySearchTree()
        a.insert_value(10)
        a.insert_value(17)
        a.insert_value(8)
        a.insert_value(3)
        a.delete_value(3)
        self.assertEqual(a.print_BST(), '(10 (8) (17))')   
    
    def test_delete_value2(self):
        a = BinarySearchTree()
        a.insert_value(10)
        a.insert_value(17)
        a.insert_value(8)
        a.insert_value(3)
        a.delete_value(8)
        self.assertEqual(a.print_BST(), '(10 (3) (17))') 
        
    def test_delete_value(self):
        a = BinarySearchTree()
        a.insert_value(10)
        a.insert_value(7)
        a.insert_value(3)
        a.insert_value(4)
        a.insert_value(8)
        a.insert_value(12)
        a.insert_value(11)
        a.delete_value(7)
        self.assertEqual(a.print_BST(), "(10 (4 (3) (8)) (12 (11) ()))")
              
if __name__ == '__main__':
    unittest.main()	
