n, q = input().strip().split(' ')
n, q = [int(n), int(q)]
nodes = [int(nodes_temp) for nodes_temp in input().strip().split(' ')]
edges = []
for edges_i in range(n - 1):
    edges_t = [int(edges_temp) for edges_temp in input().strip().split(' ')]
    edges.append(edges_t)
for a0 in range(q):
    u, v = input().strip().split(' ')
    u, v = [int(u), int(v)]
    # your code goes here

print("done")