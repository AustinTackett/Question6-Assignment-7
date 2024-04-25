import matplotlib.pyplot as plt
import networkx as nx

'''
GIT CLONE INTO PYCHARM PROJECT FROM URL
https://github.com/AustinTackett/Question6-Assignment-7.git

THEN TO ADD IN PYCHARM DEPENDENCIES GO TO IN TOOLBAR GO TO 
FILE->SETTINGS->PROJECT:(YOUR PROJECT NAME)->PYTHON INTERPRETER
THEN CLICK THE PLUS SIGN AND INSTALL THE PACKAGES 
"matplotlib" (3.8.4) AND "networkx" (3.3)
'''


G = nx.DiGraph()
input = [('I', 1), ('A', 5), ('E', 4), ('F', 1), ('T', 2), ('S', 3)]

for vertex, adjacent in input:
    G.add_node(vertex)

for index, vertex_pair in enumerate(input):
    vertex, adjacent_index = vertex_pair
    left_ajdacent_index = (index - adjacent_index) % len(input)
    right_ajdacent_index = (index + adjacent_index) % len(input)
    left_ajdacent = input[left_ajdacent_index][0]
    right_ajdacent = input[right_ajdacent_index][0]
    G.add_edge(vertex, left_ajdacent)
    G.add_edge(vertex, right_ajdacent)

nx.draw_networkx(G, arrows=True)

# There should be a pop up window in pycharm with graph
plt.show()