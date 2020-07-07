- In problems where we deal \***\*with **sorted arrays (or LinkedLists)** and need to find a **set of elements** (pair, triplet, subarray, etc) \*\***that **fulfill certain constraints.**

## Problems

---

### Pair with Target Sum

- Given an array of **sorted** numbers and a target sum, find a **pair in the array whose sum is equal to the given target**.

  Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

```python
'''
Brute force would take one number at a time and search for the second
number through **binary search** -> O(N*logN)
**We can do better using the two pointers approach
'''**
def pair_with_targetsum(arr, target_sum):
	left, right = 0, len(arr) - 1
	while (left < right):
		current_sum = arr[left] + arr[right]
		if current_sum == target_sum:
			return [left, right]
		if target_sum > current_sum:
			left += 1    # We need a pair with a bigger sum
		else:
			right -= 1    # We need a pair with a smaller sum
	return [-1, -1]

**'''
Time complexity is O(N)
Space complexity is O(1)
'''

# We can also use a hashtable to search for the required pair**
```
