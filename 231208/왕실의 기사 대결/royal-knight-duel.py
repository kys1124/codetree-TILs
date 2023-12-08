# L*L (1,1)왼상 (N,N)오하 빈칸 함정 벽 구성. 체스판 밖도 벽
# 기사들은 (r,c)좌상 기준으로 h*w 만큼 직사각형, k의 체력을 가짐.

# 이동 -> 상하좌우 1칸 이동 가능. 붙어있는 기사는 같이 1칸 밀림. -> 벽이 있으면 못움직임.

# 데미지-> 밀려난 기사만 피해를 입음. -> 함정 칸에서 직사각형 내의 함정의 수만큼 데미지.
# 다 밀리고 난 후 데미지를 입고 체력이 0이하면 판에서 사라짐.

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
            stk.append((si+row,sj+col))
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

    group, flag = dfs(i,d)
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
                        print(knight)
                        print(i,d)
                        for x in v:
                            print(*x)

            if k<=0:
                for row in range(h):
                    for col in range(w):
                        v[r+row][c+col]=0
                del knight[number]
            else:
                knight[number] = [r,c,h,w,k]
    for key in knight.keys():
        if key not in group:
            r,c,h,w,k = knight[key]
            for row in range(h):
                for col in range(w):
                    v[r + row][c + col] = key
ans = 0

for key, value in knight.items():
    ans +=origin[key][4]-knight[key][4]
print(ans)