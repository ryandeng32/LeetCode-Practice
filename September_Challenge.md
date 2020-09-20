## Techniques 

> self-balancing BST 

> Buckets

## Day2: 220.Contains Duplicate III 

* Before doing anything, try to take care of error cases such as when arr is empty or absolute value is negative
* Think about the naive approach, and try to simplify the bottleneck
* **Technique** By inserting element in a **self-balancing BST**, it's sorted for fast search 
* **Technique**: Use **bucket** to achieve linear time complexity. This is also a great way to maintain a sliding window that's easy to search 
* **Buckets and BST** are great when we want to keep a sorted array whenever we insert something 

## Day5: 1305. All Element in Two Binary Search Trees 

* Binary Search Tree & Ascending -> **Think about in-order traversal** 

## Day7: 290. Word Pattern 

* To have O(1) look up time, we can use a hashmap or a hashset

## Day8: 1022: Sum of Root to Leaf Binary Numbers 

* Root-to-leaf traversal -> DFS preorder traversal 
* We can do preorder traversal: **iteratively** and **recursively**

## Day9: 165. Compare Version Numbers

* When the input string is separated with a special character, in this case `.`, then we can use **split and parse** method 
* Add 0s to the end so both arrays are at the same length 

## Day 11: 152. Maximum Product Subarray

* Since it's a subarray problem, I might think about using **sliding window** first. However, since there exists negative number, the value of the window is unstable, so consider using **dynamic programming** 

## Week 2 Premium: 346. Moving Average from Data Stream 

* Using a list to keep track of all the numbers is an obvious solution
* However, since we only need to pop the start and append the end, we can use the **double-ended queue** 
* Think about optimized DS. 

## Day 14: 198. House Robber 

* classic DP problem
* It's hard to think about all the cases, so start simple and work on the simplest case first 

## Day 19: Sequential numbers

* Sliding window technique fits this problem well 
