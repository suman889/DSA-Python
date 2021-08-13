'''
Given a weighted, undirected and connected graph of V vertices and E edges, Find the shortest distance of all the vertex's from the source vertex S.
Note: The Graph doesn't contain any negative weight cycle.
'''



import sys

class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def get_minimum_from_list(self,dist,visited):
        m=100000
        n=len(dist)
        index=-1
        for i in range(n):
            if not visited[i] and dist[i]<m:
                m=dist[i]
                index=i
        return m,index
        
    def get_minimum_distance(self,adj,visited,dist):
        while True:
            minimum,index=self.get_minimum_from_list(dist,visited)
            if(index==-1):
                break
            visited[index]=True
            for n in adj[index]:
                if not visited[n[0]]:
                    if dist[n[0]]>dist[index]+n[1]:
                        dist[n[0]]=dist[index]+n[1]
        return dist
            
    def dijkstra(self, V, adj, S):
        #code here
       #print(adj)
        dist = [100000]*V
        visited=[False]*V
        dist[S]=0
        return self.get_minimum_distance(adj,visited,dist)