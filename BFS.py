my_dict = { 'London': 2, 'New York': 1, 'Lahore': 6, 'Tokyo': 11}
print(list(my_dict.keys())[0])
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []}

print(list(graph.keys())[0])

def BFS(dict):
    vistedvertices = []
    remainigmemberinquue = []
    vistedvertices.append(list(graph.keys())[0])
    remainigmemberinquue.append(list(graph.keys())[0])

    while remainigmemberinquue:
        b = remainigmemberinquue.pop(0)
        print(f"{b}---->",end=' ')

        for items in dict[b]:
            if items not in vistedvertices:
                vistedvertices.append(items)
                remainigmemberinquue.append(items)

    



kk = BFS(graph)
       
# code of net
# graph = {
#   'A' : ['B','C'],
#   'B' : ['D', 'E'],
#   'C' : ['F'],
#   'D' : [],
#   'E' : ['F'],
#   'F' : []
# }

# print(graph['A'])

# visited = [] # List to keep track of visited nodes.
# queue = []     #Initialize a queue

# def bfs(visited, graph, node):
#   visited.append(node)
#   queue.append(node)

#   while queue:
#     s = queue.pop(0) 
#     print (s, end = " ") 

#     for neighbour in graph[s]:
#       if neighbour not in visited:
#         visited.append(neighbour)
#         queue.append(neighbour)

# # Driver Code
# bfs(visited, graph, 'A')


