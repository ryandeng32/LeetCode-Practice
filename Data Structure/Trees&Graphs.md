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
