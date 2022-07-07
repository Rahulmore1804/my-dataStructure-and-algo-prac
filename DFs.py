# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
dfs(visited, graph, 'A')




visiteds= set()
def BFSS(dict,st1key,visiteds):
    if st1key  not in visited:
        print(st1key)
        visited.add(st1key)
        for itemsornaifgerb in dict[st1key]:
            BFSS(dict,itemsornaifgerb,visiteds)



BFSS(graph, 'A',visited)
