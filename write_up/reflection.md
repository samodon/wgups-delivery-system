# Reflection

## Strengths of The Algorithm

** 1. Efficient **:
The algorithm is efficient in optimizing the route while finding the closet next delivery point. Therefore, it could handle scenarios where the number of delivery points fluctuates.

** 2 Simple **:

Considering the algorithm simply finds the closest delivery point by calculating the distance between the current delivery point, and the rest of the delivery points, it is simple to understand and implement. This makes it easy to modify and maintain.

** 3. Hash Table Optimization **:

The custom hash table, in conjunction with the nearest neighbor algorithm, Allows for a data structure that can be optimized for this specific use case, allowing for more efficient data retrieval and storage.

## Validation

The major requirements of the algorithm are as follows:

** 1. Ensure packages deliver on time **:

The algorithm ensures that the packages are delivered on time by optimizing the route to find the closet next delivery point. The screenshots provide the delivery time for each package.

** 2. The distance traveled should not exceed 140 miles **:

The distances traveled for each trucks are as follows:

- Truck 1 : 28.40 miles
- Truck 2 : 44.00 miles
- Truck 3 : 44.60 miles

Thus, the total distance traveled by all trucks is 117.00 miles.

## Other Possible Algorithms

** 1. Dijkstra's Algorithm **:

Dijkstra's algorithm is another algorithm that could meet the above requirements. It works by finding the shortest path between nodes in a graph. Using this to solve find the shortest path between delivery points could be a viable alternative.

** 2. A \* Algorithm **:

A \* algorithm could also be used to find the shortest path between delivery points. It is similar to the Dijkstra's algorithm in that they are used for finding the shortest nodes between a graph. However, A \* algorithm uses cost( the distance in this context) of going from one node to the goal.

### Differences between Nearest Neighbor and the other algorithms.

** 1. A \* Algorithm **:

- The A \* uses the both the actual cost of the travel, and an estimate of the cost to that it would be to find the most efficient route. This is different from the nearest neighbor algorithm only using the actual cost of the travel.

** 2. Dijkstra's Algorithm **:

- Dijkstra's algorithm uses the total cost from the start node for all other nodes. This is different from the nearest neighbor algorithm, which only uses the cost of the travel from the point to the next point.

## What would I do differently?

1. I would implement a more dynamic algorithm that could handle more complex requirements such as the time windows for delivery, the capacity of trucks, the number of available drivers and trucks, and dynamically account for delays in delivery based off the conditions in 'Package_File'. These modifications would include the use of a more complex data structure, and the by handling the delivery changes at the time of delivery in the delivery method.

2. I would implement a GUI that would allow for a more user friendly interface, showing the packages as they are being updated and delivered at the time of delivery. I would implement this by using TKinter, a python library for creating GUIS.

## Alternative Data Structures.

** 1. B Tree **:

- A B Tree has a self- balancing tree structure. In this structure, nodes can have multiple children. Whenever a node has too many keys it is split into two nodes. This would be useful for this algorithm as it would allow for a more efficient way to store and retrieve data.

** 2. AVL Tree **:

- This is also a self-balancing binary search tree, but it is more rigid. It works by maintain a factor that dictates the balance of the tree. This could be useful because memory intensive operations could be improved.

### Differences between Hash Table

** 1. B Tree **:

- A B tree is a balanced tree structure optimizes by splitting nodes when they have too many keys.The time complexity is $O(log n)$ for searching and insertion. This is different from a hash table, which uses a hash function for optimization when there are collisions and has a time complexity of $O(1)$ for searching and insertion.

** 2. AVL Tree **:

- An AVL tree balances itself by maintaining a balance factor.It has a time complexity of $O(log n)$.Hash tables use hashing methods for searching, insertion and deletion, with a complexity of $O(1)$.

## Sources

[Introduction of B-Tree](https://www.geeksforgeeks.org/introduction-of-b-tree-2/)  
GeeksforGeeks. (2021). Introduction of B-Tree. [online]
[A Search Algorithm](https://www.geeksforgeeks.org/a-search-algorithm/)  
GeeksforGeeks. (2021). A\* Search Algorithm. [online]
[Introduction to AVL Tree](https://www.geeksforgeeks.org/introduction-to-avl-tree/)  
GeeksforGeeks. (2021). Introduction to AVL Tree. [online]
[Hashing Data Structure](https://www.geeksforgeeks.org/hashing-data-structure/)
