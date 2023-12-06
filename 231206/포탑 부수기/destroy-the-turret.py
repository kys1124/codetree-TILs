# 4시 35분 시작
from collections import deque
N, M, K = map(int ,input().split()) # NxM K턴
arr = [list(map(int, input().split())) for _ in range(N)]
# 0은 부서진 포탑, >0 은 공격력을 나타냄.
# 만약 >0 이 1개 뿐이라면 그 즉시 중지. ******
v = [[0]*M for _ in range(N)] #공격했던 턴 수를 기록.

def find_weak(): #공격자를 선정.
    mn_power, mn_recent, mi,mj = 5001, -1, -1  ,-1
    for i in range(N):
        for j in range(M):
            if arr[i][j]>0: #부서지지 않은 포탑.
                if arr[i][j]<mn_power:
                    mn_power,mn_recent,mi,mj = arr[i][j], v[i][j], i,j
                elif arr[i][j]==mn_power:
                    if v[i][j]>mn_recent:
                        mn_recent,mi,mj = v[i][j],i,j
                    elif v[i][j]==mn_recent:
                        if i+j>mi+mj:
                            mi,mj = i,j
                        elif i+j==mi+mj:
                            if j>mj:
                                mi,mj = i,j
    return mi,mj

def find_strong():
    mx_power, mx_recent, mi,mj = -1,K+1, N+M, M
    for i in range(N):
        for j in range(M):
            if arr[i][j]>0 and (i,j)!=(wi,wj):
                if arr[i][j]>mx_power:
                    mx_power,mx_recent,mi,mj = arr[i][j], v[i][j], i,j
                elif arr[i][j]==mx_power:
                    if v[i][j]<mx_recent:
                        mx_recent,mi,mj = v[i][j], i,j
                    elif v[i][j]==mx_recent:
                        if mi+mj>i+j:
                            mi,mj = i,j
                        elif mi+mj==i+j:
                            if mj>j:
                                mi,mj = i,j
    return mi,mj




def laser(si,sj,ei,ej):
    q = deque([(si,sj)])
    visited = [[0]*M for _ in range(N)]
    visited[si][sj]=1
    path = {}
    while q:
        for _ in range(len(q)):
            ci,cj = q.popleft()
            if (ci,cj)==(ei,ej):
                return path

            for di,dj in ((0,1),(1,0),(0,-1),(-1,0)):
                ni,nj = (ci+di)%N,(cj+dj)%M
                if visited[ni][nj]==0 and arr[ni][nj]>0:
                    visited[ni][nj]=1
                    q.append((ni,nj))
                    path[(ni,nj)] = (ci,cj)
    return {}

def potan(wi,wj, ei,ej):
    arr[ei][ej] = max(0,arr[ei][ej]-power)
    for di,dj in ((1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)):
        ni,nj = (ei+di)%N, (ej+dj)%M
        if (ni,nj)!=(wi,wj):
            arr[ni][nj] = max(0, arr[ni][nj]-power//2)
            lst.add((ni,nj))

for turn in range(1,K+1): # K번 반복.
    wi,wj = find_weak() # 가장 약한 포탑 선정.
    arr[wi][wj] += M+N #공격력 증가.
    si,sj = find_strong() #가장 강한 포탑 선정.

    v[wi][wj] = turn
    power = arr[wi][wj]

    path = laser(wi,wj,si,sj)
    lst = set([(si,sj),(wi,wj)])

    if path:
        arr[si][sj] = max(0,arr[si][sj]- power)
        while True:
            si, sj = path[(si, sj)]
            if (si,sj)==(wi,wj):
                break
            arr[si][sj] = max(0, arr[si][sj]-power//2)
            lst.add((si,sj))

    else: #포탄 공격
        potan(wi,wj,si,sj)

    sm = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j]>0:
                sm+=1

    if sm<=1:
        break

    for i in range(N):
        for j in range(M):
            if arr[i][j]>0 and (i,j) not in lst:
                arr[i][j]+=1

print(max(map(max, arr)))