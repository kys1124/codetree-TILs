import copy
L, N, Q = map(int, input().split())
arr = [[2]*(L+2)]+[[2]+list(map(int,input().split()))+[2] for _ in range(L)]+[[2]*(L+2)]
dir = {0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}

knight= {}
v = [[0]*(L+2) for _ in range(L+2)]
for i in range(1,N+1):
    r,c,h,w,k = map(int,input().split())
    knight[i] = [r,c,h,w,k]
    for row in range(h):
        for col in range(w):
            v[r+row][c+col] = i

origin = copy.deepcopy(knight)

def dfs(i,d):
    si,sj,h,w,_ = knight[i]
    stk = []
    visited = set()
    visited.add(i)
    flag = True
    for row in range(h):
        for col in range(w):
            stk.append((si+row,sj+row))
    while stk:
        ci,cj = stk.pop()
        di,dj = dir[d]
        ni,nj =ci+di, cj+dj
        if v[ni][nj]>0 and v[ni][nj] not in visited:
            visited.add(v[ni][nj])
            i,j,nh,nw,_ = knight[v[ni][nj]]
            for row in range(nh):
                for col in range(nw):
                    stk.append((i+row, j+col))
        if arr[ni][nj]==2:
            flag=False
    return visited,flag



for _ in range(Q):
    i,d = map(int, input().split())
    if not knight.get(i):
        continue
    group,flag = dfs(i,d)
    if not flag: #벽에 막혀 이동 불가.
        continue

    # 이동 가능.
    v =[[0]*(L+2) for _ in range(L+2)]
    for number in group:
        r,c,h,w,k = knight[number]
        r,c = r+dir[d][0],c+dir[d][1]
        if number==i:
            for row in range(h):
                for col in range(w):
                    v[r + row][c + col] = number
            knight[number] = [r,c,h,w,k]
        else:
            for row in range(h):
                for col in range(w):
                    v[r + row][c + col] = number
                    if arr[r+row][c+col]==1:
                        k-=1
            if k<=0:
                for row in range(h):
                    for col in range(w):
                        v[r+row][c+col]=0
                del knight[number]
            else:
                knight[number] = [r,c,h,w,k]
ans = 0

for key, value in knight.items():
    ans +=origin[key][4]-knight[key][4]
print(ans)