import math


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
        self.components = n  

    def find(self, a):
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a =self.parent[a]
        return a

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.components -= 1
        return True



def solve(filename="input.txt"):
    
    pts = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line:
                x,y,z = map(int, line.split(','))
                pts.append((x,y,z))

    n = len(pts)
    edges = []

    
    for i in range(n):
        x1,y1,z1 = pts[i]
        for j in range(i+1, n):
            x2,y2,z2 = pts[j]
            d = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
            edges.append((d, i, j))


    edges.sort()

    
    dsu = DSU(n)

    for d, i, j in edges:
        merged = dsu.union(i,j)
        if merged and dsu.components == 1:
            
            return pts[i][0] * pts[j][0] 


if __name__ == "__main__":
    print(solve("input.txt"))
