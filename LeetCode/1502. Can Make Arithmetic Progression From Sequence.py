from collections import defaultdict
def findCircleNum(self, isConnected):
    def dfs(i):
        vis[i]=True
        for j in adj[i]:
            if not vis[j]:
                dfs(j)
    adj=defaultdict(list)
    for i in range(len(isConnected)):
        for j in range(len(isConnected[0])):
            if isConnected[i][j]==1 and i!=j:
                adj[i].append(j)
                adj[j].append(i)
    c=0
    vis=[False]*len(isConnected)
    for i in range(len(isConnected)):
        if not vis[i]:
            dfs(i)
            c+=1
    return c