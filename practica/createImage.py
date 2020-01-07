import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
G=nx.DiGraph()
print(type(G))
G=nx.read_gpickle("graph.gpickle")
print(type(G))

pos = nx.circular_layout(G)

colors = nx.get_edge_attributes(G, 'color')
edge_colors = [colors[edge] for edge in G.edges()]

nx.draw(G, pos, node_size = 600, edge_color = edge_colors, labels={node:node for node in G.nodes()})

edge_labels = nx.get_edge_attributes(G,'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels)

plt.savefig("image_graph.png", format="PNG")
plt.show()
