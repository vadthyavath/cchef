crawa:similar to Spirals made of line segments, with a small change

reverse:Construct an weighted undirected graph with 0 and 1 as weights:
Assign weights in the following manner,
if a and b are vertices then...
if only a--->b exists then assign '0' and if not a <--- b then '1'
if both a-->b and a<--b exists the both weights are '0'

Ex:
7 7
1 2 
3 2
3 4
7 4
6 2
5 6
7 5
undirected graph with adjacency list representation including weights:
{0: {1: 0}, 1: {0: 1, 2: 1, 5: 1}, 2: {1: 0, 3: 0}, 3: {2: 1, 6: 1}, 4: {5: 0, 6: 1}, 5: {1: 0, 4: 1}, 6: {3: 0, 4: 0}}
2

use Dijkstra's algorithm with heap to select mini weight vertex
