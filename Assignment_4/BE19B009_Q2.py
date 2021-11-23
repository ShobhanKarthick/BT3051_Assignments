#!/usr/bin/python

import networkx as nx
import json
import matplotlib.pyplot as plt

def printCycle(stack, node):
    """
    Printing the cycle from the stack
    Pop until the node in the stack and 
    return the popped elements along with the node itself
    """
    finalCycle = []
    # finalCycle.append(stack.pop())

    # try:
    while stack[-1] != node:
        finalCycle.append(stack.pop())
    finalCycle.append(stack.pop())
    # except IndexError:
    #     pass

    for node in finalCycle:
        stack.append(node)

    return finalCycle

def getCycle(adj_list, stack, visited, outputcycle):
    for neighbor in adj_list[stack[-1]]:            # Get the neighbors from the adjacency_list
        if visited[neighbor] == 0:
             outputcycle.append(printCycle(stack, neighbor))  # Add the cycle to the output array
        elif visited[neighbor] == -1:       # Check if neighbors are unvisited
            stack.append(neighbor)          # Add to stack and change flag to 0
            visited[neighbor] = 0
            getCycle(adj_list, stack, visited, outputcycle)     # And repeat it by calling it recursively

    visited[stack[-1]] = 1          # Once all neighbors are processed change the flag to 1
    stack.pop()             # Hence, remove from stack


def construct_metabolic_graph(name_of_json_file):
    """
    Given the reaction dict, return the metabolic directed bi-partite networkx graph
    """
    file = open(name_of_json_file, "r")
    model = json.load(file)
    G = nx.DiGraph()

    for reaction in (model["reactions"]):
        G.add_node(reaction["id"], nodecolor="red")             # Add reaction nodes
        for metabolite in (reaction["metabolites"]):            # Get each metabolite
            coeff = reaction["metabolites"][metabolite]
            G.add_node(metabolite, nodecolor="blue")            # Add each metabolite for that reaction
            if coeff > 0:                                       # Add reaction edges by seeing if it is reactant of product
                G.add_edge(metabolite, reaction["id"])          
            else:
                G.add_edge(reaction["id"], metabolite)

    # Test data
    # G.add_edge(1, 2)
    # G.add_edge(2, 3)
    # G.add_edge(3, 4)
    # G.add_edge(4, 1)
    # G.add_edge(3, 5)
    # G.add_edge(5, 6)
    # G.add_edge(6, 7)
    # G.add_edge(3, "A")
    # G.add_edge("A", "B")
    # G.add_edge("B", "C")
    # G.add_edge("C", "A")

    return G

def Find_Cycles_In_Metabolic_Graph(Graph):
    """
    Given a bi-partite networkx graph, return the list of list of metabolites involved in the cycle i.
    """
    visited = {node: -1 for node in Graph.nodes}        # Initialize all nodes as unvisited
    outputcycle = []
    stack = []

    # Node flag = -1 if node Not Visted at all
    # Node flag = 0 if node is Visited and added to the stack
    # Node flag = 1 if node is done processing
    
    adj_list = dict(Graph.adjacency())      # Graph as an adjacency list

    for node in Graph.nodes:
        if visited[node] == -1:         # Check if node is not visited
            stack.append(node)          # Push it to the stack
            visited[node] = 0           # Make the node flag as 1 becuase node visited and added to stack
            getCycle(adj_list, stack, visited, outputcycle)     # Get the cycles 

    return outputcycle

# For the purpose of parsing, look under "metabolites" sub-section of "reaction" section. The stoichiometric coefficients will help you in determining if a metabolite is a reactant or a product.
G = construct_metabolic_graph("e_coli_core.json")
# Add code to visualized G below
colors = [node[1] for node in G.nodes(data="nodecolor")]
nx.draw(G, node_color=colors, with_labels=True)
plt.show()


cycles = Find_Cycles_In_Metabolic_Graph(G)
print(cycles)
print(len(cycles))
