import heapq
"""
http://www.codechef.com/AUG14/problems/REVERSE/
"""
 
def dijkstra(graph,start, goal):
    sptset=[False]*goal
    distance=[10**6 for x in xrange(goal)]
    distance[start-1]=0
    heap=[]
    u=start-1
    heapq.heappush(heap,(0,u))
   
    while heap:
        minidist, u = heapq.heappop(heap)
        distance[u]=minidist
        #print "u value%d"%u
        #print "distance of u%d"%distance[u]
 
        if u==goal-1:
            #print "in break"
            break
        else:
            #print "in else"
            sptset[u]=True
            for next in graph[u]:
                #print "next value is %d"%next
                #print not sptset[next]
                #print distance[u]+matrix[u][next] 
                #print distance[next]
 
              
                if not sptset[next] and distance[u]+graph[u][next] < distance[next]:
                   
                    distance[next]=distance[u]+graph[u][next]
                    heapq.heappush(heap, (distance[next], next))
                    #print "distance[next]%d"%distance[next]
 
    #print sptset
    if distance[goal-1]==10**6:
        print -1
    else:
        print distance[goal-1]    
 
 
n,m=map(int,raw_input().split())
graph={}
for j in xrange(m):
 
    p,q=map(int,raw_input().split())
    x=p-1
    y=q-1
#constructing undirected graph(adjacency list representation)
    if x in graph:
        if y in graph[x]:
            if graph[x][y]==1:
                graph[x][y]=0
        else:
            graph[x][y]=0
    else:
        graph[x]={}
        graph[x][y]=0
 
    if y in graph:
        if x not in graph[y]:
            graph[y][x]=1
    else:
        graph[y]={}
        graph[y][x]=1
#print graph

dijkstra(graph,1, n) 
