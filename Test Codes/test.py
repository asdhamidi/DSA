import sys
sys.path.append('C:/Users/asadu/Desktop/Code/DSA/Tree')
from binary_search_tree import BST

b = BST()
b.insert(5)
b.insert(9)
b.insert(1)
b.insert(15)
b.insert(11)

b.show(2)
if b.search(b.get_root(), 15):
    print("\n15 is found.")
else:
    print("Not found.")