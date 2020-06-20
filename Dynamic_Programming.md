* Notes from www.dynamicprogrammingbook.com
## Goals
* Have a system to solve every problem in DP
* Understand that all DP problems are very similar 

## Overview
* DP is the technique of **storing repeated comuptations in memory, rather than recomputing them every time you need them."
* DP allows you to **use more space to improve runtime**
* DP questions should have the following two characteristics: 
  * **Optimal substructure**
  * **Overlapping subproblems**
  
### Optimal Substructure
* Optimal substructure requires that **you can solve the problem based on the solutions of subproblems.**
* Eg. fib(5) = fib(4) + fib(3)
* Think whether a problem **can be easily solved recursively** 

### Overlapping Subproblems:
* When you split into subproblems, you sometimes get **duplicated subproblem.** 
* DP uses memory to **save values that have already been computed to avoid computing them again**

## Key Terms: 
* **Memoization**: the technique of writing a function that remembers the results of previous computations
  * This can be done by using a data structure like an array or HashMap 
* **Top-down and bottom-up**: Two general approaches to DP. 
  **Top-down**: Starts with the final results and recursively breaks it down into subproblems. **Recursive**
  **bottom-up**: Iteratively solve the subproblems first and then works up to the desired solution. **Iterative** 
  * Both methods are equally valid. 

## FAST Method
* **F**irst Soluton
* **A**nalyze the first solution
* Identify the **S**ubproblems
* **T**urn the solution around

### First Solution 
* Find the **brute force and recursive** solution 
* Solve the problem without concern for efficiency 
* Must meet these restrictions
 * The recursive calls must be **self-contained**, no global variables. 
 * Cannot do tail recursion. Solution should compute the results of each subproblems and then combine them afterwards 
 * Do not pass in unnecessary variables. 
 
### Analyze the First Solution
* Determine the time and space complexity and ask whether there is obvious room for improvement. 
* Ask if the problem fits the rules in DP
 * Does it have an optimal substructure? 
 * Are there overlapping subproblems? 
 
### Find the Subproblems
* Discover the high-level meaning of the subproblems. Our recursive solution can be made dynamic by caching the values, this is a top-down solution. 

### Turn the solution around
* Maybe flip it around and get a bottom-up solution instead. Write a function that will iteratively compute the results of successive subproblems, until our desired result is reached. 
*

## Examples
### Fibonacci Numbers
* First solution (Recursive & Brute Force) 
```python
  def fib(n): 
    if n == 0: 
      return 0
    if n == 1: 
      return 1
    return fib(n-1) + fib(n-2)
```
* Analysis
 * Terrible runtime O(2^n)
 * Have a bunch of duplicated functions calls 
* Find the Subproblems
```python
  def fib(n): 
    if (n < 2): 
      return n
    cache = [-1 for i in range(n+1)] 
    cache[0] = 0
    cache[1] = 1
    return fib_helper(n, cache)
  def fib_helper(n, cache): 
    if (cache[n] >= 0) return cache[n]
    cache[n] = fib_helper(n-1, cache) + fib_helper(n-2, cache) 
    return cache[n]
```
