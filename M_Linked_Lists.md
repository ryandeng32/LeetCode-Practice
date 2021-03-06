## Techniques 
> Dummy node 
> Stack, Recursion 

## 206. Reverse Linked List

* Think about how to do this both **iteratively** and **recursively**
* To think about the recursive solution, **assume that the rest of the list had already been reversed, and then see how to reverse the front part**
* Understand the space complexity for using recusion. O(n) means **the recursion could go up to n levels deep**

## 2. Add Two Numbers 

* **technique** Use a dummy node to construct new linked list
```Python
  dummyHead = new ListNode(0)
  # operation...
  return dummyHead.next
```
## 445. Add Two Numbers II 

* **technique**: when two linked lists are different length, can we fill the shorter one until they are the same length? 
* How can we traverse a singly linked list backward without reversing it? We can either do 
  * Recursion
  * Use stack (stack.pop() will remove the last element) 
  
