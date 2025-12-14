import math
import heapq


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n

    def find(self, a):
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
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

    
    k = 1000
    heap = []   

    for i in range(n):
        x1,y1,z1 = pts[i]
        for j in range(i+1, n):
            x2,y2,z2 = pts[j]
            d = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2   
            if len(heap) < k:
                heapq.heappush(heap, (-d, i, j))
            else:
               
                if -heap[0][0] > d:
                    heapq.heapreplace(heap, (-d, i, j))

    
    pairs = [(i,j) for _,i,j in heap]

    
    dsu = DSU(n)
    for i,j in pairs:
        dsu.union(i, j)

    
    comp = {}
    for i in range(n):
        r = dsu.find(i)
        comp[r] = comp.get(r, 0) + 1

    sizes = sorted(comp.values(), reverse=True)

   
    return sizes[0] *sizes[1] * sizes[2]



if __name__ == "__main__":
    print(solve("input.txt"))
