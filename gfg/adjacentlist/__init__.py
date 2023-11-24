
from typing import List

class Solution:
    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:


if __name__ == "__main__":
    T = int(input())
    for t in range(T):

        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
        obj = Solution()
        ans = obj.eventualSafeNodes(V, adj)
        for nodes in ans:
            print(nodes, end=' ')
        print()