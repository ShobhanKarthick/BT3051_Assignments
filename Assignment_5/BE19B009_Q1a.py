import networkx as nx
import matplotlib.pyplot as plt
# Use of any function from networkx.algorithms module is strictly not allowed.
# Other libraries are not allowed expect for matplotlib for visualization purposes

# Add your functions here if needed

def minimum_time_for_spread_of_contagion(G, patient_zero):
    """
    Given an connected undirected weighted networkx graph which represents the physical contant graph of a community and a node which represents patient zero of the contagion, return the minimum time taken for the contagion to spread in the complete graph.
    """
    nodes = {node: i for i, node in enumerate(G.nodes)}     # Form a dictionary with {node: i-th position}
    dist = [[float('inf') for i in range(len(nodes))] for j in range(len(nodes))]     # Initialise the distance array

    edges = list(G.edges(data = "weight"))          # Get the edges with their weights

    for edge in edges:                                      # Iterate through the edges
        dist[nodes[edge[0]]][nodes[edge[1]]] = edge[2]      # Create the matrix with weights in place
        dist[nodes[edge[1]]][nodes[edge[0]]] = edge[2]

    for node in nodes:
        dist[nodes[node]][nodes[node]] = 0              # Self loops have 0 weight

    # Floyd-Warshall algorithm
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[nodes[i]][nodes[j]] > (dist[nodes[i]][nodes[k]] + dist[nodes[k]][nodes[j]]):
                    dist[nodes[i]][nodes[j]] = dist[nodes[i]][nodes[k]] + dist[nodes[k]][nodes[j]]

    max_dist = dist[0][0]
    for i in range(len(dist)):
        if(max_dist < dist[nodes[patient_zero]][i]):       
            max_dist = dist[nodes[patient_zero]][i]             # Find the time taken for spreading from patient_zero

    return max_dist

G = nx.Graph()
G.add_edge(1,2,weight = 2); G.add_edge(3,2,weight = 3); G.add_edge(3,1,weight = 2)
G.add_edge(3,4,weight = 1); G.add_edge(4,5,weight =3); G.add_edge(5,6,weight =4)
G.add_edge(7,6,weight =7); G.add_edge(5,8,weight =2); G.add_edge(7,8,weight =6)

print(minimum_time_for_spread_of_contagion(G, 3))


# Expected output: 12
# Explanation: 
# Infected node | Time taken to reach that node
#      3        |  0
#      4        |  1
#      1        |  2
#      2        |  3
#      5        |  4 (1+3)
#      8        |  6 (1+3+2)
#      7        |  12(1+3+2+6)

# Hint:
# Therefore, minimum time taken to spread in the community = argmax_i(min(time taken to reach node i from patient zero node))
# Mininum time taken to reach node i from patient zero node can be thought of as a dynamic programming question. 
# Time taken to reach node i from node j can be thought of as a dynamic programming question. 
# To find the shortest path/minimum time taken for the person to be infected you can either use Dijkstra's algorithm or a dynamic programming variant of Dijkstra's algorithm i.e. Floyd-Warshall algorithm for all pairs of shortest paths

"""Pseudocode for Floyd-Warshall algorithm
let dist be a |V| × |V| array of minimum distances initialized to ∞ (infinity)
for each edge (u, v) do
    dist[u][v] ← w(u, v)  // The weight of the edge (u, v)
for each vertex v do
    dist[v][v] ← 0
for k from 1 to |V|
    for i from 1 to |V|
        for j from 1 to |V|
            if dist[i][j] > dist[i][k] + dist[k][j] 
                dist[i][j] ← dist[i][k] + dist[k][j]
            end if
"""
