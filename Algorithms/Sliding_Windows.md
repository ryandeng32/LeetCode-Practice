## Why

---

- A sliding window approach generally helps us **reduce the time complexity for brute force approaches**

**What is sliding window?**

- **Type 1:** Fixed size sliding window
- **Type 2:** Dynamically resizable windows
- Which type depends on the question

**What are the benefits?**

- Prevent unnecessary iteration over elements we have already seen, this usually yields a O(n^2) time complexity
- Save us from re-calculating overlapping elements
- Sliding window optimize it into linear time
- O(n) time complexity and O(1) space complexity

**How to spot the problems?**

- Things we iterate over sequentially
  - Contiguous sequence of elements
  - strings, arrays, linked lists
- Finding min, max, longest, shortest, contained

**Question Variants**

- **Fixed length:** max sum subarray of size K
- **Dynamic Variant:** smallest sum ≥ to some value S
- **Dynamic Variant with Auxiliary Data Structure** (dictionaries, etc) **:** Longest substring with no more than K distinct characters
  - Use hashmap to remember the frequency of elements
- **String Permutations**

**Commonalities:**

- Everything grouped sequentially
- Longest/smallest/contains/max/min
  **Examples & Implementation**

1. Find the max sum subarray of a fixed size K

```python
'''
Find the max sum subarray of a fixed size K
Example input: [4,2,1,7,8,1,2,8,1,0], K = 3
output: 16
'''
def findMaxSumSubarray(arr, k):
	maxValue = -float('inf')
	currentRunningSum = 0

	for i in range(len(arr)):
		currentRunningSum += arr[i]
		if i >= k - 1:
			maxValue = max(maxValue, currentRunningSum)
			currentRunningSum -= arr[i-k+1]
	return maxValue

# O(n) time, O(1) space
```

2. Smallest subarray with given sum

```python
def smallestSubarrayGiveSum(arr, targetSum):
	minWindowSize = float('inf')
	currentWindowSum = 0
	windowStart = 0
	for windowEnd in range(len(arr)):
		currentWindowSum += arr[windowEnd]
		while currentWindowSum >= targetSum:
			minWindowSize = min(minWindowSize, windowEnd - windowStart + 1)
			# shrinking the window
			currentWindowSum -= arr[windowStart]
			windowStart += 1
	if minWindowSize == float('inf'):
		return 0
	return minWindowSize
''' O(n) time, outer for loop runs for all elements and the
inner while loop process each element once, so it's O(n + n) -> O(n)
O(1) space'''
```
