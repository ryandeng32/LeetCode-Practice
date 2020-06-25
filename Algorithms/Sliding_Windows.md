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
