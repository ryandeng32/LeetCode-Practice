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

- What consists the initial window
- When do we shrink?
- What to do after shrinking?
- How to analysis time complexity:

  - O(N \* (complexity of the most expensive operation done in the iteration )

  We start with a window [Start,End] with Start = 0 and End = 0 initially.Now in those while loops we essentially either shrink or expand the window.Shrink from the left end by increasing the Start pointerAnd expand from the right end by increasing the End pointer.

  The crucial thing to note is that after each iteration of we reach a new window state and we continue this until the window reaches the end.It is also clear that the Start and End pointers only increase. Which means that Start will go from 0 to N and End will go from 0 to N.The combination of [Start, End] hence can produce only O(N) unique windows.

  Hence the total complexity would be linear that is O(N).

  Pro tip: We can write a formula :Time is : O ( N \* ( complexity of the most expensive operation done in the iteration) )

  Here you are using hashmap which has O(1) time for put and get hence complexity is O ( N \* 1 ) => O ( N ).

  - so if we use hashmap, it will be O (N \* 1) = O(N)

  Longest substring with K Distinct Characters (medium)

  ```python
  def length_of_longest_substring(str1, k):
    window_start, max_length, max_repeat_letter_count = 0, 0, 0
    frequency_map = {}

    # Try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
      right_char = str1[window_end]
      if right_char not in frequency_map:
        frequency_map[right_char] = 0
      frequency_map[right_char] += 1
      max_repeat_letter_count = max(
        max_repeat_letter_count, frequency_map[right_char])

      # Current window size is from window_start to window_end, overall we have a letter which is
      # repeating 'max_repeat_letter_count' times, this means we can have a window which has one letter
      # repeating 'max_repeat_letter_count' times and the remaining letters we should replace.
      # if the remaining letters are more than 'k', it is the time to shrink the window as we
      # are not allowed to replace more than 'k' letters
      if (window_end - window_start + 1 - max_repeat_letter_count) > k:
        left_char = str1[window_start]
        frequency_map[left_char] -= 1
        window_start += 1

      max_length = max(max_length, window_end - window_start + 1)
    return max_length

  def main():
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))

  main()
  ```

  [Intuitive explanation of why O(N) sliding window does not work if negative numbers are allowed? - LeetCode Discuss](https://leetcode.com/problems/minimum-size-subarray-sum/discuss/209740/intuitive-explanation-of-why-on-sliding-window-does-not-work-if-negative-numbers-are-allowed)

  [Subarray Sum Equals K - LeetCode](https://leetcode.com/problems/subarray-sum-equals-k/solution/)

  No-repeat Substring (Hard)

  longest substring with the same letters after replacement

  Sliding_window is a form of 2 pointers method
