import networkx as nx
# Use of any function from networkx.algorithms module is strictly not allowed.
# Other libraries are not allowed expect for matplotlib for visualization purposes

# Add your functions here if needed
# You are allowed to use the function that you used in the previous subquestion

def minimum_time_for_spread_of_contagion(G):
    """
    Given an connected undirected weighted networkx graph which represents the physical contant graph of a community and a node which represents patient zero of the contagion, return the minimum time taken for the contagion to spread in the complete graph.
    """
    nodes = {node: i for i, node in enumerate(G.nodes)}         # Form a dictionary with {node: i-th position}
    dist = [[float('inf') for i in range(len(nodes))] for j in range(len(nodes))]   # Initialise the distance array

    edges = list(G.edges(data = "weight"))      # Get the edges with their weights

    for edge in edges:                                      # Iterate through the edges
        dist[nodes[edge[0]]][nodes[edge[1]]] = edge[2]      # Create the matrix with weights in place
        dist[nodes[edge[1]]][nodes[edge[0]]] = edge[2]

    for node in nodes:                                  
        dist[nodes[node]][nodes[node]] = 0          # Self loops have 0 weight

    # Floyd-Warshall algorithm
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[nodes[i]][nodes[j]] > (dist[nodes[i]][nodes[k]] + dist[nodes[k]][nodes[j]]):
                    dist[nodes[i]][nodes[j]] = dist[nodes[i]][nodes[k]] + dist[nodes[k]][nodes[j]]

    min_time = [dist[0][0]]*len(nodes)
    for i in nodes.keys():                              # Iterate through patient nodes
        for j in range(len(dist)):
            if(min_time[nodes[i]] < dist[nodes[i]][j]):       
                min_time[nodes[i]] = dist[nodes[i]][j]          # Find the time taken for spreading for all patients

    return nodes, min_time



def most_critical_node_for_contagion(G):
    """
    Given an connected undirected weighted networkx graph which represents the physical contant graph of a community, return the most critical node. The infection of the most critical node will result in minimum time for the spread in the whole community.
    """
    nodes, min_time_array = minimum_time_for_spread_of_contagion(G)
    min_time =  min_time_array.index(min(min_time_array))       # Get the min_time for all patients
    crtical_node = 0

    for i in nodes.keys():
        if nodes[i] == min_time:        # Get the node which has the min_time from patients nodes dictionary
            crtical_node = i

    return crtical_node

G = nx.Graph()
G.add_edge(1,2,weight = 2); G.add_edge(3,2,weight = 3); G.add_edge(3,1,weight = 2)
G.add_edge(3,4,weight = 1); G.add_edge(4,5,weight =3); G.add_edge(5,6,weight =4)
G.add_edge(7,6,weight =7); G.add_edge(5,8,weight =2); G.add_edge(7,8,weight =6)

print(most_critical_node_for_contagion(G))
# Expected output: 5
# Explanation: 
# Patient zero node | minimum time taken
#      1            |  15
#      2            |  16
#      3            |  12
#      4            |  11
#      5            |  8 - minimum time
#      6            |  12
#      7            |  15
