import json

import networkx as nx
import matplotlib.pyplot as plt

file_name = "src/request-small-graph.json"
with open(file_name, 'r') as f:
    data = json.load(f)

G = nx.Graph()
for node in data['graph']:
    for connection in node['connections']:
        G.add_edge(node['id'], connection)

nx.draw_networkx(G, with_labels=True)
# plt.savefig("simple_path.png")
plt.show()