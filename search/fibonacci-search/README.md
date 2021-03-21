# Fibonacci Search

**Fibonacci search** belongs to a *divide and conquer* type of algorithms like as **binary search** but it narrows down possible locations with the aid of *Fibonacci numbers*.  Compared to *binary search* where the sorted list of elements is divided into two equal-sized parts, one of which is examined further, Fibonacci search divides the array into tow parts that have sizes that are consecutive Fibonacci numbers. On average, this lead to about 4% more comparisons to be executed, but it has the advantage that one only needs addition and subtraction to calculate the indices of the accessed array elements, while classical binary search needs bit-shift, division or multiplication, operations that were less common at the time Fibonacci search was first published. Fibonacci search has an average- and worst-case complexity of O(log n),  

### Similarities with Binary Search:  
1. Works for sorted arrays
2. A Divide and Conquer Algorithm.
3. Has Log n time complexity.

### Differences with Binary Search: 
1. Fibonacci Search divides given array into unequal parts
2.  Binary Search uses a division operator to divide range. Fibonacci Search doesn’t use /, but uses + and -. The division operator may be costly on some CPUs
3. Fibonacci Search examines relatively closer elements in subsequent steps. So when the input array is big that cannot fit in CPU cache or even in RAM, Fibonacci Search can be useful.