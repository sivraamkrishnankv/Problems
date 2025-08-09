# 547. Number of Provinces
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.


def findCircleNum(self, isConnected):
    def dfs(i):
        vis[i]=True
        for j in adj[i]:
            dfs(j)
    adj={}
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
