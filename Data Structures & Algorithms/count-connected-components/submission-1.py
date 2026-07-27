class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # n = number of nodes
        # edges [a,b] a and b are connectd
        # connected component: 
        # - set of edges that are all connected
        # range of answers is 1:n inclusive

        seen = set()
        adj_list = [set() for _ in range(n)]
        for [a, b] in edges:
            adj_list[a].add(b)
            adj_list[b].add(a)
        print(adj_list)
        def bfs(node):
            queue = deque()
            queue.append(node)
            while queue:
                cur = queue.popleft()
                for nxt in adj_list[cur]:
                    if nxt not in seen:
                        queue.append(nxt)
                        seen.add(nxt)

        cnt = 0
        for i in range(n):
            if i in seen:
                continue
            cnt += 1
            seen.add(i)
            bfs(i)

        
        
        return cnt