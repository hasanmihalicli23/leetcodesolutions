class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parents = []

        for i in range(len(edges)+ 1):
            parents.append(i)

        ranks = [1] * (len(edges) + 1)

        def find(n):
            parent = parents[n]
            while parent != parents[parent]:
                parents[parent] = parents[parents[parent]]
                parent = parents[parent]
            return parent

        def union(n1,n2):
            parent1, parent2 = find(n1), find(n2)

            if parent1 == parent2:
                return False
            
            if ranks[parent1] > ranks[parent2]:
                parents[parent2] = parent1
                ranks[parent1] += ranks[parent2]
            else:
                parents[parent1] = parent2
                ranks[parent2] += ranks[parent1]
            return True

        for n1,n2 in edges:
            if not union(n1,n2):
                return[n1,n2]





