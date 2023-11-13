from collections import deque
# 입력
N,M,P,C,D = map(int, input().split())

def dist(r1,c1,r2,c2):
    return (r1-r2)**2+(c1-c2)**2

arr =[[0]*N for _ in range(N)] # 산타의 위치를 기록할 배열. 죽은 산타는 기록x
santa = dict() # 산타를 기록
score = dict() # 산타의 점수 기록.
si,sj = map(lambda x:int(x)-1, input().split()) #루돌프 초기 위치

for _ in range(P):
    num, sr,sc = map(int, input().split())
    santa[num] = [sr-1,sc-1, 0,0] #기절 상태, 죽은지 확인
    score[num] = 0
    arr[sr-1][sc-1] = num

def move_ru(si,sj):
    q = deque([(si,sj)])
    v = [[0]*N for _ in range(N)]
    v[si][sj] = 1
    lst = []
    while q:
        for _ in range(len(q)):
            ci,cj = q.popleft()
            for di,dj in ((1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)):
                ni,nj = ci+di,cj+dj
                if 0<=ni<N and 0<=nj<N and v[ni][nj]==0:
                    v[ni][nj]=1
                    if arr[ni][nj]>0:
                        lst.append((ni,nj))
                    q.append((ni,nj))
    if lst:
        lst.sort(key=lambda x:(dist(si,sj,x[0],x[1]),-x[0],-x[1]))
        ei,ej = lst[0][0], lst[0][1]
        cur_dist = dist(si,sj,ei,ej)
        mi,mj,mdi,mdj = -1,-1,-1,-1
        for di, dj in ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)):
            ni,nj = si+di,sj+dj
            if 0<=ni<N and 0<=nj<N and cur_dist>dist(ni,nj,ei,ej):
                cur_dist = dist(ni,nj,ei,ej)
                mi,mj,mdi,mdj =ni,nj,di,dj
        return mi,mj,mdi,mdj

def move_santa(pi,pj, si,sj):
    cur_dist = dist(pi,pj,si,sj)
    arr[pi][pj]=0
    mi,mj,mdi,mdj = pi,pj,0,0
    for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
        ni,nj = pi+di,pj+dj
        if 0<=ni<N and 0<=nj<N and arr[ni][nj]==0 and cur_dist>dist(ni,nj,si,sj):
            cur_dist = dist(ni,nj,si,sj)
            mi,mj,mdi,mdj = ni,nj, di,dj
    return mi,mj,mdi,mdj

def move_ru_and_crash(si,sj,dri,drj):
    number = arr[si][sj]
    score[number]+=C
    arr[si][sj]=0
    ni,nj = si+C*dri, sj+C*drj
    if not (0<=ni<N and 0<=nj<N):
        santa[number] = [-1,-1,0,1]
    elif arr[ni][nj]==0:
        santa[number] = [ni,nj,3,0]
        arr[ni][nj] = number
    else:
        stk = [(ni,nj,arr[ni][nj])]
        arr[ni][nj] = number
        santa[number] = [ni,nj,3,0]
        while stk:
            ci,cj,num = stk.pop()
            _,_,flag1,flag2 = santa[num]
            ni,nj = ci+dri,cj+drj
            if not (0<=ni<N and 0<=nj<N):
                santa[num] = [-1,-1,0,1]
            elif arr[ni][nj]==0:
                arr[ni][nj]=num
                santa[num] = [ni,nj,flag1,flag2]
            else:
                n_num = arr[ni][nj]
                stk.append((ni,nj,n_num))
                arr[ni][nj]=num
                santa[num] = [ni,nj,flag1,flag2]


def move_santa_and_crash(pi,pj,pdi,pdj):
    number = arr[pi][pj]
    score[number]+=D
    arr[pi][pj]=0
    ni,nj = pi-D*pdi, pj-D*pdj
    if not (0<=ni<N and 0<=nj<N):
        santa[number] = [-1,-1,0,1]
    elif arr[ni][nj]==0:
        santa[number] = [ni,nj,2,0]
        arr[ni][nj]=number
    else:
        n_num = arr[ni][nj]
        stk = [(ni,nj,n_num)]
        arr[ni][nj]= number
        santa[number] = [ni,nj,2,0]
        while stk:
            ci,cj, num = stk.pop()
            ni,nj = ci-pdi, cj-pdj
            _,_,flag1,flag2 = santa[num]
            if not (0<=ni<N and 0<=nj<N):
                santa[num] = [-1,-1,0,1]
            elif arr[ni][nj]==0:
                arr[ni][nj]=num
                santa[num]=[ni,nj,flag1,flag2]
            else:
                n_num = arr[ni][nj]
                stk.append((ni,nj,n_num))
                arr[ni][nj]=num
                santa[num] =[ni,nj,flag1,flag2]

for _ in range(M):
    for i in range(1,1+P): #모든 산타가 탈락이면 게임 종료.
        if santa[i][3]==0:
            break
    else:
        break

    si,sj, dri,drj = move_ru(si,sj)
    if arr[si][sj]>0:
        move_ru_and_crash(si,sj,dri,drj)

    for i in range(1,1+P): #모든 산타가 탈락이면 게임 종료.
        if santa[i][3]==0:
            break
    else:
        break

    for i in range(1,1+P):
        if santa[i][2]>0:
            santa[i][2]-=1

    for i in range(1,1+P):
        if santa[i][2]>0 or santa[i][3]==1:
            continue

        pi,pj,flag1, flag2 = santa[i]

        npi,npj,dpi,dpj = move_santa(pi,pj,si,sj)

        arr[npi][npj]= i
        santa[i] = [npi,npj,flag1,flag2]

        if (npi,npj)==(si,sj): #충돌
            move_santa_and_crash(npi,npj,dpi,dpj)

    for i in range(1, 1 + P):  # 모든 산타가 탈락이면 게임 종료.
        if santa[i][3] == 0:
            break
    else:
        break

    for i in range(1,1+P):
        if santa[i][3]==0:
            score[i]+=1
for i in range(1,1+P):
    print(score[i], end=' ')