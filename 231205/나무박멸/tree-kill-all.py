N, M, K, C = map(int, input().split()) #격자 크기, 턴수, 확산범위, 지속 기간
arr = [list(map(int, input().split())) for _ in range(N)]
# -1은 벽, 나머지는 나무 그루수
v = [[0]*N for _ in range(N)] # 제초제 지속 기간 표시

def grow():
    copy_arr = [arr[i][:] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if copy_arr[i][j]>0:
                temp = 0
                for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                    ni,nj = i+di, j+dj
                    if 0<=ni<N and 0<=nj<N and copy_arr[ni][nj]>0:
                        temp+=1
                arr[i][j]+=temp

def bunsik():
    copy_arr = [arr[i][:] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if copy_arr[i][j]>0:
                lst = []
                for di,dj in ((1,0),(-1,0),(0,-1),(0,1)):
                    ni,nj = i+di, j+dj
                    if 0<=ni<N and 0<=nj<N and copy_arr[ni][nj]==0 and v[ni][nj]==0:
                        lst.append((ni,nj))

                if not lst:
                    continue
                tree = copy_arr[i][j]//len(lst)
                for ci,cj in lst:
                    arr[ci][cj]+=tree


def find_best():
    mx,mi,mj = 0,N,N
    for i in range(N):
        for j in range(N):
            if arr[i][j]==-1:
                continue
            cnt = arr[i][j]
            if arr[i][j]==0:
                if cnt==mx:
                    if mi>i:
                        mi,mj = i,j
                    elif mi==i:
                        if mj>j:
                            mj = j
            else: #확산 가능.
                for di,dj in ((1,1),(-1,1),(1,-1),(-1,-1)):
                    for mul in range(1,K+1):
                        ni,nj = i+mul*di, j+mul*dj
                        if 0<=ni<N and 0<=nj<N and arr[ni][nj]>0:
                            cnt+=arr[ni][nj]
                        else:
                            break
                if cnt>mx:
                    mx,mi,mj = cnt,i,j
                elif cnt==mx:
                    if mi>i:
                        mi,mj = i,j
                    elif mi==i:
                        if mj>j:
                            mj=j
    return mx,mi,mj

ans = 0
for _ in range(M):
    grow()
    bunsik()

    for i in range(N):
        for j in range(N):
            if v[i][j]>0:
                v[i][j]-=1

    mx, mi, mj = find_best()
    ans +=mx
    lst = []
    lst.append((mi,mj))
    if arr[mi][mj]>0:
        for di,dj in ((1,1),(1,-1),(-1,1),(-1,-1)):
            for mul in range(1,1+K):
                ni,nj = mi+mul*di, mj+mul*dj
                if 0<=ni<N and 0<=nj<N and arr[ni][nj]>0:
                    lst.append((ni,nj))
                elif 0<=ni<N and 0<=nj<N and arr[ni][nj]<=0:
                    lst.append((ni,nj))
                    break

    for ci,cj in lst:
        arr[ci][cj]=0
        v[ci][cj] = C

print(ans)