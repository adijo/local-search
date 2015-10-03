# Local search

Implementation of various local search algorithms to solve hard combinatorial problems 
such as the famous n-queens problem.

# Current Implementations

* **Hill climbing:** Hill climbing is a technique that involves making iterative improvements to the current available
solution. In the context of the n-queens problem, we associate a **cost** to a given state of the n-queens board.
This **cost** is the number of pairs of queens that can currently attack each other. Our goal is to reduce this cost 
to 0. Hill climbing as a distinct disadvantage of being caught in a local minima and never reaching the global minima.

* **Hill climbing with random restart:** Often times, it is benefitial to randomly reset your state to avoid getting 
stuck in local minimas. This is exactly what the random restart feature facilitates. 

Some stats after implementing these two techniques:

* Hill climbing:

  * **Cost (one run): 4.** 
  * ![](https://github.com/adijo/local-search/blob/master/images/hill_climbing.png)
  * **Average cost (100 runs): 3.10.**
  
* Hill climbing with random restart:

  * **Cost (one run): 1.**
  * ![](https://github.com/adijo/local-search/blob/master/images/hill_climbing_rr.png)
  * **Average cost (100 runs): 1.37.**
  



