n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

visited=set()
graph=[[] for _ in range(n+1)]

for s, e in edges:
    graph[s].append(e)
    graph[e].append(s)

def dfs(st, visited):
    visited.add(st)

    for idx in graph[st]:
        if idx not in visited:
            dfs(idx, visited)

dfs(1, visited)

print(len(visited)-1)