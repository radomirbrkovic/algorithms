# Dynamic programming 

**Dynamic programming** represents mathematical and computer programing optimization methods, which was developed by [Richard Bellman](https://en.wikipedia.org/wiki/Richard_E._Bellman) in the 1950s and has found applications in numerous fields, from aerospace engineering to economics. 

In both contexts it refers to simplifying a complicated problems by breaking it down into simpler sub-problems in a recursive manner. While some decision problems cannot be taken apart this way, decisions that span several points in time do often break apart recursively. Likewise, in computer science, if a problem can be solved optimally by breaking in into sub-problems the recursively finding the optimal solutions to the sub-problems then it said to have *optimal substructure*.

If sub-problems can be nested recursively inside lager problems, so that dynamic methods are applicable, then there is a relation between the value of the larger problem and rhe values of the sub-problems. In the optimization literature this relationship os called the **Bellman equation**

There are two key attributes that a problem must have in order for dynamic programming to be applicable:
 1. Optimal structure property 
 2. Overlapping sub-problems

 ## Optimal substructure property

 Any problem has optimal substructure property if its overall optimal solution can be constructed from the optimal solutions of its sub-problems. For Fibonacci numbers as we know:
 ```
 Fib(n) = Fib(n-1) + Fib(n-2)
 ```
 This clearly shows that the a problem of size `n` has been reduced to sub-problems fo size `n-1` and `n-2`. Therefore, FIbonacci have optimal substructure property.   

## Overlapping sub-problems

Sub-problems are smaller version of the original problem. Any problem has overlapping sub-problems if has a solution which involves solving the same sub-problem multiple times. Take the example of the Fibonacci numbers.For finding value the `fib(4)`, we need to break it down into the following sub-problems:

![Fibonacci solution](https://i.stack.imgur.com/CLwKE.jpg "Fibonacci solution")  

We can clearly see the overlapping subproblem pattern here, as `fib(2)` has been evaluated twice and `fib(1)` has been evaluated three times.
