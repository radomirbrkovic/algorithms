# Interpolation Search

**The Interpolation Search** is an improvement over Binary Search for instances, where the values in a sorted array are uniformly distributed. Binary Search always goes to the middle element to check. On the other hand, interpolation search may go to different locations according to the value of the key being searched.

If elements in given list are unevenly distributed, the execution time will be  **O(N)**, in other side the execution time will be **O(log(logN))**.