* Notes from watching Day by Day SWE
## BigO
* **The Question**: How does **algorithm speed** scale when input scales becoming **very large**?
* Don't care about the constant, we care about the behaviour
* Big Mistake: O(n)
  * What is n? 
    -> String Length? 
    -> Tree Node? 
    -> Array Size? 
    **Depends on the input and the question**
* Common time complexity
  * **O(1) "Constant Time"**:
    * Runtime of the runtime does not change
  * **O(Log(n)) "Logorithmic Time"**: 
    * Normally log base 2. **But doesn't really matter**
    * Example: Binary Search
  * **O(n) "Linear Time"**: 
    * Touching all elements
  * **O(nlog(n))**: 
    * Merge Sort & Quick Sort
      * Have log(n) levels and do linear work for each level
  * **O(n^2) "n-squared"**: 
     * Naive Solution
     * Naive Sorting Algorithms: Bubble sort, selection sort, insertion sort...
  * **O(2^n) "Expontential Time"
      * Backtracking problems
  * **O(n!) "n-factorial"**: 
      * usually seen in permutations
      
* How to optimize a solution: 
  * Better Time complexity, more space
  * Less space, worse time complexity
  * **We can buy more memory but we can't buy time**, so we would **prefer better time complexity**

### Space Complexity
* Question: How does the space usage scale as input gets very large
* What auxiliary space do you make? Is it in-place? 
* Runtime Stack space counts unless told otherwise. 

### Final
* Do not memorize "Code Shape", DO NOT GUESS
* Knowing hints you to the best solution
  * If you know the time complexity is log(n) and array is sorted, you think of binary search
* Can't guess in an interview
