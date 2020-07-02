A technique to **traverse a tree** in a **level by level** order

- Use a Queue to keep track of all the nodes of a level before jumping onto the next one.
- Space complexity will be O(W), where W is the maximum number of nodes on any level

**Takeaways:**

- Use queue for BFS
- check if root is None
- while queue is not empty
- if different level of the tree matters, have a variable level_len & a for loop to distinguish different levels
