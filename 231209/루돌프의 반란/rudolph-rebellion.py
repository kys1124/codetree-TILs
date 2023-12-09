# 1번~P번 산타
# NxN M턴 루돌프 이동-> 산타 (1~P순서로 이동)
# 기절 산타와 탈락 산타는 이동 불가.
# 게임판 거리는 유클리드 거리^2
N, M, P, C, D = map(int,input().split())
ri,rj = map(lambda x:int(x)-1, input().split()) #루돌프 초기 위치
santa = {} #산타는 딕셔너리로 관리
score = [0]*(1+P) #산타별 점수관리 배열
arr = [[0]*N for _ in range(N)]
for _ in range(P):
    p_id, si,sj = map(int, input().split())
    santa[p_id] = [si-1,sj-1,0] #행 열 기절
    arr[si-1][sj-1] = p_id

def distance(si,sj,ei,ej):
    return (si-ei)**2+(sj-ej)**2

def move_ru(): #가장 가까운 탈락하지 않은 산타를 찾고, 그 산타에게 가는 8방향을 조사.
    mx_dist, mi,mj = (2*N)**2,-1,-1 #적당히 맵에서 최대거리보다 큰 수.
    for number in range(1,P+1):
        if santa.get(number): #탈락하지 않은 산타 조사.
            si,sj,_ =  santa[number]
            cur_dist = distance(ri,rj,si,sj)
            if mx_dist>cur_dist: #더 가까운 산타를 찾음.
                mx_dist, mi,mj = cur_dist,si,sj
            elif mx_dist==cur_dist: #거리가 동일
                if mi<si:#행이 큰 산타 우선
                    mi,mj =si,sj
                elif mi==si:
                    if mj<sj:
                        mj=sj

    mn_dist = mx_dist
    mdi,mdj = 0,0
    for di,dj in ((1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0, -1),(1,-1)):
        ni,nj = ri+di,rj+dj
        if 0<=ni<N and 0<=nj<N and mn_dist>distance(ni,nj,mi,mj):
            mn_dist = distance(ni,nj,mi,mj)
            mdi,mdj = di,dj
    return mdi,mdj

def move_santa(number):
    si,sj,trun = santa[number]
    mn_dist,mdi,mdj = distance(si,sj,ri,rj), 0,0 #현재 루돌프와의 거리, 가만히 있는 방향으로 초기화
    for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
        ni,nj = si+di,sj+dj
        if 0<=ni<N and 0<=nj<N and arr[ni][nj]==0 and mn_dist>distance(ni,nj,ri,rj):
            mn_dist,mdi,mdj = distance(ni,nj,ri,rj),di,dj
    return mdi,mdj

def crash(ri,rj,di,dj, power):
    number = arr[ri][rj] #부딪힌 산타 번호
    score[number]+=power #점수 획득
    arr[ri][rj] = 0
    ni,nj = ri+power*di,rj+power*dj
    if not (0<=ni<N and 0<=nj<N): #칸 밖으로 밀려남.
        del santa[number]
    elif arr[ni][nj]==0: #빈칸으로 밀려남.
        santa[number] = [ni,nj,2]
        arr[ni][nj]=number
    else: #다른 산타가 있어서 상호작용 발생.
        dfs(ni,nj,di,dj)
        arr[ni][nj] = number
        santa[number] = [ni,nj,2]

def dfs(si,sj,di,dj):
    stk =[(si,sj, arr[si][sj])]
    while stk:
        ci,cj,number = stk.pop()
        ni,nj = ci+di,cj+dj
        if not (0<=ni<N and 0<=nj<N):
            del santa[number] #밖으로 밀려났으므로 삭제.
        elif arr[ni][nj]==0:
            arr[ni][nj] = number
            santa[number] = [ni,nj,santa[number][2]]

        else: # 다른 산타 있음.
            stk.append((ni,nj,arr[ni][nj]))
            arr[ni][nj] = number
            santa[number] = [ni,nj,santa[number][2]]

for _ in range(M):
    di,dj = move_ru()
    # print("루돌프 원래좌표:", ri,rj)
    ri, rj = ri+di, rj+dj
    # print('루돌프 이동방향: ',di,dj, '루돌프 좌표:' ,ri,rj)
    # for x in arr:
    #     print(*x)
    # print('\n')
    if arr[ri][rj]!=0:
        crash(ri,rj,di,dj,C)

    for i in range(1,P+1):
        if not santa.get(i) or santa[i][2]>0: #기절 or 탈락 산타는 스킵.
            continue
        else:
            si,sj,turn = santa[i]
            di,dj = move_santa(i)
            ni,nj = si+di,sj+dj
            # print("산타 번호:",i,"산타원래 좌표:",si,sj,"산타 이동 좌표:",ni,nj)
            if (ri,rj)!=(ni,nj):
                arr[si][sj] = 0
                arr[ni][nj] = i
                santa[i] = [ni,nj,turn]
            else:
                arr[ri][rj] = i
                arr[si][sj] = 0
                crash(ri,rj,-di,-dj,D)

    for i in range(1,P+1):
        if santa.get(i):
            score[i]+=1
            if santa[i][2]>0:
                santa[i][2]-=1
    # print(santa)
print(*score[1:])