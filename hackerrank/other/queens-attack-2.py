# Queen's Attack II https://www.hackerrank.com/challenges/queens-attack-2/problem

 
def queensAttack(n, k, r_q, c_q, obstacles):
    if n==0:
        return 0
    vset=set([tuple(item) for item in obstacles])
    if (r_q,c_q) in vset:
        return 0
    directions=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
    count=0
    for u,v in directions:
        cur=(r_q+u,c_q+v)
        while 1<=cur[0]<=n and 1<=cur[1]<=n and cur not in vset:
            cur=(cur[0]+u,cur[1]+v)
            count+=1
    return count


print queensAttack(4, 0, 4, 4, []) # 9
print queensAttack(5, 3, 4, 3, [[5, 5], [4, 2], [2, 3]]) # 9
