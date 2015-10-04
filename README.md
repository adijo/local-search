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

* **Simulated annealing:** Simulated annealing is a technique in which potentially bad moves are allowed early on in the search process with a certain probability, but this probability goes on reducing as the search progresses. The probability is a function of a parameter called temperature `T`, which is borrowed from the process of annealing from metallurgy. The basic algorithm is described as follows:
  * Pick a start state `s_0`
  * Initialize a temperature `T` to a high value.
  * Have an energy function `eval` that maps a given state to an energy value. In our case, this is the same heursitic function that returns how many pairs of queens are potentially in an attacking position.
  * Pick a random "neighbouring" state. 
  * If the energy value of this neighbouring state is lower than the current energy value, change the current state to the new state.
  * If it is not, choose the neighbouring state with a probability depending upon `T`. Higher the value of `T`, higher the probability.
Some stats after implementing these two techniques:

* Hill climbing:

  * **Cost (one run): 4.** 
  * ![](https://github.com/adijo/local-search/blob/master/images/hill_climbing.png)
  * **Average cost (100 runs): 3.10.**
  
* Hill climbing with random restart:

  * **Cost (one run): 1.**
  * ![](https://github.com/adijo/local-search/blob/master/images/hill_climbing_rr.png)
  * **Average cost (100 runs): 1.37.**

* Simulated annealing:
  * **Cost (one run, 1000 iteration): 2**
  * ![](https://github.com/adijo/local-search/blob/master/images/simulated_annealing.png)



