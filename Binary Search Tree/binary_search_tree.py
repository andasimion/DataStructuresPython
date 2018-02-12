class Node:
    def __init__(self, data, leftNode=None, rightNode=None):
        self.data = data
        self.leftNode = leftNode
        self.rightNode = rightNode
   
   # returns True or False
    def is_leaf(self):
        return self.leftNode is None and self.rightNode is None
    
    def has_leftNode(self):
        return self.leftNode != None
        
    def has_rightNode(self):
        return self.rightNode != None
        
    def __repr__(self):
        return repr((self.data))
        
class BinarySearchTree:
    def __init__(self):
        self.rootNode = None
    
    def insert_value(self, value):
        self.insert_value_under_node(self.rootNode, value)
            
    def insert_value_under_node(self, node, value):
        if self.rootNode is None:
            self.rootNode = Node(value)
            return
        if value <= node.data:
            if node.leftNode is None:
                #insert new node as left child
                node.leftNode = Node(value)
            else:
                self.insert_value_under_node(node.leftNode, value)
        else:
            if node.rightNode is None:
                #insert new node as right child
                node.rightNode = Node(value)
            else:
                self.insert_value_under_node(node.rightNode, value)
    
    # search if a value is in the BST an returns True or Flase
    def search_value_in_BST(self, value):
        return self.search_node(value) is not None
    
    #returns a node for a value
    def search_node(self,value):
        return self.search_node_rec(self.rootNode, value)
    
    def search_node_rec(self, node, value):
        if node is None:
            return None
        if value == node.data:
            return node
        if value < node.data:
            return self.search_node_rec(node.leftNode, value)
        if value > node.data:
            return self.search_node_rec(node.rightNode, value) 
    
    #works only if the tree is a true binary search tree
    #target_node is the childNode for which we want to find the parent
    def find_parent(self, target_node):
        if target_node == self.rootNode:
            return None
        return self.find_parent_rec(self.rootNode, target_node)
        
    def find_parent_rec(self, root, target_node):
        if root is None:
            return None
        if root.leftNode == target_node or root.rightNode == target_node:
            return root
        if target_node.data < root.data:
            return self.find_parent_rec(root.leftNode, target_node)
        if target_node.data > root.data:
            return self.find_parent_rec(root.rightNode, target_node)
   
    def find_max(self):
        return self.find_max_rec(self.rootNode)
        
        
    #finds the maximum value from the a tree 
    def find_max_rec(self, node):
        if node is None:
            return None
        if node.rightNode is None:
            return node.data
        return self.find_max_rec(node.rightNode)
    
    def find_min(self):
        return self.find_min_rec(self.rootNode)   
         
    def find_min_rec(self, node):
        if node is None:
            return None
        if node.leftNode is None:
            return node.data
        return self.find_min_rec(node.leftNode)
    
    def detach_node(self, node):
        parent = self.find_parent(node)
        if parent.leftNode == node:
            parent.leftNode = None
        else:
            parent.rightNode = None
    
    def delete_value(self, value):
        node_with_value_to_delete = self.search_node(value)
        if node_with_value_to_delete is None:
            return
        max_value = self.find_max_rec(node_with_value_to_delete.leftNode)
        min_value = self.find_min_rec(node_with_value_to_delete.rightNode)
        node_with_max_value = self.search_node(max_value)
        node_with_min_value = self.search_node(min_value)        
        if node_with_value_to_delete.leftNode is not None:
        # we must first detach the node and after that change the value in the node_with_value_to_delete
            self.detach_node(node_with_max_value)
            node_with_value_to_delete.data = max_value
        elif node_with_value_to_delete.rightNode is not None:
            self.detach_node(node_with_min_value)
            node_with_value_to_delete.data = min_value 
        else:
            self.detach_node(node_with_value_to_delete)     
   
    def print_BST(self):
        return self.print_a_node(self.rootNode)
         
    def print_a_node(self, node):
        if node is None:
            return "()"
        if node.is_leaf():
            return "(" + str(node.data) + ")"
        return "(" + str(node.data) + " " + self.print_a_node(node.leftNode) + " " + self.print_a_node(node.rightNode) + ")"
            
        
    
        

