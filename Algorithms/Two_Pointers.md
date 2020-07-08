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

### Remove Duplicates

- Given an array of **sorted** numbers, remove all duplicates from it. You should **not use any extra space**; after removing the duplicates **in-place** return the new length of the array.

See **in-place?** think about this technique (does not use auxiliary data structure

```python
'''
Since we need to do this **in-place**, think about the **2 pointers approach**
In this case, one pointer loop through the array, the other one keeps
track of the index to put the next nonduplicate number
'''
def remove_duplicates(arr):
	# index of the next non-duplicate element
  add_non_duplicate = 1
  for curr in range(1, len(arr)):
    if arr[curr] != arr[add_non_duplicate-1]:
      arr[add_non_duplicate] = arr[curr]
      add_non_duplicate += 1
  return add_non_duplicate
'''
Time complexity: O(N)
Space complexity: O(1)
'''
```

**Takeaway:** know what each pointer represent, and when to increment / decrement each pointer

## 💥Triplet Sum to Zero

- Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

The 2 pointers approach need a **sorted input**, so pointer increment / decrement is predictable

**Sorting input** is also a good way to **remove duplicate**

```python
def search_triplets(arr):
  arr.sort()
  triplets = []
  for i in range(len(arr)):
    if i > 0 and arr[i] == arr[i-1]:  # skip same element to avoid duplicate triplets
      continue
    search_pair(arr, -arr[i], i+1, triplets)

  return triplets

def search_pair(arr, target_sum, left, triplets):
  right = len(arr) - 1
  while(left < right):
    current_sum = arr[left] + arr[right]
    if current_sum == target_sum:  # found the triplet
      triplets.append([-target_sum, arr[left], arr[right]])
      left += 1
      right -= 1
      while left < right and arr[left] == arr[left - 1]:
        left += 1  # skip same element to avoid duplicate triplets
      while left < right and arr[right] == arr[right + 1]:
        right -= 1  # skip same element to avoid duplicate triplets
    elif target_sum > current_sum:
      left += 1  # we need a pair with a bigger sum
    else:
      right -= 1  # we need a pair with a smaller sumdef search_triplets(arr):
  arr.sort()
  triplets = []
  for i in range(len(arr)):
    if i > 0 and arr[i] == arr[i-1]:  # skip same element to avoid duplicate triplets
      continue
    search_pair(arr, -arr[i], i+1, triplets)

  return triplets

def search_pair(arr, target_sum, left, triplets):
  right = len(arr) - 1
  while(left < right):
    current_sum = arr[left] + arr[right]
    if current_sum == target_sum:  # found the triplet
      triplets.append([-target_sum, arr[left], arr[right]])
      left += 1
      right -= 1
      while left < right and arr[left] == arr[left - 1]:
        left += 1  # skip same element to avoid duplicate triplets
      while left < right and arr[right] == arr[right + 1]:
        right -= 1  # skip same element to avoid duplicate triplets
    elif target_sum > current_sum:
      left += 1  # we need a pair with a bigger sum
    else:
      right -= 1  # we need a pair with a smaller sum
```
