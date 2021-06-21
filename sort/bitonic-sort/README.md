# Bitonic Sort

**Bitonic sort** is a comparison-based sorting algorithm that can be run in parallel. It focuses on converting a random sequence of numbers into a *bitonic sequence*, one that monotonically increases, then decreases. Rotations of a bitonic sequence are also bitonc.   
More specifically, bitonic sor can be modelled as a type of *sorting network*. The initial unsorted sequence enters through input pipes, where a series of comparators switch two entries to be in either increasing or decreasing order.

The algorithm, created by **Ken Batcher** in 1968, consists of two parts. First, the unsorted sequence is built into a bitonic sequence, then, the series is split multiple times into smaller sequences until the input is in sorted order.     

![Bitonic sort](https://www.cs.rutgers.edu/~venugopa/parallel_summer2012/Resources/sort_network.png "Bitonic sort")