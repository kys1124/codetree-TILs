N , M , K = map(int, input().split()) #N*N , M팀, K라운드
# 팀 별로 위치를 dictionary로 저장.
arr = [list(map(int, input().split())) for _ in range(N)]
dir = {0:(0,1),1:(-1,0),2:(0,-1),3:(1,0)}
team_dir = [1]*(M+1) #1은 정방향 insert(0,pop), -1 인경우 append(pop(0))
team = {}
path = {}
v = [[0]*N for _ in range(N)]

def dfs(si,sj, idx):
    stk = [(si,sj)]
    team[idx] =[1]
    path[idx] = [(si,sj)]
    v[si][sj]= idx
    while stk:
        ci,cj = stk.pop()
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and 0<=arr[ni][nj]-arr[ci][cj]<=1:
                v[ni][nj]=idx
                if arr[ni][nj]!=4:
                    team[idx].append(arr[ni][nj])
                path[idx].append((ni,nj))
                stk.append((ni,nj))

def ball(turn):
    t = turn%(4*N)
    if 0<=t<=N-1:
        si,sj,sd = t,-1,0
    elif N<=t<=2*N-1:
        si,sj,sd = N,t-N,1
    elif 2*N<=t<=3*N-1:
        si,sj,sd = 3*N-1-t, N, 2
    else:
        si,sj,sd = -1,4*N-1-t, 3
    return si,sj,sd

ans = 0
idx= 1
for i in range(N):
    for j in range(N):
        if arr[i][j]==1:
            dfs(i,j,idx)
            idx+=1

for turn in range(K):
    arr = [[0]*N for _ in range(N)]
    for i in range(1,M+1):
        if team_dir[i]==1:
            path[i].insert(0,path[i].pop())
        else:
            path[i].append(path[i].pop(0))

        for j in range(len(team[i])):
            ci,cj = path[i][j]
            number = team[i][j]
            arr[ci][cj] = number

    si,sj,sd = ball(turn)

    for _ in range(N):
        si,sj = si+dir[sd][0], sj+dir[sd][1]
        if arr[si][sj]!=0:
            number = v[si][sj]
            if team_dir[number]==1:
                pos = path[number].index((si,sj))+1
            else:
                pos = len(team[number])-path[number].index((si,sj))

            ans += pos**2
            team_dir[number]*=-1
            team[number].reverse()
            break

print(ans)