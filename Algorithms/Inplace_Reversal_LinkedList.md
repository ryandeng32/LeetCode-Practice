```python
def reverse_sub_list(head, p, q):
	if p == q:
		return head

	# after skipping 'p-1' nodes, current will point to 'p'th node
  current, previous = head, None
  i = 0
  while current is not None and i < p - 1:
    previous = current
    current = current.next
    i += 1

	# we are interested in three parts of the LinkedList, the part before index 'p',
  # the part between 'p' and 'q', and the part after index 'q'
  last_node_of_first_part = previous
  # after reversing the LinkedList 'current' will become the last node of the sub-list
  last_node_of_sub_list = current
  next = None  # will be used to temporarily store the next node

	i = 0
  # reverse nodes between 'p' and 'q'
  while current is not None and i < q - p + 1:
    next = current.next
    current.next = previous
    previous = current
    current = next
    i += 1

  # connect with the first part
  if last_node_of_first_part is not None:
    # 'previous' is now the first node of the sub-list
    last_node_of_first_part.next = previous
  # this means p == 1 i.e., we are changing the first node (head) of the LinkedList
  else:
    head = previous

  # connect with the last part
  last_node_of_sub_list.next = current
  return head

```

- Any other **reverse "k" contiguous elements of a given LinkedList** can be converted to this parent problem.
- Example: Reverse the first "k" elements of a given LinkedList is just **p = 1, q = k**
