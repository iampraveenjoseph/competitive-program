class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph_dict={}
        for start,end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=[end]
        print(self.graph_dict)
    
    def vertex(self):
        return list(self.graph_dict.keys())

    
    def findedges(self):
        edgename = []
        for vrtx in self.graph_dict:
            for nxtvrtx in self.graph_dict[vrtx]:
                if (nxtvrtx, vrtx) not in edgename:
                    edgename.append((vrtx, nxtvrtx))
        return edgename

        
    def get_path(self,start,end,path=[]):
        path=path+[start]

        if start==end:
            return [path]
        
        if start not in self.graph_dict:
            return []
        final_path=[]
        for node in self.graph_dict[start]:
            if node not in path:
                new_path=self.get_path(node,end,path)
                for p in new_path:
                    final_path.append(p)
        return final_path
    

    def shortest_path(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return path
        if start not in self.graph_dict:
            return None
        
        shortest_path=None
        for node in self.graph_dict[start]:
            if node not in path:
                sp=self.shortest_path(node,end,path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path=sp
        return shortest_path
   

    def BFS(self,graph_dict, s): 
        visited = []
        queue=[s]
        while queue: 
            node = queue.pop(0) 
            
            if node not in visited:
                visited.append(node)
            neighbours=graph_dict[node]
            for neighbour in neighbours: 
                queue.append(neighbour) 
        print(visited)
    
    
    def DFS(self,graph_dict,s,vist):
        if s not in vist:
            vist.append(s)
            for n in graph_dict[s]:
                self.DFS(graph_dict,n,vist)
        return(vist)

routes=[
("Mumbai","Paris"),
("Mumbai","Dubai"),
("Paris","Dubai"),
("Paris","New York"),
("Dubai","New York"),
("New York","Toronto"),
]
graph_dict={'Mumbai': ['Paris', 'Dubai'], 'Paris': ['Dubai', 'New York'], 'Dubai': ['New York'], 'New York': ['Toronto'],'Toronto':[]}
route_graph=Graph(routes)
start="Mumbai"
end="Toronto"
print(f"Paths Between {start} and {end} is ",route_graph.get_path(start,end))
start="Mumbai"
end="Toronto"
print(f"Shortest Path Between {start} and {end} is ",route_graph.shortest_path(start,end))

print("DFS")
print(route_graph.DFS(graph_dict,'Paris',[]))


#print(route_graph.vertex())
#print(route_graph.findedges())
  
route_graph.BFS(graph_dict,'Paris')



