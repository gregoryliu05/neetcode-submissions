class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(set)
        for x,y in edges:
            adj[x].add(y)
            adj[y].add(x)
        seen= set([0])
        queue= deque()
        queue.append((0,-1))
        while queue:
            nd, pr = queue.popleft()
            for nxt in adj[nd]:
                if nxt == pr:
                    continue
                if nxt in seen:
                    return False
                seen.add(nxt)
                queue.append((nxt, nd))
        
        return len(seen)== n

