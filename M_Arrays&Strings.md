## All Techniques
> Two pointers （in-place) 

> Reverse with two pointers 

> Double reverse 

## Question Type
> 2 Sum 

> Reverse

> Palindrome 

## 344. Reverse String ***** This method can be used for any array reverse ***** 

**What's an in-place algorithm?** An algorithm which transforms input using **no auxiliary data structure** 

Note: Recursion doesn't use auxiliary DS, so we can use recursion to solve in-place problem. **In-place therefore does not necessarily mean constant space complexity.** 

Solved with **Two Pointers Approach** 

## 75. Sort Colors (Dutch National Flag Problem)

Solution: 

- Use three pointers to track the rightmost boundary of zeros, the leftmost boundary of twos and the current element under the consideration
- It's a **generalization of the 2 pointers technique**

## 151. Reverse Words in a String 
**Question**: To use or not use built-in methods like **reverse()** 

**Answer**: There is no universal answer, so be prepared to do both 

**Approach 1**: Use built-in methods split and reverse. **It's in-place, but linear space complexity**

**Approach 2**: Reverse the whole string and then reverse each word 
* Since python has immutable strings, one has to first **convert string into mutable data structure**
* Trim trailing and leading spaces with **two pointers** technique. **Think about using this when there is a need to approach both side of a list** 
* **Reverse the entire string, and then reverse each word** 

## 8. String to Integer (atoi) 

* **Technique**: 
1. discard leading spaces
```Python
  while (i < len(str) and str[i] == " "): 
    i += 1
```
2. Turn "8" into 8"
```Python 
  "8" - "0"
```
