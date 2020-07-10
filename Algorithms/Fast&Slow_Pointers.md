- Also known as the **Hare & Tortoise algorithm.**
- Use two pointers which move through the array (or sequence/LinkedList) **at different speeds**
- Useful when dealing with **cyclic LinkedList or arrays**

### LinkedList Cycle (easy)

- Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.

```python
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def has_cycle(head):
  # TODO: Write your code here
  slow, fast = head, head
	# make sure that fast isn't the end and fast.next.next is valid
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return True  # found the cycle
	# fast pointer reaches the end, no cycle
  return False

'''
Time complexity: O(N)
Space complexity: O(1)
'''
```

**Idea:** Imagine racers running in a circular racing track. the faster racer is bound is catch up and cross the slower racer from behind.

- What if we also want to find the length of the cycle

```python
'''
Once the fast and slow pointers meet,
we can save the slow pointer and iterate the whole cycle with
another pointer until we see the slow pointer again to find the length
'''
def calculate_cycle_length(slow):
	current = slow
	cycle_length = 0
	while True:
		current = current.next
		cycle_length += 1
		if current == slow:
			break
	return cycle_length
```

- How to find the start of the cycle

Any problems dealing with a cycle can think about **fast and slow pointers**

```python
if head is None:
    return None
  slow, fast = head, head
  length = 1
  while fast.next:
    length += 1
    fast = fast.next
  mid = length // 2 + 1
  while mid > 1:
    slow = slow.next
    mid -= 1
  return slow
```

### Middle of the LinkedList

Given the head of a **Singly LinkedList**, write a method to return the **middle node** of the LinkedList.

If the total number of nodes in the LinkedList is even, return the second middle node.

One brute force strategy could be to first count the number of nodes in the LinkedList and then find the middle node in the second iteration. Can we do this in one iteration?

We can use the **Fast & Slow pointers** method such that the fast pointer is always twice the nodes ahead of the slow pointer. This way, when the fast pointer reaches the end of the LinkedList, the slow pointer will be pointing at the middle node.

```python
def find_middle_of_linked_list(head):
  # TODO: Write your code here
  slow, fast =head, head
  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
  return slow
```

When question ask for **constant space** and **O(N)**, think about **fast & slow pointers**

Anything about **middle, we can think about fast & slow pointers, some variation could be LinkedList palindrome (split by middle)**
