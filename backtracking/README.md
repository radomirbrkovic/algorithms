# Backtracking Algorithms | [Source](https://www.geeksforgeeks.org/backtracking-algorithms)

**Backtracking** in an algorithmic-technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constrains of the problem at any point of time (by time, here, is referred to the time elapsed till reaching any level of the search tree).

For example, consider the SudoKo solving problem, we try filling digits one by one. Whenever we find that current digit cannot lead to a solution, we remove it (backtrack) and try next digit. This is better than naive approach (generating all possible combinations of digits and then trying every combination one by one) as it drops a set of permutations whenever it backtracks.

![Sudoku](https://media.geeksforgeeks.org/wp-content/uploads/sudoku.jpg)