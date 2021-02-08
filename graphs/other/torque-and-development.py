#Roads and Libraries https://www.hackerrank.com/challenges/torque-and-development/problem

from collections import defaultdict

def roadsAndLibraries(n, c_lib, c_road, cities):
    def dfs(i):
        vset.add(i)
        ans=1
        if i in d:
            for j in d[i]:
                if j not in vset:
                    ans += dfs(j)
        return ans


    if c_road > c_lib:
        return c_lib * n

    vset = set()
    d = defaultdict(list)

    for u,v in cities:
        d[u].append(v)                    
        d[v].append(u)

    group = []

    for i in range(1, n+1):
        if i not in vset:
            group.append(dfs(i))
    return n * c_road +(c_lib - c_road) * len(group)


print roadsAndLibraries(3, 2, 1, [[1, 2], [3, 1], [2, 3]]) #4
print roadsAndLibraries(6, 2, 5, [[1, 3], [3, 4], [2, 4], [1, 2], [2, 3], [5, 6]]) #12