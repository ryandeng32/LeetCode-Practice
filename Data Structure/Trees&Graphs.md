- A graph is **a collection of nodes with edges between (some of) them**
  - Can be **directed** (one-way street) \***\*or **undirected\*\* (two-way street).

## Basics

---

```python
# Simple definition of a tree node
class Node:
	def __init__(self):
		self.val = None # value of the node
		self.children = None # a list of nodes
```

**Binary Tree:** A tree in which each node has up to two children

**Binary Search Tree:** A binary tree in which every node fits a specific ordering property: **all left descendents ≤ n < all right decendents** for each node n

You should clarify the definition with the interviewer, e.g. **for BST, what will duplicate input behave ?**

**Balanced vs. Unbalanced:** balanced trees are "not terribly imbalanced", it's balanced enough to ensure O( log n ) time for insert and find, not necessarily "perfectly balanced"

## Binary Tree traversal

---

```python
# Binary tree node definition
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

root = TreeNode(12)
root.left = TreeNode(7)
```

**Three types of traversal:** in-order, post-order, and pre-order

```python
**# In-order traversal**
# visit the left branch, then the current node, and finally the right node
def inOrderTraversal(node):
	if node:
		inOrderTraversal(node.left)
		visit(node)
		inOrderTraversal(node.right)

# when performed on a binary search tree, it visits the nodes in ascending order (in-order)
```

```python
**# Post-order traversal**
# visit the current node after its child nodes (post-order)
def postOrderTraversal(node):
	if node:
		postOrderTraversal(node.left)
		postOrderTraversal(node.right)
		visit(node)

# the root is always the last node visited
```

```python
**# Pre-order traversal**
# visit the current node before its child nodes (post-order)
def postOrderTraversal(node):
	if node:
		visit(node)
		postOrderTraversal(node.left)
		postOrderTraversal(node.right)

# the root is always the first node visited
```

## Graphs

---

- A tree is a type of graph, a tree is a **connected graph without cycles**

**2 common ways to represent a graph:** adjacency list & adjacency matrices

```python
**# Adjacency List**
# Most common way to represent a graph, each vertex (node) stores a list of adjacent nodes
class Graph:
# Graph class is used because, unlike in a tree, you can't necessarily reach all the nodes from a single node
	def __init__(self, nodes = None):
		self.nodes = nodes # a list of adjacent nodes
class Node:
	def __init__(self, name = None, children = None):
		self.name = name
		self.children = children
```

**Adjacent Matrices (explore later)**

## Graph Search

---

2 most common ways to search a graph: **depth-first search & breadth-first search**

## Extra

---

- **Binary Heaps & Tries**
