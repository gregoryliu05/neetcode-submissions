class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # directed graph
        # [a,b] -> means have to take b before taking a
        # b -> a

        adj = [[] for _ in range(numCourses)]
        for a,b in prerequisites:
            adj[b].append(a)
        # if there is a cycle its not valid essentially 
        # there can be multiple connected components
        # so we have to check all of the nodes to see if any lead to a cycle
        # a -> b -> c -> d ->a
        #       -> e -> f-> g

        def dfs(node, seen):
            if node in seen:
                return False
            if adj[node] == []:
                return True
            seen.add(node)
            for nxt in adj[node]:
                if not dfs(nxt, seen):
                    return False
            seen.remove(node)
            adj[node] = []
            return True
            

        for i in range(numCourses):
            if not (dfs(i, set())):
                return False


        return True
        