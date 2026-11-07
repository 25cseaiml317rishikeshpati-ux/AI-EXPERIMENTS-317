# Experiment 10: Travelling Salesman Problem (TSP)

from itertools import permutations

# Number of cities
n = int(input("Enter number of cities: "))

# Taking cost matrix as input
graph = []

print("Enter the cost matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

# Taking starting city
start = int(input("Enter starting city (0 to {}): ".format(n-1)))

# Create list of all cities
cities = list(range(n))

# Remove starting city
cities.remove(start)

# Initialize minimum cost
min_cost = float('inf')
best_path = []

# Generate all possible routes
for route in permutations(cities):

    # Create complete path
    path = [start] + list(route) + [start]

    # Calculate total travelling cost
    cost = 0

    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i+1]]

    # Check for minimum cost
    if cost < min_cost:
        min_cost = cost
        best_path = path

# Display the result
print("\nOptimal Route:")

for city in best_path:
    print(city, end=" ")

print("\nMinimum Travelling Cost:", min_cost)


# Sample Input :
Enter number of cities: 4
Enter the cost matrix:
0 10 15 20
10 0 35 25
15 35 0 30
20 25 30 0
Enter starting city (0 to 3): 0

# OUTPUT :

Optimal Route:
0 1 3 2 0 
Minimum Travelling Cost: 80


