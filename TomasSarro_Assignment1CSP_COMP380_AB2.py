#############################
#   Tomas Sarro, 300184539  #
#   October 30,    2023     #
#                           #
#   COMP-380-AB2            #
#   Assignment 1            #
#############################

# This program displays a graph of nodes depicting
# the states of the USA.
# An image of the graph is shown with all nodes colored
# grey; after entering a start and end node, the colors
# of the graph change into either red, blue, yellow, or
# green.
# The color output of the nodes in the graph follow the
# arc consistency algorithm; no two adjacent nodes have
# the same color.

import networkx as nx
from networkx import *
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

# Checks if the passed node shares the same value as each neighbour
def is_valid_color(graph, node, color, coloring):
    for neighbor in graph.neighbors(node):
        # Returns false if the current node and neighbour node
        # are the same color.
        if neighbor in coloring and coloring[neighbor] == color:
            return False
    return True

# Assigns colors to each node in the graph using backtracking
# that checks if a colored solution is valid.
# If the node is valid, then the color of the node is added to 'node_colors' array
def four_color_theorem(graph):
    # Initializes array and sets values containing 4 ints; [0,1,2,3]
    coloring = {}
    colors = set(range(4))

    # Takes a node as input and colors the graph using recursion
    def backtrack(node):
        # Returns true if there are no more nodes to color
        if node is None:
            return True
        # Iterates through the 4 colors from 'colors' array
        for color in colors:
            # Continues if node has different color than adjacent nodes
            if is_valid_color(graph, node, color, coloring):
                # Add color to 'coloring' array
                coloring[node] = color
                # Recursively runs backtrack on the next adjacent node
                if backtrack(next_node()):
                    # Returns true if a valid color is found
                    return True
                del coloring[node]
        
        # Returns false if there are no solutions to given node
        return False
    
    # Finds the next adjacent connected node 
    def next_node():
        # Iterate through all nodes
        for node in graph.nodes():
            # Continutes if node is not colored
            if node not in coloring:
                return node
        return None

    # Continues if a valid coloring solution to the next node is found
    if backtrack(next_node()):
        return coloring

# Draws the graph of nodes onto the displays
# Makes graph follow the networkx kamada kawai layout
# The color of each node changes depending on passed input
def drawGraph(x):
    pos = nx.kamada_kawai_layout(G)
    nx.draw_networkx_labels(G, pos, font_color='Black')
    nx.draw(G, pos, node_size=1000, node_color=x)

# Assigns values from node_colors [red,blue,yellow, or green]
# Passes the values that are generated from 'coloring' function,
# and compares against the list of states from 'G.nodes'.
def colorGraph():
    # Iterate over every node in G.nodes
    for node in G.nodes:
        # Iterate over every state in the Queue
        for x in Queue:
            # Continues if 'node' and 'x' are equal (two states equal)
            if (node == x):
                color = node_colors[int(coloring.get(x))]
                # Adds 'color' value to the all_colors array
                all_colors.append(color)

    # Passes the first 50 values into 'drawGraph' function
    # Only 50 nodes in graph, so only 50 values are needed.
    drawGraph(all_colors[:50])

# Takes inputted value from first text box
def submitOne(text):
    global startNode
    # Assigns start node to given variable
    startNode = text

# Takes inputted value from second text box
def submitTwo(text):
    global endNode
    # Assigns end node to given variable
    endNode = text
    # Clears the graph, colors the graph.
    plt.clf()
    colorGraph()
    # Prints node path from start to end
    # Prints path found from astar algorithm (all weights are same)
    # Prints length of path from start to end
    plt.text(-1,1.12, 'Path from start node to end node:',fontsize=15)
    plt.text(-1,1, nx.astar_path(G, startNode, endNode), fontsize=15)
    plt.text(-1,0.88, int(len(nx.astar_path(G, startNode, endNode)))-1, fontsize=15)
    plt.show()

# Creates graph
G = nx.DiGraph()

