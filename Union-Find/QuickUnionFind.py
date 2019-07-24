class QuickUnionFind:
        def __init__(self, n):
            self.id = [None] * n
            self.sz = [0] * n
            for i in range(n):
                self.id[i] = i

        def _findroot(self, i):
            while self.id[i] != i:
                self.id[i] = self.id[self.id[i]] # Path compression
                i = self.id[i]
            return i

        def connected(self, p, q):
            return self._findroot(p) == self._findroot(q)

        def union(self, p, q):
            p_root = self._findroot(p)
            q_root = self._findroot(q)

            if p_root == q_root:
                return

            if self.sz[p_root] < self.sz[q_root]:
                self.id[p_root] = q_root
                self.sz[q_root] += 1
            else:
                self.id[q_root] = p_root
                self.sz[p_root] += 1
