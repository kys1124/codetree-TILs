N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
def dfs(idx,si,sj):
    v[si][sj] = idx
    stk = [(si,sj)]
    group[idx] = [(si,sj)]
    while stk:
        ci,cj = stk.pop()
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]==arr[si][sj]:
                v[ni][nj]=idx
                group[idx].append((ni,nj))
                stk.append((ni,nj))

def cal(a,b):
    a_cnt,b_cnt = len(group[a]), len(group[b])
    ai,aj = group[a][0]
    bi,bj = group[b][0]
    a_num, b_num = arr[ai][aj], arr[bi][bj]
    temp = 0
    if a_cnt<b_cnt:
        for ci,cj in group[a]:
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj = ci+di , cj+dj
                if 0<=ni<N and 0<=nj<N and v[ni][nj]==b:
                    temp+=1
    else:
        for ci,cj in group[b]:
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj = ci+di , cj+dj
                if 0<=ni<N and 0<=nj<N and v[ni][nj]==a:
                    temp+=1

    return (a_cnt+b_cnt)*a_num*b_num*temp

def rotate(arr):
    L = N//2
    new_arr =[[0]*N for _ in range(N)]
    for si,sj in ((0,0),(0,L+1),(L+1,0),(L+1,L+1)):
        for i in range(L):
            for j in range(L):
                new_arr[si+i][sj+j] = arr[si+L-1-j][sj+i]

    for i in range(N):
        new_arr[i][L] = arr[L][N-1-i]
        new_arr[L][i] = arr[i][L]
    return new_arr


v= [[0]*N for _ in range(N)]
group = {}
idx = 1
for i in range(N):
    for j in range(N):
        if v[i][j]==0:
            dfs(idx,i,j)
            idx+=1

for i in range(1,len(group)):
    for j in range(i+1, len(group)+1):
        ans += cal(i,j)

for _ in range(3):
    arr = rotate(arr)
    v = [[0] * N for _ in range(N)]
    group = {}
    idx = 1
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:
                dfs(idx, i, j)
                idx += 1

    for i in range(1, len(group)):
        for j in range(i + 1, len(group) + 1):
            ans += cal(i, j)
print(ans)