# Initialize each state as a connection of nodes
G.add_node('HI')
G.add_node('AK')
G.add_edge('AL','MS')
G.add_edge('AL','TN')
G.add_edge('AL','GA')
G.add_edge('AL','FL')
G.add_edge('AZ','CA')
G.add_edge('AZ','NV')
G.add_edge('AZ','UT')
G.add_edge('AZ','NM')
G.add_edge('AR','MO')
G.add_edge('AR','TN')
G.add_edge('AR','MS')
G.add_edge('AR','LA')
G.add_edge('AR','TX')
G.add_edge('AR','OK')
G.add_edge('CA','OR')
G.add_edge('CA','NV')
G.add_edge('CA','AZ')
G.add_edge('CO','WY')
G.add_edge('CO','NE')
G.add_edge('CO','KS')
G.add_edge('CO','OK')
G.add_edge('CO','NM')
G.add_edge('CO','UT')
G.add_edge('CT','NY')
G.add_edge('CT','MA')
G.add_edge('CT','RI')
G.add_edge('DE','NJ')
G.add_edge('DE','PA')
G.add_edge('DE','MD')
G.add_edge('FL','AL')
G.add_edge('FL','GA')
G.add_edge('GA','TN')
G.add_edge('GA','NC')
G.add_edge('GA','SC')
G.add_edge('GA','FL')
G.add_edge('GA','AL')
G.add_edge('ID','WA')
G.add_edge('ID','OR')
G.add_edge('ID','NV')
G.add_edge('ID','UT')
G.add_edge('ID','WY')
G.add_edge('ID','MT')
G.add_edge('IL','WI')
G.add_edge('IL','IN')
G.add_edge('IL','KY')
G.add_edge('IL','MO')
G.add_edge('IL','IA')
G.add_edge('IN','MI')
G.add_edge('IN','OH')
G.add_edge('IN','KY')
G.add_edge('IN','IL')
G.add_edge('IA','MN')
G.add_edge('IA','IL')
G.add_edge('IA','MO')
G.add_edge('IA','NE')
G.add_edge('IA','SD')
G.add_edge('IA','WI')
G.add_edge('KS','NE')
G.add_edge('KS','MO')
G.add_edge('KS','OK')
G.add_edge('KS','CO')
G.add_edge('KY','IL')
G.add_edge('KY','IN')
G.add_edge('KY','OH')
G.add_edge('KY','WV')
G.add_edge('KY','VA')
G.add_edge('KY','TN')
G.add_edge('KY','MO')
G.add_edge('LA','TX')
G.add_edge('LA','AR')
G.add_edge('LA','MS')
G.add_edge('ME','NH')
G.add_edge('MD','PA')
G.add_edge('MD','DE')
G.add_edge('MD','VA')
G.add_edge('MD','WV')
G.add_edge('MA','VT')
G.add_edge('MA','NH')
G.add_edge('MA','NY')
G.add_edge('MA','CT')
G.add_edge('MA','RI')
G.add_edge('MI','WI')
G.add_edge('MI','IN')
G.add_edge('MI','OH')
G.add_edge('MN','ND')
G.add_edge('MN','SD')
G.add_edge('MN','IA')
G.add_edge('MS','AR')
G.add_edge('MS','LA')
G.add_edge('MS','TN')
G.add_edge('MS','AL')
G.add_edge('MO','IA')
G.add_edge('MO','IL')
G.add_edge('MO','KY')
G.add_edge('MO','TN')
G.add_edge('MO','AR')
G.add_edge('MO','OK')
G.add_edge('MO','KS')
G.add_edge('MO','NE')
G.add_edge('MT','ND')
G.add_edge('MT','SD')
G.add_edge('MT','WY')
G.add_edge('MT','ID')
G.add_edge('NE','SD')
G.add_edge('NE','IA')
G.add_edge('NE','MO')
G.add_edge('NE','KS')
G.add_edge('NE','CO')
G.add_edge('NE','WY')
G.add_edge('NV','CA')
G.add_edge('NV','OR')
G.add_edge('NV','ID')
G.add_edge('NV','UT')
G.add_edge('NV','AZ')
G.add_edge('NH','VT')
G.add_edge('NH','ME')
G.add_edge('NH','MA')
G.add_edge('NJ','NY')
G.add_edge('NJ','DE')
G.add_edge('NJ','PA')
G.add_edge('NM','CO')
G.add_edge('NM','OK')
G.add_edge('NM','TX')
G.add_edge('NM','AZ')
G.add_edge('NY','VT')
G.add_edge('NY','MA')
G.add_edge('NY','CT')
G.add_edge('NY','NJ')
G.add_edge('NY','PA')
G.add_edge('NC','VA')
G.add_edge('NC','TN')
G.add_edge('NC','GA')
G.add_edge('NC','SC')
G.add_edge('ND','MT')
G.add_edge('ND','SD')
G.add_edge('ND','MN')
G.add_edge('OH','MI')
G.add_edge('OH','IN')
G.add_edge('OH','KY')
G.add_edge('OH','WV')
G.add_edge('OH','PA')
G.add_edge('OK','CO')
G.add_edge('OK','KS')
G.add_edge('OK','MO')
G.add_edge('OK','AR')
G.add_edge('OK','TX')
G.add_edge('OK','NM')
G.add_edge('OR','WA')
G.add_edge('OR','ID')
G.add_edge('OR','NV')
G.add_edge('OR','CA')
G.add_edge('OR','WA')
G.add_edge('PA','NY')
G.add_edge('PA','NJ')
G.add_edge('PA','DE')
G.add_edge('PA','MD')
G.add_edge('PA','WV')
G.add_edge('PA','OH')
G.add_edge('RI','MA')
G.add_edge('RI','CT')
G.add_edge('SC','NC')
G.add_edge('SC','GA')
G.add_edge('SD','ND')
G.add_edge('SD','MT')
G.add_edge('SD','MN')
G.add_edge('SD','WY')
G.add_edge('SD','NE')
G.add_edge('SD','IA')
G.add_edge('TN','KY')
G.add_edge('TN','MO')
G.add_edge('TN','AR')
G.add_edge('TN','VA')
G.add_edge('TN','MS')
G.add_edge('TN','AL')
G.add_edge('TN','GA')
G.add_edge('TN','NC')
G.add_edge('TX','NM')
G.add_edge('TX','OK')
G.add_edge('TX','AR')
G.add_edge('TX','LA')
G.add_edge('UT','ID')
G.add_edge('UT','NV')
G.add_edge('UT','AZ')
G.add_edge('UT','CO')
G.add_edge('UT','WY')
G.add_edge('VT','NH')
G.add_edge('VT','MA')
G.add_edge('VT','NY')
G.add_edge('VA','KY')
G.add_edge('VA','WV')
G.add_edge('VA','MD')
G.add_edge('VA','TN')
G.add_edge('VA','NC')
G.add_edge('WA','OR')
G.add_edge('WA','ID')
G.add_edge('WV','OH')
G.add_edge('WV','PA')
G.add_edge('WV','MD')
G.add_edge('WV','VA')
G.add_edge('WV','KY')
G.add_edge('WI','MI')
G.add_edge('WI','IL')
G.add_edge('WI','IA')
G.add_edge('WI','MN')
G.add_edge('WY','MT')
G.add_edge('WY','SD')
G.add_edge('WY','NE')
G.add_edge('WY','CO')
G.add_edge('WY','UT')
G.add_edge('WY','ID')

# Creates an array of size 50 (Amount of states)
Queue = [50]
# Creates array that holds the color of each state
all_colors = []
# Creates array that gives color value from an integer
node_colors = {0: 'Red', 1: 'Blue', 2: 'Yellow', 3: 'Green'}

# Adds each value from G.nodes into the Queue
for i in list(G.nodes):
    Queue.append(i)
    
# Calls the four_color_theorem function while passing the graph of nodes
coloring = four_color_theorem(G)

# Prints the graph, makes the color of each node gray
plt.show()
drawGraph('Gray')

# Creates and initializes each text box to wait for user input; prints on given axes
text_box = TextBox(plt.axes([0.1, 0.02, 0.05, 0.05]), 'Enter start state:', initial="")
text_box2 = TextBox(plt.axes([0.4, 0.02, 0.05, 0.05]), 'Enter end state:', initial="")
text_box.on_submit(submitOne)
text_box2.on_submit(submitTwo)

# Displays the plot
plt.show()

# Prints the array that gives color value from an integer
print(node_colors)
# Prints a list ordered '[state]: [int]'
# Given by each state, and the color value assigned to it from node_colors
print(coloring)
