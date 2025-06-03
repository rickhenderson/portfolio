# Test Binary Tree ADT
# https://en.wikipedia.org/wiki/Binary_tree

# Assumptions:
# Elements will only be integers
# Tree starts unbalanced and unordered
# Trees can be the empty set.
# Trees have at most 2 children.
# Operations: Insert, Delete,


class Element:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None
        # Maybe an element should be a List?
        # self = [value, None, None]

    def __str__(self):
        return f"[{self.value}].Left[{self.leftChild}].Right[{self.rightChild}]"


class BinaryTree:
    def __init__(self, root):
        self.root = Element(0)

    def Insert(self, newElement):
        if self.root.leftChild == None:
            self.root.leftChild = newElement
        elif self.root.rightChild == None:
            self.root.rightChild == newElement
        else:
            self.Insert(self.root.leftChild, newElement)
            # This could be recursive and it has no stop condition. I think.


def main():
    print("[+] Test Binary Tree Class\n")
    intro = """
    A binary tree is a type of data structure in which each node can have at most two children, 
    referred to as the left child and the right child. 
    It is commonly used in computer science for efficient data storage and retrieval, 
    as well as for various operations like searching and sorting."
    """
    print(intro + "\n - Duck Duck Go AI Assist\n\n")

    root = Element(3)
    print(root)

    myTree = BinaryTree(root)
    print(myTree)
    print("3 ,None, None")

    item = Element(10)
    print(item)
    myTree.Insert(item)
    print("3, 10, None")

    item = Element(5)
    print(item)
    myTree.Insert(item)
    print("3, 10, 5")

    print("Now it get's tricky! Attempting to insert into a full tree!")
    item = Element(6)
    myTree.Insert(item)
    print("If it didn't crash, we need to find a way to print the tree.")
    print(myTree)
    print(f"My Tree Root: {myTree.root}")
    print(f"Root Left: {myTree.root.leftChild}")
    print(f"Root Right: {myTree.root.rightChild}")
    myTree.Insert(item)
    print(f"My Tree Root: {myTree.root}")
    print("Nope that's not working.")


if __name__ == "__main__":
    main()
