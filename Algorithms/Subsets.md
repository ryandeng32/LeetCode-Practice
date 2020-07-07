**Use case:** questions involving dealing with **permutations** and **combinations of a given set of elements**

- This pattern describe an efficient **BFS** approach to handle all these problems
  **Given a set with distinct elements, find all of its distinct subsets**

**Input:** [1,3]

**Output:** [], [1], [3], [1,3]

```python
# we can use BFS to generate all subsets of the given set
'''
Given set: [1, 5, 3]

Start with an empty set: [[]]
Add the first number (1) to all the existing subsets to create new subsets: [[], [1]];
Add the second number (5) to all the existing subsets: [[], [1], [5], [1,5]];
Add the third number (3) to all the existing subsets: [[], [1], [5], [1,5], [3], [1,3], [5,3], [1,5,3]].
'''
def find_subsets(nums):
  subsets = []
  # start by adding the empty subset
  subsets.append([])
  for currentNumber in nums:
    # we will take all existing subsets and insert the current number in them to create new subsets
    n = len(subsets)
    for i in range(n):
      # create a new subset from the existing subset and insert the current element to it
      set = list(subsets[i])
      set.append(currentNumber)
      subsets.append(set)

  return subsets

'''
Time complexity: O(2^n) since number of subsets to add doubles every step
Space complexity: O(2^n) since we have O(2^n) subsets
'''
```
