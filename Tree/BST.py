"""
Code for a Binary Search Tree.
"""
from simpleTree import Tree, Node

class BST(Tree):
	def search(self, root, data):
		"""
		Method for searching for an element in a BST.
		
		root (Node): Base of the tree.
		data (int/str): Element to look for in the tree.

		returns: True if element is found, False otherwise.
		"""
		if not root: # Base Case
			return False

		if data == root.data:
			return True
		elif data > root.data:
			return self.search(root.right, data)
		else:
			return self.search(root.left, data)
		
	def insert(self, data):
		"""
		Method for inserting an element in a BST.

		root (Node): Base of the tree.
		data (int/str): Element to look for in the tree.

		returns: None
		"""
		if not self.root:
			self.root =  Node(data)
		else:
			root = self.root
			while root:
				if root.data == data:
					return
				elif data > root.data:
					if root.right:
						root = root.right
					else:
						root.right = Node(data)
						return
				else:
					if root.left:
						root = root.left
					else:
						root.left = Node(data)
						return

if __name__ == "__main__":
	t = BST()
	for r in range(5): t.insert(int(input("Enter the element: ")))
	t.show(2)
	if t.search(t.get_root(), 3):
		print("Element present")
	print("Height of the BST : ", t.height(t.get_root()))
	print("Number of Nodes : ", t.count(t.get_root()))