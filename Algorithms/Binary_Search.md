When we are given a **sorted Array** or **LinkedList**, and we are asked to find a certain element, the best alg we can use is **Binary Search**

### Order-agnostic Binary Search

Given a sorted array of numbers, find if a given number ‘key’ is present in the array. Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order. You should assume that the array can have duplicates.

Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.

```python
def binary_search(arr, key):
  start, end = 0, len(arr) - 1
	# check if the sorted array is ascending or not
  isAscending = arr[start] < arr[end]
  **while start <= end:**
    # calculate the middle of the current range
		# use this instead of (start + end) // 2 to prevent integer overflow
		# which isn't a problem in Python, it is in Java, C, etc. though
    mid = start + (end - start) // 2

    if key == arr[mid]:
      return mid

    if isAscending:  # ascending order
      if key < arr[mid]:
        end = mid - 1  # the 'key' can be in the first half
      else:  # key > arr[mid]
        start = mid + 1  # the 'key' can be in the second half
    else:  # descending order
      if key > arr[mid]:
        end = mid - 1  # the 'key' can be in the first half
      else:  # key < arr[mid]
        start = mid + 1  # the 'key' can be in the second half

  return -1  # element not found

'''
Time complexity: O(logN) since we are reducing the search by half at every step
Space complexity: O(1)
'''
```
