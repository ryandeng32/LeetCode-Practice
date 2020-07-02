A technique to **traverse a tree** in a **level by level** order

- Use a Queue to keep track of all the nodes of a level before jumping onto the next one.
- Space complexity will be O(W), where W is the maximum number of nodes on any level

**Takeaways:**

- Use queue for BFS
- check if root is None
- while queue is not empty
- if different level of the tree matters, have a variable level_len & a for loop to distinguish different levels

```python
'''
Given a binary tree, populate an array to represent its level-by-level traversal.
You should populate the values of all nodes of each level from left to right in separate sub-arrays.
'''
from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = []
  if root is None:
    return result
	# push the root node to queue
  queue = deque()
  queue.append(root)
	# keep iterating until the queue is empty
  while queue:
		# count the elements in the current level
    levelSize = len(queue)
    currentLevel = []
    for _ in range(levelSize):
      currentNode = queue.popleft()
      # add the node to the current level
      currentLevel.append(currentNode.val)
      # insert the children of current node in the queue
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)

    result.append(currentLevel)

  return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))

main()
'''
time complexity is O(n) because we traverse each node once
space complexity is O(n) because we need a list and a queue, each of them is O(n)
'''
```

- when it comes to inserting element at the beginning of an iterable, we can use deque, or linked list, since these 2 will be more efficient O(1) than a list O(n), where you have to shift all the elements
