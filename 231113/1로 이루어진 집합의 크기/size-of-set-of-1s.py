N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

v = [[0]*M for _ in range(N)]
def dfs(si,sj,idx):
    q= [(si,sj)]
    v[si][sj] = idx
    cnt = 1
    while q:
        temp_q= []
        for k in range(len(q)):
            ci,cj = q[k]
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj = ci+di,cj+dj
                if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]==1:
                    v[ni][nj]= idx
                    temp_q.append((ni,nj))
                    cnt+=1
        q = temp_q
    return cnt
mx = 0
idx = 1
cnt_lst = [0]
for i in range(N):
    for j in range(M):
        if arr[i][j]==1 and v[i][j]==0:
            cnt = dfs(i,j, idx)
            mx = max(mx, cnt)
            cnt_lst.append(cnt)
            idx+=1

for i in range(N):
    for j in range(M):
        if arr[i][j]==0:
            S = set()
            cnt = 1
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj = i+di,j+dj
                if 0<=ni<N and 0<=nj<M and arr[ni][nj]==1:
                    S.add((v[ni][nj]))
            for num in S:
                cnt+= cnt_lst[num]
            mx = max(cnt,mx)
print(mx)