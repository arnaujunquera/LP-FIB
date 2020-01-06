import networkx as nx
import matplotlib.pyplot as plt

G=nx.read_gpickle("graph.gpickle")
pos = nx.circular_layout(G)
nx.draw(G, pos, labels={node:node for node in G.nodes()})
plt.savefig("image_graph.png", format="PNG")
plt.show()
