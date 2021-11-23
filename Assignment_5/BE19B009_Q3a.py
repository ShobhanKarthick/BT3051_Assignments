import numpy as np 
import matplotlib.pyplot as plt
from numpy import random
import networkx as nx

def get_leaders(G):
    return sorted(G.nodes, key = G.degree, reverse=True)[:6]

SocialGraph = nx.barabasi_albert_graph(60, 2, 42)
Leaders = get_leaders(SocialGraph)
print(Leaders)

# You are given SocialGraph which reflects the social network of the 60 participants.
# Six chosen leaders are given to you as a list using variable called 'Leaders'

# Add any functions required

def Form_Teams(G, Leaders):
    """ Form six teams each consisting of 10 individuals """
    teams = {i:[0 for i in range(10)] for i in Leaders}
    nodes = list(G.nodes)           # Get all the nodes

    for i in Leaders:
        teams[i][0] = i             # Add leaders to teams
        nodes.remove(i)             # Remove leaders from non-team members list

    leaders = Leaders.copy()
    for j in range(len(leaders)):
        i = random.choice(leaders,1)[0]         # Randomly choose the leader
        leaders.remove(i)                       # Remove the leader from the leader list
        neighbors = list(G.neighbors(i))            # Get neighbors

        for j in range(1, 9):               # Add other 9 members
            if len(neighbors) != 0:
                member = random.choice(neighbors, 1, replace=False)[0]      
                if member in nodes:                     # Check if members is there in non-team member list
                    teams[i][j] = member
                    neighbors.remove(member)
                    nodes.remove(member)
        
        teams[i] = sorted(teams[i])         # Sort the team array for adding other members easily

        if i == 0:                                      # For leader 0, number of 0s in the list will be 1 extra
            for k in range(teams[i].count(0) - 1):
                if len(nodes) != 0:
                    member = random.choice(nodes, 1)[0]
                    teams[i][k] = member
                    nodes.remove(member)
        else:
            for k in range(teams[i].count(0)):          # For other leaders, number of 0s = vacant positions for members
                if len(nodes) != 0:
                    member = random.choice(nodes, 1)[0]
                    teams[i][k] = member
                    nodes.remove(member)
            
    return teams


def Tug_of_war(Teams):
    """ Tug of war round. Each team has equal chance of winning. Returns three winning teams."""
    """ Add your code here """
    
    all_leaders = list(Teams.keys())
    Winning_Teams = []

    for i in range(3):
        playing_teams = random.choice(all_leaders, 2, replace=False)
        Winning_Teams.append(random.choice(playing_teams, 1)[0])
        for leader in playing_teams:
            all_leaders.remove(leader)

    return Winning_Teams


def simulate(G, Leaders):
    """ Simulate the scenario multiple times """
    probabilities_of_winning = {i:0.2 for i in G.nodes}
    """ Modify the code as required """

    for i in range(10000):
        Teams = Form_Teams(G,Leaders)
        Winners = Tug_of_war(Teams)
        print(i)

    return probabilities_of_winning

simulate(SocialGraph,Leaders)
