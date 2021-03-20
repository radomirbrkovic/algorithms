# Quick sort | [Source](https://www.geeksforgeeks.org/quick-sort/)

Like as **Merge Sort** algorithm, **quick sort** belongs to *Divide and Conquer* group of algorithms. It picks an element as pivot and partitions the given list around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.

 1. Always pick the first element as pivot
 2. Always pick the last element as pivot (implemented in example)
 3. Pick a random element as pivot
 4. Pick median as pivot

The key process in quickSort is `partition()`. Target of partition is, given an `array` and an element `x` of `array` as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.   

![Quick sort](https://www.geeksforgeeks.org/wp-content/uploads/gq/2014/01/QuickSort2.png "Quick sort")

### Partition Algorithm 

There can be many ways to do partition, following pseudo code adopts the method given in CLRS book. The logic is simple, we start from the leftmost element and keep track of index of smaller (or equal to) elements as i. While traversing, if we find a smaller element, we swap current element with arr[i]. Otherwise we ignore current element. 

### Quick sort pseudo code
```
/* low  --> Starting index,  high  --> Ending index */
quickSort(arr[], low, high)
{
    if (low < high)
    {
        /* pi is partitioning index, arr[pi] is now
           at right place */
        pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);  // Before pi
        quickSort(arr, pi + 1, high); // After pi
    }
}
```

### Pseudo code for partition() 
```
/* This function takes last element as pivot, places
   the pivot element at its correct position in sorted
    array, and places all smaller (smaller than pivot)
   to left of pivot and all greater elements to right
   of pivot */
partition (arr[], low, high)
{
    // pivot (Element to be placed at right position)
    pivot = arr[high];  
 
    i = (low - 1)  // Index of smaller element and indicates the 
                   // right position of pivot found so far

    for (j = low; j <= high- 1; j++)
    {
        // If current element is smaller than the pivot
        if (arr[j] < pivot)
        {
            i++;    // increment index of smaller element
            swap arr[i] and arr[j]
        }
    }
    swap arr[i + 1] and arr[high])
    return (i + 1)
}
```