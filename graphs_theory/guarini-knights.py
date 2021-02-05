# we put 2 white and two black knights
# in a 3x3 chess board....
# is it possible to move them to a specific
# combination from another one?
# that's possible only if the cases
# have same parity of permutation...
# with graphs we can see it better
# in this case, we can clearly see
# the optimal solutions!!!

# 3x3 table- knights in the corner
# can't reach the center
#  0  1  2
#  3  x  4
#  5  6  7
# knights position in table:
#  W  *  B      in G.nodes():
#  *  x  *  ->  "W*B**B*W"
#  B  *  W

import networkx as nx
import itertools as it
from nxpd import draw, nxpdParams
nxpdParams['show'] = 'ipynb'

G = nx.Graph();
# count=0;

for wb_indices in it.permutations(range(8),4):
	configuration = ['*'] * 8;
	configuration[wb_indices[0]] = 'W';
	configuration[wb_indices[1]] = 'W';
	configuration[wb_indices[2]] = 'B';
	configuration[wb_indices[3]] = 'B';
	G.add_node("".join(configuration));
	# count+=1;
	# if count <10:
	# 	print(wb_indices);
	# 	print("".join(configuration));

# Graph G contains, in each node, each
# possible configuration of the board
# it saves strings in the form: "WW*B**B*"

moves = [[] for _ in range(8)];
moves[0] = [4, 6];
moves[1] = [5, 7];
moves[2] = [3, 6];
moves[3] = [2, 7];
moves[4] = [0, 5];
moves[5] = [1, 4];
moves[6] = [0, 2];
moves[7] = [1, 3];

tup=[];

for i in range(len(moves)):
	for j in range(len(moves[i])):
		if  ( (str(i),str(moves[i][j])) not in tup ) and ( (str(moves[i][j]),str(i)) not in tup ):
			tup.append((str(i),str(moves[i][j])));

print(tup)
F = nx.Graph();
F.add_edges_from(tup);
draw(F, layout='circo');

# moves stores the possible moves
# i-> j, with j in moves[i];

for node in G.nodes():
	configuration = [c for c in node];

	for i in range(len(configuration)):
		if configuration[i] != "*":
			for new_pos in moves[i]:
				if configuration[new_pos] != "*":
					continue;
				new_configuration = list(configuration);

				new_configuration[i] = "*";
				new_configuration[new_pos] = configuration[i];
				# position changed only if its a legal move
				
				if not G.has_edge("".join(configuration), "".join(new_configuration)):
					G.add_edge("".join(configuration), "".join(new_configuration));
				# adding a node to the two configurations;
				# both are edged by a single movement of a piece;

print(nx.number_of_nodes(G));
print(nx.number_of_edges(G));
print(nx.number_connected_components(G));

assert "W*B**W*B" in nx.node_connected_component(G, "W*W**B*B");
assert "B*B**W*W" in nx.node_connected_component(G, "W*W**B*B");
assert "W*B**B*W" not in nx.node_connected_component(G, "W*W**B*B");

print(" -> ".join(nx.shortest_path(G, "W*W**B*B", "B*B**W*W")));
# printing the shortest path between two possible configurations;