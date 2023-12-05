dir = {0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}

N,M,H, K = map(int, input().split())
people = {}
for _ in range(M):
    x,y,d = map(int,input().split())
    if d==1:
        people[(x-1,y-1)] = [1]
    else:
        people[(x-1,y-1)] = [2]

tree = [[0]*N for _ in range(N)]
for _ in range(H):
    x,y = map(lambda x:int(x)-1, input().split())
    tree[x][y] = 1

si,sj,sd = N//2, N//2, 0
v = [[0]*N for _ in range(N)]
v[si][sj]=1
ans = 0
flag = True
for turn in range(1,K+1):
    new_people = {}
    for key, value in people.items():
        ci,cj = key
        dist = abs(ci-si)+abs(cj-sj)
        if dist>3: #3초과인 도망자는 현재 위치 그대로
            if new_people.get((ci,cj)):
                new_people[(ci,cj)]+=value
            else:
                new_people[(ci,cj)] = value
            continue

        for cd in value:
            di,dj = dir[cd]
            ni,nj = ci+di,cj+dj
            if not (0<=ni<N and 0<=nj<N): #격자 벗어남.
                cd = (cd+2)%4 #방향 전환
                ni,nj = ci+dir[cd][0], cj+dir[cd][1] #한칸 이동
                if (ni,nj)!=(si,sj): #술래와 위치가 다르면
                    ci,cj = ni,nj #해당 위치가 현재로 바뀜
            elif (ni,nj)!=(si,sj):
                ci,cj = ni,nj

            if new_people.get((ci,cj)):
                new_people[(ci,cj)].append(cd)
            else:
                new_people[(ci,cj)] = [cd]



    if flag:
        si,sj = si+dir[sd][0], sj+dir[sd][1]
        v[si][sj] = 1
        ni,nj = si+dir[(sd+1)%4][0], sj+dir[(sd+1)%4][1]
        if v[ni][nj]==0:
            sd = (sd+1)%4
        if (si,sj)==(0,0):
            flag=False
            sd = 2
            v[si][sj] = 0
    else: # 반시계
        si,sj = si+dir[sd][0], sj+dir[sd][1]
        v[si][sj] = 0
        ni,nj = si+dir[sd][0], sj+dir[sd][1]
        if not (0<=ni<N and 0<=nj<N) or v[ni][nj]!=0:
            sd = (sd-1)%4
        if (si,sj)==(N//2,N//2):
            flag=True
            sd = 0
            v[si][sj]=1


    for mul in range(3):
        ni,nj = si+mul*dir[sd][0], sj+mul*dir[sd][1]
        if not (0<=ni<N and 0<=nj<N):
            break
        if new_people.get((ni,nj)) and tree[ni][nj]==0:
            ans += turn * len(new_people[(ni,nj)])
            del new_people[(ni,nj)]

    people = new_people
    if len(people)==0:
        break
print(ans)