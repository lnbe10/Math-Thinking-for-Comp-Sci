import networkx as nx
import pygraphviz as pgv
from nxpd import draw, nxpdParams
nxpdParams['show'] = 'ipynb'


G = nx.Graph();

G.add_edges_from([('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'a'),
                  ('f', 'a'), ('g', 'b'), ('h', 'c'), ('i', 'd'), ('j', 'e'), 
                  ('f', 'h'), ('h', 'j'), ('j', 'g'), ('g', 'i'), ('i', 'f'),
                  ('j', 'i'), ('j', 'd'), ('d', 'g')
                ]);

draw(G, layout='circo');

cliques=nx.find_cliques(G)
max_clique = G.nodes()[0];
for c in cliques:
    if (len(c) > len(max_clique)):
        max_clique = c;
        
for v in max_clique:
    G.node[v]['color'] = 'red';
    for u in max_clique:
        if u != v:
            G[u][v]['color']='red';
            
draw(G, layout='circo');