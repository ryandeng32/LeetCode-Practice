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
