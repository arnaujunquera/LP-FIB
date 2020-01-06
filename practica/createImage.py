import networkx as nx
import matplotlib.pyplot as plt

G=nx.read_gpickle("graph.gpickle")

pos = nx.circular_layout(G)
nx.draw(G, pos, labels={node:node for node in G.nodes()})

edge_labels = nx.get_edge_attributes(G,'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels)

plt.savefig("image_graph.png", format="PNG")
plt.show()
