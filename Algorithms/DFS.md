This pattern is based on the **Depth First Search (DFS)** technique to traverse a tree.

We will be using recursion (or we can also use a stack for the iterative approach) to keep track of all the previous (parent) nodes while traversing. This also means that the space complexity of the algorithm will be O(H)_O_(_H_), where ‘H’ is the maximum height of the tree.

Description: A technique to traverse a tree

- Use recursion (or use a stack for the iterative approach) to keep track of all the previous (parent) nodes while traversing
- Space complexity will be O(H), where 'H' is the maximum height of the tree
- We use DFS to search for a **root-to-leaf path**
