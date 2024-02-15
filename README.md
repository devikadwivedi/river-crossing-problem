# river-crossing-problem

## River Crossing Problem

The River Crossing problem is a classic toy problem in the field of artificial intelligence. It is a river crossing puzzle where the goal is to transport three missionaries and three cannibals from one side of a river to the other using a boat. The catch is that the boat can only carry a maximum of two passengers at a time, and at no point should there be more cannibals than missionaries on either side of the river, otherwise the cannibals would eat the missionaries.

### Problem Statement

Given an initial state where all three missionaries and three cannibals are on the left side of the river, and an empty boat, the task is to find a sequence of boat crossings that will safely transport all missionaries and cannibals to the right side of the river.

### Solution with DFS/BFS

The problem can be solved using Depth-First Search (DFS) or Breadth-First Search (BFS) algorithms. These algorithms explore all possible states of the problem space, gradually moving towards the goal state.

- **DFS (Depth-First Search):** This algorithm explores the deepest branches of the state space tree first. It uses a stack data structure to keep track of states to be explored.

- **BFS (Breadth-First Search):** Unlike DFS, BFS explores all the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level. It uses a queue data structure to keep track of states to be explored.

### Implementation

The provided Python code implements the DFS approach to solve the Missionaries and Cannibals problem. It defines functions to generate successor states, check for legality of states, check for the goal state, and conduct DFS search to find the solution path.

```python

# Python code for solving the problem using DFS
# Define start state, path, and visited list
start = (3, 3, 'L')
path = []
visited = []

# DFS function and other supporting functions are defined here

# Initial DFS call to find solution path
dfs(start, path, visited)
```

The solution is printed once it is found, showing the sequence of states from the initial state to the goal state. Additionally, the code outputs statistics such as the total number of states checked, repeated states, and illegal states encountered during the search.

### Running the Code

To run the provided code, simply execute the Python script. Ensure that you have Python installed on your system. The code will output the solution path along with statistics regarding the search process.

---

### Sensitivity of Terminology

While the Missionaries and Cannibals problem is a well-known puzzle in artificial intelligence and computer science, it's important to recognize the potentially insensitive nature of its name. The term "cannibals" carries historical baggage, often invoking stereotypes and colonial narratives that may be offensive or inappropriate. As we strive for inclusivity and cultural sensitivity, it's advisable to use more neutral or descriptive language when discussing this problem. Referring to it as the "MCC problem" or "River Crossing Puzzle" helps to avoid perpetuating harmful stereotypes and acknowledges the need for respectful dialogue in all aspects of problem-solving and education.

--- 
