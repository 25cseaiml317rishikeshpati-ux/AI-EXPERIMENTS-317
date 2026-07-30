def dfs(graph, start_node):
    visited = []
    stack = [start_node]

    while stack:
        current_node = stack.pop()

        if current_node not in visited:
            print(f"Exploring node: {current_node}")
            visited.append(current_node)

            # Add unvisited neighbors to the stack
            for neighbor in graph.get(current_node, []):
                if neighbor not in visited and neighbor not in stack:
                    stack.append(neighbor)

    return visited


# ---------------- BUILD YOUR GRAPH ----------------
print("------ BUILD YOUR GRAPH ------")

student_graph = {}

# Get the total number of edges
num_edges = int(input("How many edges (connections) does your graph have? "))
print("Enter each edge separated by a space (e.g., A B):")
for i in range(num_edges):
    u, v = input(f"Edge {i + 1}: ").split()

    # Initialize adjacency lists if needed
    if u not in student_graph:
        student_graph[u] = []
    if v not in student_graph:
        student_graph[v] = []

    # Undirected graph
    student_graph[u].append(v)
    student_graph[v].append(u)

# Get the starting node
start = input("Enter the starting node for DFS: ")

print("\nYour Graph Dictionary:", student_graph)
print("Starting DFS Traversal...\n")

result = dfs(student_graph, start)

print("\nDFS Traversal Order:", result)
