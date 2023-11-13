N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


def dfs(si,sj,idx):
    stk = [(si,sj)]
    v[si][sj]=idx
    temp = 0
    for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
        ni,nj = si+di,sj+dj
        if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0:
            temp+=1
    if temp>0:
        lst.append((si,sj,temp))

    while stk:
        temp =0
        ci,cj = stk.pop()

        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]>0:
                v[ni][nj]=idx
                stk.append((ni,nj))
            elif 0<=ni<N and 0<=nj<M and arr[ni][nj]==0:
                temp+=1
        if temp>0:
            lst.append((ci,cj,temp))

ans = 0
while True:
    idx = 1
    v = [[0]*M for _ in range(N)]
    lst = []
    for i in range(N):
        for j in range(M):
            if arr[i][j]>0 and v[i][j]==0:
                dfs(i,j,idx)
                idx+=1

    for ci,cj,cnt in lst:
        arr[ci][cj] = max(0, arr[ci][cj]-cnt)

    if idx>2:
        print(ans)
        break
    elif idx==1:
        print(0)
        break

    ans+=1