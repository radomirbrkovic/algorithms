# Jump Search [Source](https://www.geeksforgeeks.org/jump-search/)

Like *Binary search*, Jump search is algorithm for sorted list of elements. The basic idea is to check fewer elements (than linear search) by jumping ahead by fixed steps or skipping some elements in place of searching all elements.  

For example, suppose we have an array `arr[]` of size `n` and block (to be jumped) size `m`. Then we search at the indexes `arr[0], arr[m], arr[2m]…..arr[km]` and so on. Once we find the interval `(arr[km] < x < arr[(k+1)m])`, we perform a linear search operation from the index `km` to find the element `x`.

### What is the optimal block size to be skipped?

In the worst case, we have to do `n/m` jumps and if the last checked value is greater than the element to be searched for, we perform `m-1` comparisons more for linear search. Therefore the total number of comparisons in the worst case will be `((n/m) + m-1)`. The value of the function `((n/m) + m-1)` will be minimum when `m = √n`. Therefore, the best step size is `m = √n`.