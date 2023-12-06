from  collections import deque
# m명의 사람 t번은 t분에 베이스캠프 -> 편의점으로 이동.
N, M = map(int, input().split()) # NxN M명
arr = [list(map(int, input().split())) for _ in range(N)]
# 0빈칸, 1베이스캠프
market = {}
player = {}
check = [0]*(1+M)
def bfs(si,sj,ei,ej):
    q = deque([(si,sj)])
    v=[[0]*N for _ in range(N)]
    v[si][sj] = 1
    path = {}
    while q:
        for _ in range(len(q)):
            ci,cj = q.popleft()
            if (ci,cj)==(ei,ej):
                while True:
                    if path[(ci,cj)]==(si,sj):
                        return ci,cj
                    ci,cj = path[(ci,cj)]

            for di,dj in ((-1,0),(0,-1),(0,1),(1,0)):
                ni,nj = ci+di,cj+dj
                if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]!=-1:
                    v[ni][nj]=1
                    q.append((ni,nj))
                    path[(ni,nj)] =(ci,cj)

def findBaseCamp(ei,ej):
    q= deque([(ei,ej)])
    v= [[0]*N for _ in range(N)]
    v[ei][ej]=1
    while q:
        lst = []
        for _ in range(len(q)):
            ci,cj = q.popleft()
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj = ci+di,cj+dj
                if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]!=-1:
                    v[ni][nj]=1
                    q.append((ni,nj))
                    if arr[ni][nj]==1:
                        lst.append((ni,nj))
        if lst:
            lst.sort()
            return lst[0][0], lst[0][1]


for i in range(1,M+1):
    ei,ej = map(lambda x:int(x)-1, input().split())
    market[i] = (ei,ej) #딕셔너리로 가고 싶은 편의점 위치 저장.

T = 0
while True:
    for i in range(min(T,M+1)):
        if not player.get(i):
            continue
        ci,cj = player[i]
        ei,ej = market[i]
        ni,nj = bfs(ci,cj,ei,ej)
        player[i] = (ni,nj)

    for i in range(1,M+1):
        if player.get(i):
            if check[i]==0:
                ei,ej = market[i]
                if player[i]==market[i]:
                    check[i]=1
                    del player[i]
                    arr[ei][ej]=-1

    if sum(check)==M:
        break

    T+=1

    if T<=M:
        ei,ej = market[T]
        si,sj = findBaseCamp(ei,ej)
        player[T] = (si,sj)
        arr[si][sj]=-1

print(T)