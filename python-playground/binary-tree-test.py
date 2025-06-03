# Test Binary Tree ADT
# https://en.wikipedia.org/wiki/Binary_tree

# Assumptions:
# Elements will only be integers
# Tree starts unbalanced and unordered
# Trees can be the empty set.
# Trees have at most 2 children.
# Operations: Insert, Delete, 

class Element():
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

class BinaryTree():
    def __init__(self,root):
        self.root = Element(0)

    def Insert(self, newElement):
        print("NYI: Inserting a node.") 

def main():
    print("[+] Test Binary Tree Class\n")
    intro = "A binary tree is a type of data structure in which each node can have at most two children, referred to as the left child and the right child. It is commonly used in computer science for efficient data storage and retrieval, as well as for various operations like searching and sorting."
    print(intro + "\n - Duck Duck Go AI Assist ")
    root = Element(3)
    

if __name__ == "__main__":
    main()
